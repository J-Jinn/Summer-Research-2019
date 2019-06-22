"""
Social License to Operate
Advisor: Professor VanderLinden
Name: Joseph Jinn
Date: 5-29-19

SLO Twitter Dataset Analysis

###########################################################
Notes:

Work-in-progress.

###########################################################

Resources Used:

dataset_slo_20100101-20180510.json
dataset_20100101-20180510.csv

"""

################################################################################################################
################################################################################################################

import logging as log
import warnings
import time
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Import custom utility functions.
import slo_twitter_data_analysis_utility_functions as tweet_util
import slo_twitter_data_analysis_utility_functions_v2 as tweet_util_v2

#############################################################
# Adjust parameters to display all contents.
pd.options.display.max_rows = None
pd.options.display.max_columns = None
pd.options.display.width = None
pd.options.display.max_colwidth = 1000
# Seaborn setting.
sns.set()
# Set level of precision for float value output.
pd.set_option('precision', 12)
# Ignore these types of warnings - don't output to console.
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

"""
Turn debug log statements for various sections of code on/off.
(adjust log level as necessary)
"""
log.basicConfig(level=log.INFO)


################################################################################################################
################################################################################################################

def tweets_number_associated_companies(tweet_dataframe):
    """
    Function displays statistics on the # of Tweets associated with one versus multiple companies.

    :param tweet_dataframe: the Twitter dataset in a Pandas dataframe.
    :return: None.
    """
    # Number of rows in entire dataframe.
    number_rows_total = tweet_dataframe.shape[0]

    # Select only rows with one associated company. (don't graph company combos)
    single_company_only_df = tweet_dataframe.loc[tweet_dataframe['multiple_companies_derived_count'] == 1]

    # Number of rows associated with only one company.
    number_rows_one_company = single_company_only_df.shape[0]

    print(f"The # of Tweets associated with multiple companies is {number_rows_total - number_rows_one_company}")
    print(f"The # of Tweets associated with one company is {number_rows_one_company}")


################################################################################################################

def tweet_count_by_timedate_time_series(created_at_attribute_file, file_type):
    """
    Function computes time series statistics and visualizations on Tweet Creation Time-Date Stamp.

    This function will work for any JSON file or CSV file that contains a attribute or column named "tweet_created_at"
    and "company_derived".

    Note: Ensure input file is small enough to fit in RAM.  This function will not read in data by chunks!

    :param file_type: type of input file.
    :param created_at_attribute_file: the input file containing the "created_at" Tweet attribute.
    :return: None.
    """
    start_time = time.time()

    if file_type == "csv":
        twitter_data = pd.read_csv(f"{created_at_attribute_file}", sep=",")
    elif file_type == "json":
        twitter_data = pd.read_json(f"{created_at_attribute_file}",
                                    orient='records',
                                    lines=True)
    else:
        print(f"Invalid file type entered - aborting operation")
        return

    # Create a empty Pandas dataframe.
    dataframe = pd.DataFrame(twitter_data)

    # Select only rows with one associated company. (don't graph company combos)
    single_company_only_df = dataframe.loc[dataframe['multiple_companies_derived_count'] == 1]

    # 1st Plot.
    plt.figure(figsize=(18.5, 10.5), dpi=300)
    plt.title(f"Tweet Creation Time-Date Count by Year/Month/Day")
    plt.xlabel("Year/Month/Day")
    plt.ylabel("Tweet Count")
    pd.to_datetime(dataframe['tweet_created_at']).value_counts().resample('1D').sum().plot()
    plt.show()

    # 2nd Plot.
    plt.figure()
    grid = sns.FacetGrid(dataframe[['tweet_created_at', 'company_derived_designation']],
                         row='company_derived_designation', size=2,
                         aspect=10,
                         sharey=False)
    grid.map_dataframe(tweet_util_v2.ts_plot, 'tweet_created_at').set_titles('{row_name}')
    plt.show()

    # # 3rd Plot.
    # # FIXME - not working as intended.
    # plt.figure()
    # grid = sns.FacetGrid(dataframe[['retweeted_derived', 'tweet_created_at', 'company_derived']],
    # row='company_derived',
    #                      size=2, aspect=10,
    #                      sharey=False)
    # grid.map_dataframe(tweet_util_v2.ts_plot_2, 'tweet_created_at').set_titles('{row_name}')
    # plt.show()

    end_time = time.time()
    time_elapsed = (end_time - start_time) / 60.0
    log.debug(f"The time taken to visualize the statistics is {time_elapsed} minutes")


################################################################################################################

def retweet_statistics(tweet_dataframe):
    """
    Re-Tweet statistics and visualizations for the CSV format Twitter dataset.
    Uses the Pandas "value_counts()" function to display unique values for the attribute.
    Groups user-specified attribute by the company the Tweet is associated with.

    Note: The raw JSON file does not have associated "company" information.

    :param tweet_dataframe: the Twitter dataset in a Pandas dataframe.
    :return: None.
    """

    # Select only rows with one associated company. (don't graph company combos)
    single_company_only_df = tweet_dataframe.loc[tweet_dataframe['multiple_companies_derived_count'] == 1]

    print(f"ReTweeted Attribute Statistics for entire CSV dataset:")
    print(tweet_dataframe["retweeted_derived"].value_counts())
    print()

    print(f"ReTweeted Statistics for CSV dataset by Company:")
    print(f"Number of Tweets that are \"retweeted_derived\" Attribute by associated company: ")
    print(tweet_dataframe.groupby(['company_derived_designation', "retweeted_derived"]).size())
    print()

    # Graph the Statistics.
    print(f"Percentage of All Tweets that Are or Aren't Retweets' by Associated Company: ")
    plt.figure()
    grid = sns.FacetGrid(tweet_dataframe[["retweeted_derived", 'company_derived_designation']],
                         col='company_derived_designation',
                         col_wrap=6, ylim=(0, 1))
    grid.map_dataframe(tweet_util_v2.bar_plot, "retweeted_derived").set_titles('{col_name}') \
        .set_xlabels("ReTweet - 0.0 No, 1.0 Yes").set_ylabels("Percentage of All Tweets")
    plt.show()

    plt.figure()
    print(f"Percentage of All Tweets Associated with a Given Company by ReTweet Count")
    grid = sns.FacetGrid(tweet_dataframe[['tweet_id', 'company_derived_designation']],
                         col='company_derived_designation', col_wrap=6,
                         ylim=(0, 1),
                         xlim=(0, 10))
    grid.map_dataframe(tweet_util_v2.bar_plot_zipf, 'tweet_id').set_titles('{col_name}').set_xlabels(
        'ReTweeted Count').set_ylabels("Percentage of All Tweets")
    plt.show()

    # Retweet counts of the top Retweeted Tweets.
    print(f"\nReTweet counts for the Top (most) Retweeted Tweets.\n")
    print(tweet_dataframe[['company_derived_designation', 'tweet_id']].groupby('company_derived_designation') \
          .apply(lambda x: x['tweet_id'].value_counts().value_counts(normalize=True) \
                 .sort_index(ascending=False).head(3)))

    # Portion of top Retweeted Tweets.
    print(f"\nWhat Percentage of All Tweets for Given Company does the Top (most) Retweeted Tweets Comprise?.\n")
    print(tweet_dataframe[['company_derived_designation', 'tweet_id']].groupby('company_derived_designation') \
          .apply(lambda x: x['tweet_id'].value_counts(normalize=True).head()))


def retweet_statistics_2(tweet_dataframe):
    """
    TODO - implement.
    :param tweet_dataframe:
    :return:
    """


################################################################################################################

def user_screen_name_statistics(tweet_dataframe):
    """
    User screen-name by associated company related statistics and visualizations.

    Note: The raw JSON file does not have associated "company" information.

    :param tweet_dataframe: the Twitter dataset in a Pandas dataframe.
    :return: None.
    """
    # Increased limit in order to display all 5 users for all companies and combinations of companies.
    pd.options.display.max_rows = 1000

    # Select only rows with one associated company. (don't graph company combos)
    single_company_only_df = tweet_dataframe.loc[tweet_dataframe['multiple_companies_derived_count'] == 1]

    print("User Statistics for CSV dataset by Company: ")
    print("Top Tweet counts for Unique User by Associated Company.")
    print(
        tweet_dataframe[['company_derived_designation', 'user_screen_name']].groupby('company_derived_designation')
            .apply(lambda x: x['user_screen_name'].value_counts(normalize=True).head())
        # .value_counts(normalize=True)\
        # .sort_index(ascending=False).head())
    )
    print()

    # Graph the User Statistics.
    print("Number of Times a Percentage of Users Appears as Tweet Author for a Given Company: ")
    plt.figure()
    grid = sns.FacetGrid(tweet_dataframe[['user_screen_name', 'company_derived_designation']],
                         col='company_derived_designation',
                         col_wrap=6,
                         ylim=(0, 1),
                         xlim=(0, 10))
    grid.map_dataframe(tweet_util_v2.bar_plot_zipf, 'user_screen_name').set_titles('{col_name}').set_xlabels(
        'Appearance (Tweet author) Count').set_ylabels("Percentage of all Users")
    plt.show()


################################################################################################################

def tweet_character_counts(tweet_dataframe):
    """
    Character count for Tweet text by associated company related statistics and visualizations.

    Note: The raw JSON file does not have associated "company" information.

    :param tweet_dataframe: the Twitter dataset in a Pandas dataframe.
    :return: None.
    """
    # Select only rows with one associated company. (don't graph company combos)
    single_company_only_df = tweet_dataframe.loc[tweet_dataframe['multiple_companies_derived_count'] == 1]

    print("Character Count Statistics of Tweet Text for CSV dataset by Company: ")
    print("Character Count Relative Frequency Histogram: ")
    plt.figure()
    grid = sns.FacetGrid(tweet_dataframe[['text_derived', 'company_derived_designation']],
                         col='company_derived_designation', col_wrap=6,
                         ylim=(0, 1))
    grid.map_dataframe(tweet_util_v2.relhist_proc, 'text_derived', bins=10, proc=tweet_util_v2.char_len).set_titles(
        '{col_name}').set_xlabels("# of Characters").set_ylabels("Percentage of all Tweets")
    plt.show()

    print("Character Count Statistics of User Description Text for CSV dataset by Company: ")
    print("Character Count Relative Frequency Histogram: ")
    plt.figure()
    grid = sns.FacetGrid(tweet_dataframe[['user_description', 'company_derived_designation']],
                         col='company_derived_designation', col_wrap=6,
                         ylim=(0, 1))
    grid.map_dataframe(tweet_util_v2.relhist_proc, 'user_description', bins=10, proc=tweet_util_v2.char_len).set_titles(
        '{col_name}').set_xlabels("# of Characters").set_ylabels("Percentage of all Tweets")
    plt.show()


################################################################################################################

def attribute_describe(input_file_path, attribute_name_list, file_type):
    """
    Function utilizes Pandas "describe" function to return dataframe statistics.

    https://chrisalbon.com/python/data_wrangling/pandas_dataframe_descriptive_stats/

    Note: This function will not work for attributes whose values are "objects" themselves.
    (can only be numeric type or string)

    :param input_file_path: absolute file path of the dataset in CSV format.
    :param attribute_name_list:  list of names of the attributes we are analyzing.
    :param file_type: type of input file.
    :return: None.
    """
    start_time = time.time()

    if file_type == "csv":
        twitter_data = pd.read_csv(f"{input_file_path}", sep=",")
    elif file_type == "json":
        twitter_data = pd.read_json(f"{input_file_path}",
                                    orient='records',
                                    lines=True)
    else:
        print(f"Invalid file type entered - aborting operation")
        return

    # Create a empty Pandas dataframe.
    dataframe = pd.DataFrame(twitter_data)

    for attribute_name in attribute_name_list:
        print(f"\nPandas describe for \"{attribute_name}\":\n")
        print(dataframe[attribute_name].describe(include='all'))

    end_time = time.time()
    time_elapsed = (end_time - start_time) / 60.0
    log.debug(f"The time taken to visualize the statistics is {time_elapsed} minutes")


################################################################################################################

def count_nan_non_nan(input_file_path, attribute_name_list, file_type):
    """
    Function counts the number of NaN and non-Nan examples in a Pandas dataframe for the specified columns.

    :param input_file_path: absolute file path of the dataset in CSV format.
    :param attribute_name_list:  list of names of the attributes we are analyzing.
    :param file_type: type of input file.
    :return: None.
    """
    start_time = time.time()

    if file_type == "csv":
        twitter_data = pd.read_csv(f"{input_file_path}", sep=",", dtype=object)
    elif file_type == "json":
        twitter_data = pd.read_json(f"{input_file_path}",
                                    orient='records',
                                    lines=True)
    else:
        print(f"Invalid file type entered - aborting operation")
        return

    # Create a empty Pandas dataframe.
    dataframe = pd.DataFrame(twitter_data)

    number_examples = dataframe.shape[0]
    number_attributes = dataframe.shape[1]
    print(f"\nThe number of rows (examples) in the dataframe is {number_examples}")
    print(f"The number of columns (attributes) in the dataframe is {number_attributes}\n")

    for attribute_name in attribute_name_list:
        null_examples = dataframe[attribute_name].isnull().sum()
        non_null_examples = number_examples - null_examples

        print(f"The number of NaN rows for \"{attribute_name}\" is {null_examples}")
        print(f"The number of non-NaN rows for \"{attribute_name}\" is {non_null_examples}\n")

    end_time = time.time()
    time_elapsed = (end_time - start_time) / 60.0
    log.debug(f"The time taken to visualize the statistics is {time_elapsed} minutes")


################################################################################################################

def unique_values(input_file_path, attribute_list, file_type):
    """
    Function that determines the # of unique items based on specified attributes list to check for duplicate values.

    Note: If attribute_list is an empty List, then the function will use all columns in the dataframe to check for
    duplicate values.

    :param file_type: type of file to import. ("json" or "csv")
    :param input_file_path: absolute file path of the input file to extract the field from.
    :param attribute_list: List of attributes to use to determine the uniqueness of the examples in the dataframe.
    :return: the dataframe with only unique rows based on the specified attribute List for uniqueness checking.

    TODO - is this function even necessary/useful? Not functional yet.
    """

    if file_type == "csv":
        # Read in the CSV file.
        tweet_dataset = \
            pd.read_csv(f"{input_file_path}", sep=",")
    elif file_type == "json":
        # Read in the JSON file.
        tweet_dataset = pd.read_json(f"{input_file_path}",
                                     orient='records',
                                     lines=True)
    else:
        print("Invalid file type - aborting operation")
        return

    tweet_dataframe = pd.DataFrame(tweet_dataset)

    print(f"Dataframe shape: \n{tweet_dataframe.shape}\n")

    if len(attribute_list) == 0:
        # Drop any duplicate rows by checking all columns for duplicate values.
        tweet_dataframe.drop_duplicates()
    else:
        # Drop any duplicate rows by checking specified columns (attributes) for duplicate values.
        tweet_dataframe.drop_duplicates(subset=[f"{attribute_list}"])

    print(f"Dataframe shaped after dropping duplicate items: \n{tweet_dataframe.shape}\n")

    print(f"The number of unique rows in the dataframe after dropping duplicate values in attribute(s) "
          f"{attribute_list} is {tweet_dataframe.count()}")

    # Return the dataframe with only the unique items based on the check.
    return tweet_dataframe


################################################################################################################

def hashtags(tweet_dataframe):
    """
    Hashtag related statistics and visualizations.

    :param tweet_dataframe: the Twitter dataset in a dataframe.
    :return: None.

    FIXME - graphs function; text stats non-functional (TypeError: 'float' object is not iterable)
    """
    # Select only rows with one associated company. (don't graph company combos)
    single_company_only_df = tweet_dataframe.loc[tweet_dataframe['multiple_companies_derived_count'] == 1]

    # the number of hashtags within tweets
    print(f"The Number of Hashtags within Tweets:")
    tweet_dataframe['#hashtags'] = single_company_only_df['tweet_entities_hashtags'].apply(
        lambda x: len(x) if x is not None and not isinstance(x, float) else 0)
    # companies = df['company']

    plt.figure()
    grid = sns.FacetGrid(tweet_dataframe[['#hashtags', 'company_derived_designation']],
                         col='company_derived_designation', col_wrap=6,
                         ylim=(0, 1),
                         xlim=(-1, 10))
    grid.map_dataframe(tweet_util_v2.bar_plot, '#hashtags').set_titles('{col_name}') \
        .set_xlabels("# of Hashtags").set_ylabels("Percentage of All Tweets?")
    plt.show()

    # # top hashtags
    # single_company_only_df[['company_derived', 'tweet_entities_hashtags']].groupby('company_derived') \
    #     .apply(lambda x: pd.Series([hashtag
    #                                 for hashtags in x['tweet_entities_hashtags'] if hashtags is not None
    #                                 for hashtag in hashtags]) \
    #            .value_counts(normalize=True) \
    #            .head())
    #
    # # top hashtags, lower-cased
    # single_company_only_df[['company_derived', 'tweet_entities_hashtags']].groupby('company_derived') \
    #     .apply(lambda x: pd.Series([hashtag.lower()
    #                                 for hashtags in x['tweet_entities_hashtags'] if hashtags is not None
    #                                 for hashtag in hashtags]) \
    #            .value_counts(normalize=True) \
    #            .head())


################################################################################################################

def mentions(tweet_dataframe):
    """
    Mentions related statistics and visualizations.

    :param tweet_dataframe: the Twitter dataset in a dataframe.
    :return: None.
    """
    # Select only rows with one associated company. (don't graph company combos)
    single_company_only_df = tweet_dataframe.loc[tweet_dataframe['multiple_companies_derived_count'] == 1]

    print(f"tweet_entities_user_mentions_id count divided by length of tweet_dataframe")
    print(tweet_dataframe['tweet_entities_user_mentions_id'].count() / len(tweet_dataframe))

    print(f"tweet_in_reply_to_status_id count divided by length of tweet_dataframe")
    print(tweet_dataframe['tweet_in_reply_to_status_id'].count() / len(tweet_dataframe))

    # the number of mentions within tweets
    print(f"\nThe number of Mentions within the Tweets:")
    tweet_dataframe['#mentions'] = tweet_dataframe['tweet_entities_user_mentions_id']. \
        apply(lambda x: len(x) if isinstance(x, list) else 0)

    plt.figure()
    grid = sns.FacetGrid(tweet_dataframe[['#mentions', 'company_derived_designation']],
                         col='company_derived_designation', col_wrap=6,
                         ylim=(0, 1),
                         xlim=(-1, 10))
    grid.map_dataframe(tweet_util_v2.bar_plot, '#mentions').set_titles('{col_name}') \
        .set_xlabels("Number of Mentions").set_ylabels("Percentage of All Tweets?")
    plt.show()

    # top mentions
    print(f"Top (Most) Mentions for a Company by User Mentions ID")
    print(
        tweet_dataframe[['company_derived_designation', 'tweet_entities_user_mentions_id']].groupby(
            'company_derived_designation') \
            .apply(lambda x: pd.Series([mention
                                        for mentions in x['tweet_entities_user_mentions_id'] if mentions is not None
                                        for mention in mentions]) \
                   .value_counts(normalize=True) \
                   .head()))


################################################################################################################

def analyze_multi_company_tweets(tweet_dataframe):
    """
    This function simply provides a Pandas.describe() stat summary of the entire dataframe.

    :param tweet_dataframe: Tweet dataframe.
    :return: None.
    """
    dataframe = pd.DataFrame(tweet_dataframe)
    print(f"\nStat summary of multi-company Tweets:\n {dataframe.describe(include='all')}\n")


################################################################################################################

def unique_authors_tweet_counts(tweet_dataframe):
    """
    This function provides statistics on all unique authors and their Tweet post counts in the dataset.

    :param tweet_dataframe: Tweet dataframe.
    :return: None.

    TODO - implement graph of distribution of unique authors.
    """
    author_series = pd.Series(tweet_dataframe["user_screen_name"])
    print("All Unique Authors by User Screen Name and their Tweet Post Count:")
    print(author_series.value_counts(sort=True, ascending=False))


################################################################################################################

################################################################################################################

"""
Main function.  Execute the program.
"""
if __name__ == '__main__':
    start_time = time.time()

    # # Import CSV dataset and convert to dataframe.
    # tweet_csv_dataframe = tweet_util_v2.import_dataset(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/selected-attributes-final.csv",
    #     "csv")

    # # Import CSV dataset and convert to dataframe.
    # tweet_csv_dataframe = tweet_util_v2.import_dataset(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/selected-attributes-final-subset.csv",
    #     "csv")

    # # Specify and call data analysis functions on chunked raw JSON Tweet file.
    # tweet_util_v2.call_data_analysis_function_on_json_file_chunks(
    #     "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json", "none")

    ##############################################################

    # # Append new column to CSV dataset file indicating a single company name association or "multiple" for multiple
    # # company name associations.
    # tweet_util_v2.tweet_single_company_name_or_multiple_company_designation(tweet_csv_dataframe)
    #
    # # Append new column to CSV dataset file that records how long the user description text is.
    # tweet_util_v2.compute_user_description_text_length(tweet_csv_dataframe)
    #
    # # Extract all Tweets over this length.
    # tweet_util_v2.extract_tweets_over_specified_character_length(tweet_csv_dataframe, 140)
    #
    # # List all unique authors (user) and their Tweet counts.
    # unique_authors_tweet_counts(tweet_csv_dataframe)
    #
    # # Determine the language of Tweet text using spaCy NLP and append as new column in CSV dataset.
    # tweet_util_v2.spacy_language_detection(tweet_csv_dataframe)

    ##############################################################

    # # Isolate multi-company associated Tweets for data analysis and export to new CSV file.
    # tweet_util_v2.export_multi_company_tweets(tweet_csv_dataframe)
    #
    # # Import CSV dataset and convert to dataframe.
    # multi_company_tweets_df = tweet_util_v2.import_dataset(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/multi-company-tweets.csv",
    #     "csv")
    #
    # # Analyze the multi-company associated Tweets.
    # analyze_multi_company_tweets(multi_company_tweets_df)

    ##############################################################################################

    # # Display Tweet count by time-date time series statistics.
    # tweet_count_by_timedate_time_series(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/selected-attributes-temp.csv",
    #     "csv")
    #
    # # Determine whether Tweets have been re-Tweeted.
    # retweet_statistics(tweet_csv_dataframe)
    #
    # # Determine the Tweet count for most prolific user by company.
    # user_screen_name_statistics(tweet_csv_dataframe)
    #
    # # Determine the # of characters in Tweets via relative frequency histogram.
    # tweet_character_counts(tweet_csv_dataframe)
    #
    # # Hashtag Statistics.
    # hashtags(tweet_csv_dataframe)
    #
    # # Mentions Statistics.
    # mentions(tweet_csv_dataframe)
    #
    # # Tweets associated with one or multiple companies.
    # tweets_number_associated_companies(tweet_csv_dataframe)

    ##############################################################################################

    # # Read in JSON/CSV data as chunks and export to CSV/JSON files.
    # tweet_util_v2.generalized_data_chunking_file_export_function(
    #     "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json",
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/dataset-chunks/", "csv")

    # # Extract various nested attributes from a outer attribute in the raw JSON file and export to CSV or JSON file.
    # # We extract 13 different attributes (some nested).
    # tweet_util_v2.flatten_extract_nested_json_attributes(
    #     "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json",
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/test.csv",
    #     "retweeted_status",
    #     ['created_at', 'id', 'full_text', 'in_reply_to_status_id', 'in_reply_to_user_id', 'in_reply_to_screen_name',
    #      'retweet_count', 'favorite_count', 'lang', 'entities', 'user', 'coordinates', 'place'],
    #     "csv")

    # # Test the function on JSON files.
    # tweet_util_v2.flatten_extract_nested_json_attributes(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/twitter-dataset-flatten-json-test.json",
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/twitter-dataset-flatten-test_results",
    #     "retweeted_status",
    #     ['created_at', 'id', 'full_text', 'in_reply_to_status_id', 'in_reply_to_user_id', 'in_reply_to_screen_name',
    #      'retweet_count', 'favorite_count', 'lang', 'entities', 'user', 'coordinates', 'place'],
    #     "csv")

    # # Extract various single or multiple attributes in the raw JSON file and export to JSON or CSV.
    # tweet_util_v2.extract_single_multi_json_attributes(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/twitter-dataset-extract-json-test.json",
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/twitter-dataset-extract-test_results",
    #     ['created_at', 'id', 'full_text', 'in_reply_to_status_id', 'quoted_status_id',
    #      'in_reply_to_user_id', 'in_reply_to_screen_name',
    #      'retweet_count', 'favorite_count', 'lang'],
    #     "csv")

    ###############################################################################################

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

    additional_fields = ["company_derived_designation", "user_description_text_length"]

    required_fields = ['retweeted_derived', 'company_derived', 'text_derived',  # "tweet_quoted_status_id",
                       'tweet_url_link_derived', 'multiple_companies_derived', 'multiple_companies_derived_count',
                       'tweet_text_length_derived'] + tweet_fields + user_fields + entities_fields + additional_fields

    # # Analyze full-text.
    # attribute_describe(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/selected-attributes-temp.csv",
    #     required_fields, "csv")

    # # Determine the number of NaN and non-NaN rows for a attribute in a dataset.
    # count_nan_non_nan(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/selected-attributes-temp.csv",
    #     required_fields, "csv")

    ################################################################################################################

    end_time = time.time()

    time_elapsed_seconds = (end_time - start_time)
    time_elapsed_minutes = (end_time - start_time) / 60.0
    time_elapsed_hours = (end_time - start_time) / 60.0 / 60.0
    print(f"Time taken to process dataset: {time_elapsed_seconds} seconds, "
          f"{time_elapsed_hours} hours, {time_elapsed_minutes} minutes")

    ################################################################################################################
