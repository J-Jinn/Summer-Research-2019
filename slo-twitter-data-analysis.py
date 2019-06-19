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
import tensorflow as tf
import time
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Import custom utility functions.
import slo_twitter_data_analysis_utility_functions as tweet_util

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
tf.logging.set_verbosity(tf.logging.INFO)


################################################################################################################
################################################################################################################


def tweet_count_by_timedate_time_series(created_at_attribute_file, file_type):
    """
    Visualize the Tweet creation time based on time-date information in the "created_at" attribute field of the
    input file.

    This function will work for any JSON file or CSV file that contains a attribute or column named "created_at".

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

    # 1st Plot.
    plt.figure(figsize=(18.5, 10.5), dpi=300)
    plt.title(f"Tweet Creation Time-Date Count by Year/Month/Day")
    plt.xlabel("Year/Month/Day")
    plt.ylabel("Tweet Count")
    pd.to_datetime(dataframe['tweet_created_at']).value_counts().resample('1D').sum().plot()
    plt.show()

    # 2nd Plot.
    plt.figure()
    grid = sns.FacetGrid(dataframe[['tweet_created_at', 'company_custom']], row='company_custom', size=2, aspect=10,
                         sharey=False)
    grid.map_dataframe(tweet_util.ts_plot, 'tweet_created_at').set_titles('{row_name}')
    plt.show()

    # # 3rd Plot.
    # TODO - not working as intended.
    # grid = sns.FacetGrid(dataframe[['retweeted_custom', 'tweet_created_at', 'company_custom']], row='company_custom',
    #                      size=2, aspect=10,
    #                      sharey=False)
    # grid.map_dataframe(tweet_util.ts_plot_2, 'tweet_created_at').set_titles('{row_name}')
    # plt.show()

    end_time = time.time()
    time_elapsed = (end_time - start_time) / 60.0
    log.debug(f"The time taken to visualize the statistics is {time_elapsed} minutes")


################################################################################################################

def attribute_value_counts(tweet_dataframe, attribute_name):
    """
    User-specified attribute statistics and visualizations for the CSV format Twitter dataset.
    Uses the Pandas "value_counts()" function to display unique values for the attribute.
    Suggested use on Boolean attributes or other attributes with only a few unique values.
    Groups user-specified attribute by the company the Tweet is associated with.

    Note: The raw JSON file does not have associated "company" information.

    TODO - finish generalizaing or reverse and return to being specific to reTweets.
    :param tweet_dataframe: the Twitter dataset in a Pandas dataframe.
    :param attribute_name: name of the attribute we are analyzing.
    :return: None.
    """

    print(f"\"{attribute_name}\" Attribute Statistics for entire CSV dataset:")
    print(tweet_dataframe[attribute_name].value_counts())
    print()

    print(f"\"{attribute_name}\" Attribute Statistics for CSV dataset by Company:")
    print(f"Number of Tweets that are \"{attribute_name}\" Attribute by associated company: ")
    print(tweet_dataframe.groupby(['company_custom', attribute_name]).size())
    print()

    # Graph the Statistics.
    print(f"Proportion of \"{attribute_name}\" Attribute by associated company: ")
    plt.figure()
    grid = sns.FacetGrid(tweet_dataframe[[attribute_name, 'company_custom']], col='company_custom', col_wrap=6,
                         ylim=(0, 1))
    grid.map_dataframe(tweet_util.bar_plot, attribute_name).set_titles('{col_name}')
    plt.show()

    # TODO - understand what this represents.
    plt.figure()
    print(f"What does this represent?")
    grid = sns.FacetGrid(tweet_dataframe[['tweet_id', 'company_custom']], col='company_custom', col_wrap=6, ylim=(0, 1),
                         xlim=(0, 10))
    grid.map_dataframe(tweet_util.bar_plot_zipf, 'tweet_id').set_titles('{col_name}').set_xlabels('RTed count')
    plt.show()

    # Retweet counts of the top Retweeted Tweets.
    print(f"\nRetweet counts of the top Retweeted Tweets.\n")
    print(tweet_dataframe[['company_custom', 'tweet_id']].groupby('company_custom') \
          .apply(lambda x: x['tweet_id'].value_counts().value_counts(normalize=True) \
                 .sort_index(ascending=False).head(3)))

    # Portion of top Retweeted Tweets.
    print(f"\nPortion of top Retweeted Tweets.\n")
    print(tweet_dataframe[['company_custom', 'tweet_id']].groupby('company_custom') \
          .apply(lambda x: x['tweet_id'].value_counts(normalize=True).head()))


################################################################################################################

def most_tweets_by_users_per_company(tweet_dataframe):
    """
    User screen-name by associated company related statistics and visualizations.

    Note: The raw JSON file does not have associated "company" information.

    :param tweet_dataframe: the Twitter dataset in a Pandas dataframe.
    :return: None.
    """
    # Increased limit in order to display all 5 users for all companies.
    pd.options.display.max_rows = 1000

    print("User Statistics for CSV dataset by Company: ")
    print("Top Tweet counts for unique user by associated company.")
    print(
        tweet_dataframe[['company_custom', 'user_screen_name']].groupby('company_custom')
            .apply(lambda x: x['user_screen_name'].value_counts(normalize=True).head())
        # .value_counts(normalize=True)\
        # .sort_index(ascending=False).head())
    )
    print()

    # Graph the User Statistics.
    print("Proportion of most Tweets for unique users by associated company: ")
    plt.figure()
    grid = sns.FacetGrid(tweet_dataframe[['user_screen_name', 'company_custom']], col='company_custom', col_wrap=6,
                         ylim=(0, 1),
                         xlim=(0, 10))
    grid.map_dataframe(tweet_util.bar_plot_zipf, 'user_screen_name').set_titles('{col_name}').set_xlabels(
        'appearance count')
    plt.show()


################################################################################################################

def tweet_character_counts(tweet_dataframe):
    """
    Character count for Tweet text by associated company related statistics and visualizations.

    Note: The raw JSON file does not have associated "company" information.

    :param tweet_dataframe: the Twitter dataset in a Pandas dataframe.
    :return: None.
    """

    print("Character Statistics for CSV dataset by Company: ")
    print("Character count relative frequency histogram: ")
    plt.figure()
    grid = sns.FacetGrid(tweet_dataframe[['text_custom', 'company_custom']], col='company_custom', col_wrap=6,
                         ylim=(0, 1))
    grid.map_dataframe(tweet_util.relhist_proc, 'text_custom', bins=10, proc=tweet_util.char_len).set_titles(
        '{col_name}')
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
    Function counts the number of NaN and non-Nan examples in a Pandas dataframe.

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

    TODO - is this function even necessary/useful?
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

    FIXME - not functional.
    """
    # the number of hashtags within tweets
    tweet_dataframe['#hashtags'] = tweet_dataframe['hashtags_custom'].apply(
        lambda x: len(x) if x is not None and not isinstance(x, float) else 0)
    # companies = df['company']

    grid = sns.FacetGrid(tweet_dataframe[['#hashtags', 'company_custom']], col='company_custom', col_wrap=6,
                         ylim=(0, 1),
                         xlim=(-1, 10))
    grid.map_dataframe(tweet_util.bar_plot, '#hashtags').set_titles('{col_name}')

    # top hashtags
    tweet_dataframe[['company_custom', 'hashtags_custom']].groupby('company_custom') \
        .apply(lambda x: pd.Series([hashtag
                                    for hashtags in x['hashtags_custom'] if hashtags is not None
                                    for hashtag in hashtags]) \
               .value_counts(normalize=True) \
               .head())

    # top hashtags, lower-cased
    tweet_dataframe[['company_custom', 'hashtags_custom']].groupby('company_custom') \
        .apply(lambda x: pd.Series([hashtag.lower()
                                    for hashtags in x['hashtags_custom'] if hashtags is not None
                                    for hashtag in hashtags]) \
               .value_counts(normalize=True) \
               .head())


################################################################################################################

def mentions(tweet_dataframe):
    """
    Mentions related statistics and visualizations.

    :param tweet_dataframe: the Twitter dataset in a dataframe.
    :return: None.

    TODO - implement.  will need to extract mentions from Tweet text.
    """
    print("TODO - implement")


################################################################################################################

"""
Main function.  Execute the program.
"""
if __name__ == '__main__':
    # # Import CSV dataset and convert to dataframe.
    # tweet_csv_dataframe = tweet_util.import_dataset(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/selected-attributes.csv",
    #     "csv")

    ###############################################################################################

    # # Specify and call data analysis functions on chunked raw JSON Tweet file.
    # tweet_util.call_data_analysis_function_on_json_file_chunks(
    #     "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json", "none")

    # # Display Tweet count by time-date time series statistics.
    # tweet_count_by_timedate_time_series(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/selected-attributes.csv",
    #     "csv")

    # Determine whether Tweets have been re-Tweeted.
    # attribute_value_counts(tweet_csv_dataframe, "retweeted_custom")

    # # Determine the Tweet count for most prolific user by company.
    # most_tweets_by_users_per_company(tweet_csv_dataframe)

    # # Determine the # of characters in Tweets via relative frequency histogram.
    # tweet_character_counts(tweet_csv_dataframe)

    # Hashtag Statistics.
    # hashtags(tweet_csv_dataframe)

    # Mentions Statistics.

    ###############################################################################################

    # # Extract multiple fields from raw JSON file and export to CSV file.
    # tweet_util.generalized_multi_field_extraction_function(
    #     "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json",
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/",
    #     ["retweet_count", "retweeted", "favorite_count", "favorited"], "csv")
    #
    # Extract various individual fields from raw JSON file and export to CSV/JSON file.
    # tweet_util.generalized_field_extraction_function(
    #     "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json",
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/",
    #     "entities", "csv")
    #
    # # Read in JSON/CSV data as chunks and export to CSV/JSON files.
    # tweet_util.generalized_data_chunking_file_export_function(
    #     "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json",
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/dataset-chunks/", "csv")

    # TODO - fix issues with extraction for CSV files.
    # tweet_util.generalized_two_layer_nested_multi_field_extraction_function(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/tweet-object-entities-attribute.csv",
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/", "entities",
    #     ["urls", "hashtags", "user_mentions", "symbols"], "csv")

    ###############################################################################################

    tweet_fields = ['tweet_created_at', 'tweet_id', 'tweet_full_text', 'tweet_in_reply_to_status_id',
                    'tweet_in_reply_to_user_id',
                    'tweet_in_reply_to_screen_name', 'tweet_retweet_count', 'tweet_favorite_count', 'tweet_lang']

    user_fields = ['user_id', 'user_name', 'user_screen_name', 'user_location', 'user_description',
                   'user_followers_count', 'user_friends_count', 'user_listed_count', 'user_favourites_count',
                   'user_statuses_count',
                   'user_created_at',
                   'user_time_zone', 'user_lang', ]

    required_fields = ['retweeted_custom', 'hashtags_custom', 'company_custom', 'text_custom',
                       'tweet_url_link_custom'] + tweet_fields + user_fields

    # # Analyze full-text.
    # attribute_describe(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/selected-attributes.csv",
    #     required_fields, "csv")
    #
    # # Determine the number of NaN and non-NaN rows for a attribute in a dataset.
    # count_nan_non_nan(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/selected-attributes.csv",
    #     required_fields, "csv")

################################################################################################################
