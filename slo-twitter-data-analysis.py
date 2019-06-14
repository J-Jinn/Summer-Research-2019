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

def call_data_analysis_function_on_json_file_chunks(input_file_path, function_name):
    """
    This function reads the raw JSON Tweet dataset in chunk-by-chunk and calls the user-defined data analysis
    function that is specified as a parameter.

    :param input_file_path: absolute file path of the input raw JSON file.
    :param function_name: name of the data analysis function to call.
    :return: None.
    """
    start_time = time.time()

    # Define size of chunks to read in.
    chunksize = 100000

    # Read in the JSON file.
    twitter_data = pd.read_json(f"{input_file_path}",
                                orient='records',
                                lines=True,
                                chunksize=chunksize)

    # Create a empty Pandas dataframe.
    json_dataframe = pd.DataFrame()

    counter = 0
    chunk_number = 0

    # Loop through chunk-by-chunk and call the data analysis function on each chunk.
    for data in twitter_data:
        json_dataframe = json_dataframe.append(data, ignore_index=True)

        counter += 1
        chunk_number += 1

        if chunk_number == 1 and function_name == "none":
            # Print shape and column names.
            log.info(
                f"\nThe shape of the dataframe storing the contents of the raw JSON Tweet file chunk "
                f"{chunk_number} is:\n")
            log.info(json_dataframe.shape)
            log.info(
                f"\nThe columns of the dataframe storing the contents of the raw JSON Tweet file chunk "
                f"{chunk_number} is:\n")
            log.info(json_dataframe.columns)
            log.info(
                f"\nA sample from the dataframe storing the contents of the raw JSON Tweet file chunk "
                f"{chunk_number} is:\n")
            with pd.option_context('display.max_rows', None, 'display.max_columns',
                                   None, 'display.width', None, 'display.max_colwidth', 1000):
                log.info(f"\n{json_dataframe.sample(1, axis=0)}")
            time.sleep(2)

        if function_name != "none":
            # Call the data analysis functions.
            function_name(json_dataframe, chunk_number)
        else:
            return
            # Clear the contents of the dataframe.
        json_dataframe = pd.DataFrame()

        # For debug purposes.
        # break

    end_time = time.time()
    time_elapsed = (end_time - start_time) / 60.0
    time.sleep(3)
    log.info(f"The time taken to read in the JSON file by Chunks is {time_elapsed} minutes")
    log.info(f"The number of chunks is {chunk_number} based on chunk size of {chunksize}")
    log.info('\n')


################################################################################################################

def generalized_field_extraction_function(input_file_path, output_file_path, field_to_extract, file_type):
    """
    This is a generalized function to extract a single field from the raw JSON Tweet file.
    The data is read in by chunks to ensure they can fit in RAM.

    :param file_type: type of file to save as. ("json" or "csv")
    :param input_file_path: absolute file path of the input file to extract the field from.
    :param output_file_path: absolute file path of the output file to save the extracted field to.
    :param field_to_extract: string name of the field to extract.
    :return: None.
    """
    start_time = time.time()

    # Define size of chunks to read in.
    chunksize = 100000

    # Read in the JSON file.
    twitter_data = pd.read_json(f"{input_file_path}",
                                orient='records',
                                lines=True,
                                chunksize=chunksize)

    # Create empty Pandas Dataframes.
    json_dataframe = pd.DataFrame()
    created_at_dataframe = pd.DataFrame()
    selected_field = pd.DataFrame()

    # Append each chunk of extracted fields to the dataframe.
    chunk_number = 0
    for data in twitter_data:
        json_dataframe = json_dataframe.append(data, ignore_index=True)
        selected_field[field_to_extract] = json_dataframe[field_to_extract]
        created_at_dataframe = created_at_dataframe.append(selected_field)

        # Clear dataframe and increment counter.
        json_dataframe = pd.DataFrame()
        chunk_number += 1

    file_path = \
        f"{output_file_path}{field_to_extract}-attribute.{file_type}"

    if file_type == "csv":
        # Export to CSV file.
        created_at_dataframe.to_csv(file_path, sep=',',
                                    encoding='utf-8', index=False, header=True)
    elif file_type == "json":
        # Export JSON file.
        created_at_dataframe.to_json(file_path, orient='records', lines=True)
    else:
        print(f"Invalid file type entered - aborting operation")
        return

    end_time = time.time()
    time_elapsed = (end_time - start_time) / 60.0

    log.info(f"The time taken to extract the field \"{field_to_extract}\" from the JSON file is {time_elapsed} minutes")
    log.info(f"The number of chunks is {chunk_number} based on chunk size of {chunksize} ")
    log.info('\n')


################################################################################################################

def generalized_json_data_chunking_file_export_function(input_file_path, output_file_path, file_type):
    """
    This function reads in raw JSON files as chunks and exports each individual chunk to a CSV or JSON file.
    Please use absolute file path strings.
    Please use "csv" or "json" for the file type to save as.

    :param file_type: type of file to save as.
    :param input_file_path: absolute file path of the input file.
    :param output_file_path: absolute file path of the output file.

    :return: None.
    """
    start_time = time.time()

    # Define size of chunks to read in.
    chunksize = 100000

    # Read in the JSON file.
    twitter_data = pd.read_json(f"{input_file_path}",
                                orient='records',
                                lines=True,
                                chunksize=chunksize)

    # Create a empty Pandas dataframe.
    json_dataframe = pd.DataFrame()

    # Read in data by chunk and export to file.
    chunk_number = 0
    for data in twitter_data:
        json_dataframe = json_dataframe.append(data, ignore_index=True)
        chunk_number += 1

        # Note: Absolute file paths are required.  Relative do not work.
        csv_output_file_path = f"{output_file_path}raw-twitter-dataset-chunk-{chunk_number}.csv"
        json_output_file_path = f"{output_file_path}raw-twitter-dataset-chunk-{chunk_number}.json"

        if file_type == "csv":
            # Export to CSV file.
            json_dataframe.to_csv(csv_output_file_path, sep=',',
                                  encoding='utf-8', index=False, header=True)
        elif file_type == "json":
            # Export JSON file.
            json_dataframe.to_json(json_output_file_path, orient='records', lines=True)
        else:
            print(f"Invalid file type entered - aborting operation")
            return

        # Clear the contents of the dataframe.
        json_dataframe = pd.DataFrame()

    end_time = time.time()
    time_elapsed = (end_time - start_time) / 60.0

    log.info(f"The time taken to read in the JSON file by Chunks is {time_elapsed} minutes")
    log.info(f"The number of chunks is {chunk_number} based on chunk size of {chunksize}")
    log.info('\n')


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

def csv_retweeted():
    """
    Re-tweet statistics and visualizations for the CSV Twitter preprocessed dataset.

    Note: The raw JSON file does not have associated "company" information.

    :return: None.
    """

    print("Re-Tweet Statistics for entire CSV dataset:")
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

# Read in the CSV file.
tweet_dataset_processed = \
    pd.read_csv("D:/Dropbox/summer-research-2019/datasets/dataset_20100101-20180510.csv", sep=",")

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
with pd.option_context('display.max_rows', None, 'display.max_columns',
                       None, 'display.width', None, 'display.max_colwidth', 1000):
    log.info(f"\n{csv_dataframe.sample(1, axis=0)}")
log.info("\n")

################################################################################################################

"""
Main function.  Execute the program.
"""
if __name__ == '__main__':
    # Specify and call data analysis functions on chunked raw JSON Tweet file.
    # call_data_analysis_function_on_json_file_chunks(
    #     "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json", json_retweeted)
    # call_data_analysis_function_on_json_file_chunks(
    #     "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json", json_favorited)
    call_data_analysis_function_on_json_file_chunks(
        "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json", "none")

    # Extract the "created_at" field from raw JSON file and export to CSV file.
    # generalized_field_extraction_function(
    #     "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json",
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/",
    #     "user", "csv")

    # Read in JSON raw data as chunks and export to CSV/JSON files.
    # generalized_json_data_chunking_file_export_function(
    #     "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json",
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/dataset-chunks/", "csv")

    # Display Tweet count by time-date time series statistics.
    # tweet_count_by_timedate_time_series(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/created_at-attribute.csv",
    #     "csv")

################################################################################################################
