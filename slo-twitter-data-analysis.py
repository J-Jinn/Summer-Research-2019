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

sns.set()
pd.options.display.max_rows = 10
pd.set_option('precision', 7)
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)

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
    json_dataframe = pd.DataFrame(twitter_data)

    plt.figure()
    plt.title(f"Tweet Creation Time-Date Count by Year/Month/Day")
    plt.xlabel("Year/Month/Day")
    plt.ylabel("Tweet Count")
    pd.to_datetime(json_dataframe['created_at']).value_counts().resample('1D').sum().plot()
    plt.show()
    end_time = time.time()
    time_elapsed = (end_time - start_time) / 60.0
    log.debug(f"The time taken to visualize the statistics is {time_elapsed} minutes")


################################################################################################################


def json_retweeted(json_dataframe, chunk):
    """
    Re-tweet statistics and visualizations for the raw JSON Twitter data chunks.

    :param json_dataframe: the dataframe containing the JSON data chunk.
    :param chunk: the JSON data chunk number.
    :return: None.
    """
    print(f"Re-Tweet Statistics for raw JSON Twitter data chunk {chunk}:")
    print(json_dataframe['retweeted'].value_counts())
    print()


################################################################################################################

def json_favorited(json_dataframe, chunk):
    """
    Re-tweet statistics and visualizations for the raw JSON Twitter data chunks.

    :param json_dataframe: the dataframe containing the JSON data chunk.
    :param chunk: the JSON data chunk number.
    :return: None.
    """
    print(f"Re-Tweet Statistics for raw JSON Twitter data chunk {chunk}:")
    print(json_dataframe['favorited'].value_counts())
    print()


################################################################################################################

def csv_retweeted(tweet_csv_dataframe):
    """
    Re-tweet statistics and visualizations for the CSV Twitter preprocessed dataset.

    Note: The raw JSON file does not have associated "company" information.

    :return: None.
    """

    print("Re-Tweet Statistics for entire CSV dataset:")
    print(tweet_csv_dataframe['retweeted'].value_counts())
    print()

    print("Re-Tweet Statistics for CSV dataset by Company:")
    print("Number of Tweets that are or aren't re-tweets by associated company: ")
    print(tweet_csv_dataframe.groupby(['company', 'retweeted']).size())
    print()

    # Graph the Re-Tweet Statistics.
    print("Proportion of Re-Tweets versus non Re-Tweets by associated company: ")
    plt.figure()
    grid = sns.FacetGrid(tweet_csv_dataframe[['retweeted', 'company']], col='company', col_wrap=6,
                         ylim=(0, 1))
    grid.map_dataframe(tweet_util.bar_plot, 'retweeted').set_titles('{col_name}')
    plt.show()


################################################################################################################

def most_tweets_by_users_per_company(tweet_csv_dataframe):
    """
    User related statistics and visualizations.

    Note: The raw JSON file does not have associated "company" information.

    :return: None.
    """

    # Adjusted parameters to allow statistics for all companies to show in output.
    pd.set_option("display.precision", 12)
    pd.options.display.max_rows = 100

    print("User Statistics for CSV dataset by Company: ")
    print("Top Tweet counts for unique user by associated company.")
    print(
        tweet_csv_dataframe[['company', 'user_screen_name']].groupby('company')
            .apply(lambda x: x['user_screen_name'].value_counts(normalize=True).head())
        # .value_counts(normalize=True)\
        # .sort_index(ascending=False).head())
    )
    print()

    # Graph the User Statistics.
    print("Proportion of most Tweets for unique users by associated company: ")
    plt.figure()
    grid = sns.FacetGrid(tweet_csv_dataframe[['user_screen_name', 'company']], col='company', col_wrap=6,
                         ylim=(0, 1),
                         xlim=(0, 10))
    grid.map_dataframe(tweet_util.bar_plot_zipf, 'user_screen_name').set_titles('{col_name}').set_xlabels(
        'appearance count')
    plt.show()


################################################################################################################

def tweet_character_counts(tweet_csv_dataframe):
    """
    Character related statistics and visualizations.

    Note: The raw JSON file does not have associated "company" information.

    :return: None.
    """

    def relhist_proc(col, **kwargs):
        """
        Helper function to visualize the data.

        :param col: the columns of the graph.
        :param kwargs: variable number of arguments.
        :return: None.
        """
        ax = plt.gca()
        data = kwargs.pop('data')
        proc = kwargs.pop('proc')
        processed = proc(data[col])
        # relative frequency histogram
        # https://stackoverflow.com/questions/9767241/setting-a-relative-frequency-in-a-matplotlib-histogram
        ax.hist(processed, weights=np.ones_like(processed) / processed.size, **kwargs)

    def char_len(tweets):
        """
        Determine the length of the Tweet text.

        :param tweets: the Tweet text.
        :return: the length of the Tweet.
        """
        return tweets.str.len()

    print("Character Statistics for CSV dataset by Company: ")
    print("Character count relative frequency histogram: ")
    plt.figure()
    grid = sns.FacetGrid(tweet_csv_dataframe[['text', 'company']], col='company', col_wrap=6, ylim=(0, 1))
    grid.map_dataframe(relhist_proc, 'text', bins=10, proc=char_len).set_titles('{col_name}')
    plt.show()


################################################################################################################

"""
Main function.  Execute the program.
"""
if __name__ == '__main__':
    # Import dataset and convert to dataframe.
    tweet_preprocessed_csv_dataframe = tweet_util.import_dataset(
        "D:/Dropbox/summer-research-2019/datasets/dataset_20100101-20180510.csv", "csv")

    # # Specify and call data analysis functions on chunked raw JSON Tweet file.
    # tweet_util.call_data_analysis_function_on_json_file_chunks(
    #     "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json", json_retweeted)
    #
    # tweet_util.call_data_analysis_function_on_json_file_chunks(
    #     "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json", json_favorited)
    #
    # tweet_util.call_data_analysis_function_on_json_file_chunks(
    #     "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json", "none")

    # Extract the "created_at" field from raw JSON file and export to CSV file.
    tweet_util.generalized_field_extraction_function(
        "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json",
        "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/",
        "user", "csv")

    # Read in JSON raw data as chunks and export to CSV/JSON files.
    tweet_util.generalized_json_data_chunking_file_export_function(
        "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json",
        "D:/Dropbox/summer-research-2019/jupyter-notebooks/dataset-chunks/", "csv")

    # Display Tweet count by time-date time series statistics.
    # tweet_count_by_timedate_time_series(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/created_at-attribute.csv",
    #     "csv")

    # Determine whether Tweets have been re-Tweeted.
    # csv_retweeted(tweet_preprocessed_csv_dataframe)

    # Determine the Tweet count for most prolific user by company.
    # most_tweets_by_users_per_company(tweet_preprocessed_csv_dataframe)

    # Determine the # of characters in Tweets via relative frequency histogram.
    # tweet_character_counts(tweet_preprocessed_csv_dataframe)

################################################################################################################
