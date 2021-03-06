"""
This Python file contains modules that processes a raw JSON Twitter data file into a formatted CSV file containing
various derived attributes and native attributes.

Original Author: Professor Keith VanderLinden
Modified by: Joseph Jinn
Modified for: SLO Twitter Data Analysis for Topic Modeling Research.
Date: June 19, 2019
Version: 2.0

Notes:

Ensure there is at least ONE existing non-null value for any attribute you wish to extract in the current data chunk,
otherwise you will encounter a error along the lines of: KeyError: 'quoted_status_id'

# TODO - implement language detection using "spaCy" and "spaCy-langdetect"
# TODO - parallelize the chunks, if possible.
"""

#########################################################################################################
#########################################################################################################

import os
import csv
import json
import re
import time
from fire import Fire
from pathlib import Path

import numpy as np
import pandas as pd
# from polyglot.text import Text, Word

import logging as log

log.basicConfig(level=log.INFO)

from settings import PTN_rt, PTN_companies

# Count irrelevant tweets.
unknown_company_count_global = 0
non_english_count_global = 0

# import dask.dataframe as dask_df


#########################################################################################################
#########################################################################################################

def create_dataset(json_data_filepath, dataset_filepath, encoding, drop_irrelevant_tweets):
    """This function rebuilds a dataset from the given raw JSON file.
    It reads/writes the (large) file in chunks.
    """
    global unknown_company_count_global, non_english_count_global
    log.info(f'\tloading raw tweets from {json_data_filepath}')

    # Load/save the file in chunks.
    count = 0
    include_header = True

    # for df_chunk in dask_df.read_json(json_data_filepath,
    #                                   orient='records',
    #                                   lines=True,
    #                                   blocksize=10000, encoding="ISO-8859-1"):
    #         print()

    for df_chunk in pd.read_json(json_data_filepath,
                                 orient='records',
                                 lines=True,
                                 chunksize=10000,
                                 # encoding=encoding,
                                 ):

        original_fields = ['created_at', 'id', 'full_text', 'in_reply_to_status_id',
                           'in_reply_to_user_id', 'in_reply_to_screen_name',
                           'retweet_count', 'favorite_count', 'lang']

        tweet_fields = ['tweet_created_at', 'tweet_id', 'tweet_full_text', 'tweet_in_reply_to_status_id',
                        'tweet_in_reply_to_user_id', 'tweet_in_reply_to_screen_name',
                        'tweet_retweet_count', 'tweet_favorite_count', 'tweet_lang']

        user_fields = ['user_id', 'user_name', 'user_screen_name', 'user_location', 'user_description',
                       'user_followers_count', 'user_friends_count', 'user_listed_count', 'user_favourites_count',
                       'user_statuses_count', 'user_created_at', 'user_time_zone', 'user_lang']

        entities_fields = ["tweet_entities_expanded_urls", "tweet_entities_hashtags", "tweet_entities_user_mentions_id",
                           "tweet_entities_user_mentions_name", "tweet_entities_user_mentions_screen_name",
                           "tweet_entities_symbols"]

        required_fields = ['retweeted_derived', 'company_derived', 'text_derived',  # "tweet_quoted_status_id",
                           'tweet_url_link_derived', 'multiple_companies_derived', 'multiple_companies_derived_count',
                           'tweet_text_length_derived'] + tweet_fields + user_fields + entities_fields

        # Rename main Tweet object fields.  Note: ORDER MATTERS for these two Lists during assignment/re-assignment.
        df_chunk[tweet_fields] = df_chunk[original_fields]
        # df_chunk["tweet_quoted_status_id"] = df_chunk["quoted_status_id"]

        # Extract Tweet "user" object fields.
        df_chunk[user_fields] = df_chunk.apply(compute_user_series, axis=1)

        # Extract Tweet "entities" fields.
        # TODO - combine these to improve computational speed/efficiency.
        df_chunk["tweet_entities_expanded_urls"] = df_chunk.apply(compute_expanded_urls, axis=1)
        df_chunk['tweet_entities_hashtags'] = df_chunk.apply(compute_hashtags, axis=1)
        df_chunk["tweet_entities_user_mentions_id"] = df_chunk.apply(compute_user_mentions_id, axis=1)
        df_chunk["tweet_entities_user_mentions_name"] = df_chunk.apply(compute_user_mentions_name, axis=1)
        df_chunk["tweet_entities_user_mentions_screen_name"] = df_chunk.apply(compute_user_mentions_screen_name, axis=1)
        df_chunk["tweet_entities_symbols"] = df_chunk.apply(compute_symbols, axis=1)

        # Create/update/infer fields. (original extracted/derived fifelds)
        df_chunk['retweeted_derived'] = df_chunk.apply(compute_retweet, axis=1)
        df_chunk['text_derived'] = df_chunk.apply(compute_full_text, axis=1)
        df_chunk['company_derived'] = df_chunk.apply(compute_company, axis=1)
        df_chunk['tweet_url_link_derived'] = df_chunk.apply(compute_url_link, axis=1)

        # Polyglot only works on Linux (PITA to get working on Windows - sometimes impossible)
        # df_chunk['language_polyglot'] = df_chunk.apply(update_language, axis=1)

        # Determine whether Tweet is associated with multiple companies and count # of companies.
        df_chunk[['multiple_companies_derived', 'multiple_companies_derived_count']] = \
            df_chunk.apply(compute_multiple_companies, axis=1)

        # Compute Tweet text length.
        df_chunk["tweet_text_length_derived"] = df_chunk.apply(compute_text_length, axis=1)

        # Remove irrelevant tweets (non-English or unknown-company).
        if drop_irrelevant_tweets:
            df_chunk = df_chunk[
                ((df_chunk['company'] != '') &
                 (df_chunk['lang'].str.startswith('en') |
                  df_chunk['language_polyglot'].str.startswith('en')))
            ]

        # Write each chunk to the combined dataset file.
        df_chunk[required_fields].to_csv(dataset_filepath,
                                         index=False,
                                         quoting=csv.QUOTE_NONNUMERIC,
                                         mode='a',
                                         header=include_header,
                                         )

        # Print a progress message.
        count += get_size(df_chunk)
        # Only include the header once, at the top of the file.
        include_header = False
        log.info(f'\t\tprocessed {count} records...')

        # Debug purposes.
        # break

    # Drop duplicate rows/examples/Tweets.
    df_full = pd.read_csv(dataset_filepath, sep=',', encoding="utf-8")
    # df_full = pd.read_csv(dataset_filepath, sep=',', encoding='ISO-8859-1')
    df_full.drop_duplicates(inplace=True)
    df_full.to_csv(dataset_filepath, index=False, header=True, quoting=csv.QUOTE_NONNUMERIC, encoding='utf-8')

    log.info(f'\tsaved the dataset to {dataset_filepath}'
             f'\n\t\tunknown company count: {unknown_company_count_global}'
             f'\n\t\tnon-English count: {non_english_count_global}'
             )


#########################################################################################################

def compute_text_length(row):
    """
    Function determines the length of the Tweet's text.

    :param row: current example in the dataframe we are operating on.
    :return: current example we are operating on.
    """
    derived_series = pd.read_json(json.dumps(row['text_derived']), typ='series')
    derived_series = pd.Series(derived_series)
    row["tweet_text_length_derived"] = derived_series.str.len()
    return row["tweet_text_length_derived"]


#########################################################################################################

def compute_url_link(row):
    """This function constructs a URL referencing the full context of the
    given tweet.
    """
    return f'https://twitter.com/-/status/{row["id"]}'


#########################################################################################################

def compute_retweet(row):
    """This function determines if a tweet is a retweet."""
    return row['full_text'].startswith('RT')


#########################################################################################################

def compute_full_text(row):
    """This function creates the full text, either from the tweet itself or,
    if the tweet is a retweet (RT) that has been truncated (... at the end),
    by pasting the retweet header onto the original tweet text.
    """
    full_text = row['full_text']

    # If needed, reconstruct the full tweet text from the original text,
    # leaving the retweet header intact.
    if full_text.startswith('RT @') \
            and full_text.endswith('\u2026') \
            and not pd.isnull(row['retweeted_status']):
        text_header = PTN_rt.search(row['full_text']).group()
        retweet_series = pd.read_json(json.dumps(row['retweeted_status']),
                                      typ='series')
        full_text = f'{text_header}{retweet_series["full_text"]}'

    return clean_text(full_text)


#########################################################################################################

# def update_language(row):
#     """This function computes an alternate language code for the given
#     tweet using TextBlob, a more reliable language coder.
#
#     # TODO - look at polyglot and textblob and try to get them working (or equivalent package)
#     """
#     global non_english_count_global
#     if row['lang'].startswith('en'):
#         # Leave English codes (i.e., en, en-gb) unchanged.
#         return row['lang']
#     else:
#         # Compute alternate code for non-English tweets, many of which are
#         # in English as well.
#         lang2 = Text(row['full_text']).language.code
#         if not lang2.startswith('en'):
#             non_english_count_global += 1
#             log.warning(f"\t\t\tnon-English tweet (will be dropped): "
#                            f"\n\t\t\t\tid: {row['id']}"
#                            f"\n\t\t\t\ttweet: {row['text']}"
#                            f"\n\t\t\t\tLanguage tags: {row['lang']} - {lang2}"
#                            )
#         return lang2


#########################################################################################################

def compute_user_series(row):
    """This function grabs the attributes specified in the List from the
    nested user JSON structure.
    """
    user_series = pd.read_json(json.dumps(row['user']), typ='series')
    user_series['description'] = clean_text(user_series['description'])

    user_fields = ['id', 'name', 'screen_name', 'location', 'description',
                   'followers_count', 'friends_count', 'listed_count', 'favourites_count', 'statuses_count',
                   'created_at',
                   'time_zone', 'lang']

    return user_series[user_fields]


#########################################################################################################

def compute_expanded_urls(row):
    """This function grabs the list of hashtags from the nested entities
    JSON structure.
    """
    entity_series = pd.read_json(json.dumps(row['entities']), typ='series')
    expanded_urls = list(map(lambda entry: entry['expanded_url'], entity_series['urls']))
    return ','.join(expanded_urls)


#########################################################################################################

def compute_hashtags(row):
    """This function grabs the list of hashtags from the nested entities
    JSON structure.
    """
    entity_series = pd.read_json(json.dumps(row['entities']), typ='series')
    hashtags = list(map(lambda entry: entry['text'], entity_series['hashtags']))
    return ','.join(hashtags)


#########################################################################################################

def compute_user_mentions_name(row):
    """
    This function extracts the nested attributes within the "entities" object of the main Tweet object.

    :param row: a Tweet (line) from the raw JSON file.
    :return: the extracted attributes as individual columns.
    """
    entity_series = pd.read_json(json.dumps(row['entities']), typ='series')
    user_mentions_name = list(map(lambda entry: entry['name'], entity_series['user_mentions']))
    return ','.join(user_mentions_name)


def compute_user_mentions_screen_name(row):
    """
    This function extracts the nested attributes within the "entities" object of the main Tweet object.

    :param row: a Tweet (line) from the raw JSON file.
    :return: the extracted attributes as individual columns.
    """
    entity_series = pd.read_json(json.dumps(row['entities']), typ='series')
    user_mentions_screen_name = list(map(lambda entry: entry['screen_name'], entity_series['user_mentions']))
    return ','.join(user_mentions_screen_name)


def compute_user_mentions_id(row):
    """
    This function extracts the nested attributes within the "entities" object of the main Tweet object.

    :param row: a Tweet (line) from the raw JSON file.
    :return: the extracted attributes as individual columns.
    """
    entity_series = pd.read_json(json.dumps(row['entities']), typ='series')
    user_mentions_id = list(map(lambda entry: entry['id'], entity_series['user_mentions']))
    return user_mentions_id


#########################################################################################################

def compute_symbols(row):
    """This function grabs the list of hashtags from the nested entities
    JSON structure.
    """
    entity_series = pd.read_json(json.dumps(row['entities']), typ='series')
    user_mentions_symbols = list(map(lambda entry: entry['text'], entity_series['symbols']))
    return ','.join(user_mentions_symbols)


#########################################################################################################

def compute_company(row):
    """This function identifies the target company from the tweet text, issuing
    a warning for unrecognized texts. It assumes that the full, untruncated
    tweet text has already been constructed (see compute_full_text()).
    """
    global unknown_company_count_global

    associated_company = []

    # Identify the target company using known patterns in the tweet text.
    tweet = row['text_derived'].lower()
    author = row['user_screen_name'].lower()
    for company_pattern in PTN_companies:
        if re.compile(author).fullmatch(company_pattern[2]):
            associated_company.append(company_pattern[0])
            break
        if company_pattern[1].search(tweet):
            associated_company.append(company_pattern[0])

    if len(associated_company) > 0:
        return '|'.join(associated_company)

    # No company pattern applies, so it's unclear how this tweet was selected.
    unknown_company_count_global += 1
    # log.warning(f"\t\t\tunrecognized company (will be dropped): "
    #             f"\n\t\t\t\tid: {row['tweet_id']}"
    #             f"\n\t\t\t\ttweet: {row['text_derived']}"
    #             f"\n\t\t\t\thashtags: {row['tweet_entities_hashtags']}")
    return ''


#########################################################################################################

def compute_multiple_companies(row):
    """
    Function determines whether a Tweet is associated with multiple companies.

    :param row: current example in the dataframe we are operating on.
    :return: current example we are operating on.
    """
    derived_series = pd.read_json(json.dumps(row['company_derived']), typ='series')
    derived_series = pd.Series(derived_series)
    derived_string = derived_series.to_string()
    if "|" in derived_string:
        row["multiple_companies_derived"] = True
    else:
        row["multiple_companies_derived"] = False

    row["multiple_companies_derived_count"] = derived_string.count('|') + 1
    return row[["multiple_companies_derived", "multiple_companies_derived_count"]]


#########################################################################################################

def get_size(df):
    """Get the number of rows in the given dataframe."""
    return df.shape[0]


#########################################################################################################

def clean_text(text):
    """Do simple text cleanup for the data processing files."""
    return text.replace('\n', ' ').replace('\r', ' ')


#########################################################################################################

def remove_filepath_if_exists(filepath):
    """Delete the given file if it exists."""
    if os.path.isfile(filepath):
        log.info(f'\tdeleting existing file: {filepath}')
        os.remove(filepath)


#########################################################################################################

def create_separate_company_datasets(dataset_filepath, dataset_path, filename_base):
    """Read the given full/combined dataset file and create/save
    company-specific groups.
    """
    log.info(f'\tsplitting dataset into company-specific datasets...')
    df = pd.read_csv(dataset_filepath, encoding='utf-8', engine='python')
    for company_name, group in df.groupby(['company_derived']):
        group.to_csv(
            dataset_path / f'{filename_base}-{company_name}.csv',
            index=False)


#########################################################################################################

def main(json_data_filepath='dataset.json',
         dataset_path='.',
         filename_base='dataset',
         encoding='utf-8',
         drop_irrelevant_tweets=True,
         add_company_datasets=False,
         logging_level=log.INFO,
         ):
    """This tool loads the raw JSON-formatted tweets from the given
    filepath, does some general updates to the dataset items and saves
    the results in filename (.csv). The columns are modified as
    follows:

    - The tweet text is modified to remove newlines (\\n, \\r).
    - A company column is added to identify the company of the tweet.
    - A language_textblob column is added to give a second (more accurate)
      language tag.

    Keyword Arguments:
        json_data_filepath -- the system path from which to load the raw JSON files
            (default='.')
        dataset_path -- the system path to which the dataset files are to be written
            (default='.')
        filename_base -- the base name of a/the pre-saved dataset files
            (default='dataset')
        encoding -- the file encoding to use
            (default: 'utf-8')
        add_company_datasets -- whether to add company-specific datasets
            (default: True)
        logging_level -- the level of logging to use
            (default: logging.INFO)
    """
    log.basicConfig(level=logging_level, format='%(message)s')
    log.info(f'building the dataset')

    if not os.path.isfile(json_data_filepath):
        log.fatal(f'\tfilepath doesn\'t exist: {json_data_filepath}')
        exit(-1)

    full_dataset_filepath = Path(dataset_path) / f'{filename_base}.csv'
    remove_filepath_if_exists(full_dataset_filepath)

    create_dataset(Path(json_data_filepath), full_dataset_filepath, encoding, drop_irrelevant_tweets)

    if add_company_datasets:
        create_separate_company_datasets(full_dataset_filepath,
                                         Path(dataset_path),
                                         filename_base)


#########################################################################################################
#########################################################################################################

if __name__ == '__main__':
    # Fire(main)
    # Example invocation:
    # python dataset_processor.py --json_data_filepath=/media/hdd_2/slo/stance/slo-tweets-20160101-20180304/dataset.json --dataset_path=/media/hdd_2/slo/stance/datasets

    start_time = time.time()

    # # Absolute file path.
    # create_dataset("D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json",
    #                "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/selected-attributes-final.csv",
    #                "utf-8", False)

    # # Relative file path.
    # create_dataset("/json/dataset_slo_20100101-20180510.json",
    #                "/jupyter-notebooks/attribute-datasets/selected-attributes-final.csv",
    #                "utf-8", False)

    end_time = time.time()

    time_elapsed_seconds = (end_time - start_time)
    time_elapsed_minutes = (end_time - start_time) / 60.0
    time_elapsed_hours = (end_time - start_time) / 60.0 / 60.0
    print(f"Time taken to process dataset: {time_elapsed_seconds} seconds, "
          f"{time_elapsed_hours} hours, {time_elapsed_minutes} minutes")

#########################################################################################################
#########################################################################################################
