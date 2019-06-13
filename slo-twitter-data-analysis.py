"""
Social License to Operate
Advisor: Professor VanderLinden
Name: Joseph Jinn
Date: 5-29-19

SLO Twitter Dataset Analysis

###########################################################
Notes:

Json file sample:

{"in_reply_to_status_id_str":"305159434462691328",

"in_reply_to_status_id":305159434462691328,

"coordinates":null,

"created_at":"Sat Feb 23 03:40:21 +0000 2013",

"truncated":false,

"in_reply_to_user_id_str":"2768501",

"source":"<a href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\">Twitter for iPhone<\/a>",

"retweet_count":0,

"retweeted":false,

"geo":null,

"in_reply_to_screen_name":"abcnews",

"is_quote_status":false,

***************************************

"entities":{

"urls":[],

"hashtags":[],

"user_mentions":[{"indices":[0,8],"screen_name":"abcnews","id_str":"2768501", "name":"ABC News","id":2768501}],

"symbols":[]},

***************************************

"full_text":"@abcnews About bloody time. Adani only wants FIFO Indian workers for his Bowen basin mines.",

"id_str":"305160140833816576",

"in_reply_to_user_id":2768501,

"display_text_range":[0,91],

"favorite_count":0,

"id":305160140833816576,

"place":null,

"contributors":null,

"lang":"en",

***************************************

"user":{

"utc_offset":36000,

"friends_count":1385,

"profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/698290934618787840\/SIpBKnWE_normal.jpg",

"listed_count":3,

"profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","default_profile_image":false,

"favourites_count":533,

"description":"Train Driver extraordinaire, proud Union Leftie and Labor supporter.

Cant stand the LNP and their regressive ideas. Mainly political but I do enjoy a laugh.",

"created_at":"Tue Aug 21 23:23:52 +0000 2012",

"is_translator":false,

"profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",

"protected":false,

"screen_name":"DazzDicko",

"id_str":"772466924",

"profile_link_color":"1DA1F2",

"is_translation_enabled":false,

"translator_type":"none",

"id":772466924,

"geo_enabled":true,

"profile_background_color":"C0DEED",

"lang":"en",

"has_extended_profile":false,

"profile_sidebar_border_color":"C0DEED",

"profile_text_color":"333333",

"verified":false,

"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/698290934618787840\/SIpBKnWE_normal.jpg",

"time_zone":"Australia\/Brisbane",

"url":null,"contributors_enabled":false,

"profile_background_tile":false,

********************

"entities":{"description":{"urls":[]}},

********************

"statuses_count":5176,

"follow_request_sent":false,

"followers_count":945,

"profile_use_background_image":true,

"default_profile":true,

"following":false,

"name":"Daryl Dickson",

"location":"Far North Queensland",

"profile_sidebar_fill_color":"DDEEF6",

"notifications":false},

***************************************

"favorited":false}

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

sns.set()
#############################################################

pd.options.display.max_rows = 10
# pd.options.display.float_format = '{:.1f}'.format
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

def bar_plot(col, **kwargs):
    """
    Helper function to visualize the data.

    :param col: the columns of the graph.
    :param kwargs: variable number of arguments.
    :return: None.
    """
    ax = plt.gca()
    data = kwargs.pop('data')
    height = data[col].value_counts(normalize=True)
    height.sort_index(inplace=True)
    ax.bar(height.index, height)


################################################################################################################


def bar_plot_zipf(col, **kwargs):
    """
    Helper function to visualize the data.

    Based on Zipf's Law. (https://en.wikipedia.org/wiki/Zipf%27s_law)

    :param col: the columns of the graph.
    :param kwargs: variable number of arguments.
    :return: None.
    """
    ax = plt.gca()
    data = kwargs.pop('data')
    height = data[col].value_counts().value_counts(normalize=True)
    ax.bar(height.index, height)


################################################################################################################

def time_series(json_dataframe, chunk):
    """
    Visualize the Tweet creation time based on time-date information in the raw JSON Tweet file.

    Note: The processed CSV dataset file does not contain this information.

    :param json_dataframe: the dataframe containing the JSON data chunk.
    :param chunk: the dataframe JSON data chunk number.
    :return: None.
    """
    plt.figure()
    plt.title(f"Tweet Creation TimeDate Count for Chunk: {chunk}")
    plt.xlabel("Year and Month")
    plt.ylabel("Tweet Count")
    pd.to_datetime(json_dataframe['created_at']).value_counts().resample('1D').sum().plot()
    plt.show()


################################################################################################################

def json_retweeted(json_dataframe, chunk):
    """
    Re-tweet statistics and visualizations for the raw JSON file chunks.

    :param json_dataframe: the dataframe containing the JSON data chunk.
    :param chunk: the dataframe JSON data chunk number.
    :return: None.
    """
    print(f"Re-Tweet Statistics for raw JSON file data chunk {chunk}:")
    print(json_dataframe['retweeted'].value_counts())
    print()


################################################################################################################

def csv_retweeted():
    """
    Re-tweet statistics and visualizations for the CSV Twitter preprocessed dataset.

    Note: The raw JSON file does not have associated "company" information.

    :return: None.
    """

    print("Re-Tweet Statistics for CSV dataset:")
    print(csv_dataframe['retweeted'].value_counts())
    print()

    print("Re-Tweet Statistics for CSV dataset by Company:")
    print("Number of Tweets that are or aren't re-tweets by associated company: ")
    print(csv_dataframe.groupby(['company', 'retweeted']).size())
    print()

    # Graph the Re-Tweet Statistics.
    print("Proportion of Re-Tweets versus non Re-Tweets by associated company: ")
    plt.figure()
    grid = sns.FacetGrid(csv_dataframe[['retweeted', 'company']], col='company', col_wrap=6,
                         ylim=(0, 1))
    grid.map_dataframe(bar_plot, 'retweeted').set_titles('{col_name}')
    plt.show()


# Call the function.
# csv_retweeted()


################################################################################################################

def most_tweets_by_users():
    """
    User related statistics and visualizations.

    Note: The raw JSON file does not have associated "company" information.

    :return: None.
    """

    # Graph the User Statistics.
    print("Proportion of most Tweets for unique users by associated company: ")
    plt.figure()
    grid = sns.FacetGrid(csv_dataframe[['user_screen_name', 'company']], col='company', col_wrap=6,
                         ylim=(0, 1),
                         xlim=(0, 10))
    grid.map_dataframe(bar_plot_zipf, 'user_screen_name').set_titles('{col_name}').set_xlabels('appearance count')
    plt.show()

    # Adjusted parameters to allow statistics for all companies to show in output.
    pd.set_option("display.precision", 12)
    pd.options.display.max_rows = 100

    print("User Statistics for CSV dataset by Company: ")
    print("Top Tweet counts for unique user by associated company.")
    print(
        csv_dataframe[['company', 'user_screen_name']].groupby('company')
            .apply(lambda x: x['user_screen_name'].value_counts(normalize=True).head())
        # .value_counts(normalize=True)\
        # .sort_index(ascending=False).head())
    )
    print()


# Call the function.
# most_tweets_by_users()


################################################################################################################

def character_counts():
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
        # relative frequency histgram
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
    grid = sns.FacetGrid(csv_dataframe[['text', 'company']], col='company', col_wrap=6, ylim=(0, 1))
    grid.map_dataframe(relhist_proc, 'text', bins=10, proc=char_len).set_titles('{col_name}')
    plt.show()


# Call the function.
# character_counts()


################################################################################################################

def hashtags():
    """
    Hashtag related statistics.

    Note to self: reference "dataset_processor.py" for how to extract from nested "entities" structure.
    Currently non-functional.

    :return: None.
    """

    # Count the # of hashtags for each Tweet.
    # FIXME - not working at the moment.
    # csv_dataframe['#hashtags'] = csv_dataframe['hashtags'].apply(
    #     lambda x: len(x) if x is not None else 0)
    # # companies = df['company']
    #
    # print("Hashtag Statistics for CSV dataset by Company: ")
    # plt.figure()
    # grid = sns.FacetGrid(csv_dataframe[['#hashtags', 'company']], col='company', col_wrap=6, ylim=(0, 1),
    #                      xlim=(-1, 10))
    # grid.map_dataframe(bar_plot, '#hashtags').set_titles('{col_name}')
    # plt.show()

    # print("Hashtag Statistics for CSV dataset by Company: ")
    # print("The top hashtags for each associated company: ")
    # csv_dataframe[['company', 'hashtags']].groupby('company') \
    #     .apply(lambda x: pd.Series([hashtag
    #                                 for hashtags in x['hashtags'] if hashtags is not None
    #                                 for hashtag in hashtags])
    #            .value_counts(normalize=True)
    #            .head())


################################################################################################################

def emojis():
    """
    TODO - implement.

    :return: None.
    """
    print()


################################################################################################################

def call_data_analysis_function_on_json_file_chunks(function_name, enable_info):
    """
    This function reads the raw JSON Tweet dataset in chunk-by-chunk and calls the user-defined data analysis
    function that is specified as a parameter.

    :param function_name: name of the data analysis function to call.
    :param enable_info: enable or disable dataframe information output.

    :return: None.
    """
    # Define size of chunks to read in.
    chunksize = 100000

    # Read in the JSON file.
    twitter_data = pd.read_json("json/dataset_slo_20100101-20180510.json",
                                orient='records',
                                lines=True,
                                chunksize=chunksize)

    # twitter_data = pd.read_json("D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json",
    #                             orient='records',
    #                             lines=True,
    #                             chunksize=chunksize)

    # Create a empty Pandas dataframe.
    json_dataframe = pd.DataFrame()

    start_time = time.time()
    counter = 0
    chunk_number = 0

    for data in twitter_data:
        json_dataframe = json_dataframe.append(data, ignore_index=True)

        counter += 1
        chunk_number += 1

        # Note: Absolute file paths are required.  Relative do not work.
        csv_output_file_path = "D:/Dropbox/summer-research-2019/jupyter-notebooks/dataset-chunks/" \
                               "raw-twitter-dataset-chunk-" + str(chunk_number) + ".csv"
        json_output_file_path = "D:/Dropbox/summer-research-2019/jupyter-notebooks/dataset-chunks/" \
                                "raw-twitter-dataset-chunk-" + str(chunk_number) + ".json"

        if enable_info:
            # Print shape and column names.
            log.info("\n")
            log.info(
                f"The shape of the dataframe storing the contents of the raw JSON Tweet file chunk {chunk_number} is:")
            log.info(json_dataframe.shape)
            log.info("\n")
            log.info(
                f"The columns of the dataframe storing the contents of the raw JSON Tweet file chunk {chunk_number} is:")
            log.info(json_dataframe.columns)
            log.info("\n")
            log.info(
                f"A sample from the dataframe storing the contents of the raw JSON Tweet file chunk {chunk_number} is:")
            log.info(json_dataframe.sample(1))
            log.info("\n")

        # Limit # of chunks so we don't run out of RAM.
        if counter >= 1:
            # Export to CSV file.
            # json_dataframe.to_csv(str(csv_output_file_path), sep=',',
            #                       encoding='utf-8', index=False, header=True)
            # Export JSON file.
            # json_dataframe.to_json(str(json_output_file_path), orient='records', lines=True)

            if function_name != "None":
                # Call the data analysis functions.
                function_name(json_dataframe, chunk_number)
            # Clear the contents of the dataframe.
            json_dataframe = pd.DataFrame()
            # Reset the counter.
            counter = 0

            # For debug purposes.
            # break

    end_time = time.time()
    time_elapsed = (end_time - start_time) / 60.0

    log.info("The time taken to read in the JSON file by Chunks is: " + str(time_elapsed) + " minutes")
    log.info("The number of chunks is: " + str(chunk_number) + " based on chunk size of: " + str(chunksize))
    log.info('\n')


################################################################################################################

# Read in the CSV file.
tweet_dataset_processed = \
    pd.read_csv("datasets/dataset_20100101-20180510.csv", sep=",")

# tweet_dataset_processed = \
#     pd.read_csv("D:/Dropbox/summer-research-2019/datasets/dataset_20100101-20180510.csv", sep=",")

# Reindex and shuffle the data randomly.
tweet_dataset_processed = tweet_dataset_processed.reindex(
    pd.np.random.permutation(tweet_dataset_processed.index))

# Generate a Pandas dataframe.
csv_dataframe = pd.DataFrame(tweet_dataset_processed)

# Print shape and column names.
log.info("\n")
log.info("The shape of our dataframe storing the contents of the preprocessed CSV Tweet file is:")
log.info(csv_dataframe.shape)
log.info("\n")
log.info("The columns of our dataframe storing the contents of the preprocessed CSV Tweet file is:")
log.info(csv_dataframe.columns)
log.info("\n")
log.info("A sample from the dataframe storing the contents of the preprocessed CSV Tweet file is:")
log.info(csv_dataframe.sample(10))
log.info("\n")

################################################################################################################

"""
Main function.  Execute the program.
"""
if __name__ == '__main__':
    # Specify and call data analysis functions on chunked raw JSON Tweet file.
    call_data_analysis_function_on_json_file_chunks(time_series, False)
    call_data_analysis_function_on_json_file_chunks(json_retweeted, False)

    # Use this call to just print raw JSON file data chunk information.
    call_data_analysis_function_on_json_file_chunks("None", True)

################################################################################################################
