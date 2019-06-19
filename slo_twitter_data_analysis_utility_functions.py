"""
Social License to Operate
Advisor: Professor VanderLinden
Name: Joseph Jinn
Date: 5-29-19

SLO Twitter Dataset Analysis Utility Functions

###########################################################
Notes:

These are imported into the "slo-twitter-data-analysis.py" file.

TODO - refactor and iterate upon codebase for style, readability, and efficiency.

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
from pandas.io.json import json_normalize

sns.set()
#############################################################

pd.options.display.max_rows = None
pd.options.display.max_columns = None
pd.options.display.width = None
pd.options.display.max_colwidth = 1000

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
"""
This section contains helper functions taken from "SLO analysis.ipynb" by Shuntaro Yada from CSIRO.
"""


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

def ts_plot(col, **kwargs):
    """
    Helper function to visualize the data.

    :param col: the columns of the graph.
    :param kwargs: variable number of arguments.
    :return: None.
    """
    ax = plt.gca()
    data = kwargs.pop('data')
    ts = pd.to_datetime(data[col]).value_counts().resample('1D').sum()
    ax.plot(ts)


################################################################################################################

def ts_plot_2(col, **kwargs):
    """
    Helper function to visualize the data.

    :param col: the columns of the graph.
    :param kwargs: variable number of arguments.
    :return: None.

    FIXME - not working as intended.
    """
    ax = plt.gca()
    data = kwargs.pop('data')
    ts_rt = pd.to_datetime(data.query("retweeted_custom == 'TRUE'")[col]).value_counts().resample('1D').sum()
    ts = pd.to_datetime(data.query("retweeted_custom == 'FALSE'")[col]).value_counts().resample('1D').sum()
    ax.plot(ts)
    ax.plot(ts_rt)


################################################################################################################

def relhist_proc(col, **kwargs):
    """
    Helper function to visualize the data.  Constructs a relative frequency histogram.

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


################################################################################################################

def char_len(tweets):
    """
    Determine the length of the Tweet text.

    :param tweets: the Tweet text.
    :return: the length of the Tweet.
    """
    return tweets.str.len()


################################################################################################################
################################################################################################################
"""
This section contains the utility functions we created.
"""


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

def generalized_multi_field_extraction_function(input_file_path, output_file_path, fields_to_extract, file_type):
    """
       This is a generalized function to extract multiple fields from the raw JSON Tweet file simultaneously.
       The data is read in by chunks to ensure they can fit in RAM.

       :param file_type: type of file to save as. ("json" or "csv")
       :param input_file_path: absolute file path of the input file to extract the field from.
       :param output_file_path: absolute file path of the output file to save the extracted field to.
       :param fields_to_extract: List of string names of the fields to extract.
       :return: None.

       FIXME - ensure the last Tweet is not truncated when producing the CSV file.
       TODO - ensure it works for CSV files.
       """
    start_time = time.time()

    # Define size of chunks to read in.
    chunksize = 100000

    if file_type == "csv":
        # Read in the CSV file.
        twitter_data = \
            pd.read_csv(f"{input_file_path}", sep=",",
                        chunksize=chunksize)
    elif file_type == "json":
        # Read in the JSON file.
        twitter_data = pd.read_json(f"{input_file_path}",
                                    orient='records',
                                    lines=True,
                                    chunksize=chunksize)
    else:
        print("Invalid file type - aborting operation")
        return

    # Create empty Pandas Dataframes.
    json_dataframe = pd.DataFrame()
    created_at_dataframe = pd.DataFrame()
    selected_field = pd.DataFrame()

    # Append each chunk of extracted fields to the dataframe.
    chunk_number = 0
    for data in twitter_data:
        json_dataframe = json_dataframe.append(data, ignore_index=True)

        # Append each attribute in the list to the dataframe.
        for field in fields_to_extract:
            if json_dataframe[field] is not None:
                selected_field[field] = json_dataframe[field]
            else:
                selected_field[field] = "NaN"
            created_at_dataframe = created_at_dataframe.append(selected_field)

        # Clear dataframe and increment counter.
        json_dataframe = pd.DataFrame()
        chunk_number += 1

    file_path = \
        f"{output_file_path}{fields_to_extract}-attribute.{file_type}"

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

    log.info(
        f"The time taken to extract the fields \"{fields_to_extract}\" from the JSON file is {time_elapsed} minutes")
    log.info(f"The number of chunks is {chunk_number} based on chunk size of {chunksize} ")
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
    TODO - ensure it works for CSV files.
    """
    start_time = time.time()

    # Define size of chunks to read in.
    chunksize = 100000

    if file_type == "csv":
        # Read in the CSV file.
        twitter_data = \
            pd.read_csv(f"{input_file_path}", sep=",",
                        chunksize=chunksize)
    elif file_type == "json":
        # Read in the JSON file.
        twitter_data = pd.read_json(f"{input_file_path}",
                                    orient='records',
                                    lines=True,
                                    chunksize=chunksize)
    else:
        print("Invalid file type - aborting operation")
        return

    # Create empty Pandas Dataframes.
    json_dataframe = pd.DataFrame()
    created_at_dataframe = pd.DataFrame()
    selected_field = pd.DataFrame()

    # Append each chunk of extracted fields to the dataframe.
    chunk_number = 0
    for data in twitter_data:
        json_dataframe = json_dataframe.append(data, ignore_index=True)
        if json_dataframe[field_to_extract] is not None:
            selected_field[field_to_extract] = json_dataframe[field_to_extract]
        else:
            selected_field[field_to_extract] = "NaN"
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

def generalized_data_chunking_file_export_function(input_file_path, output_file_path, file_type):
    """
    This function reads in raw JSON or CSV files as chunks and exports each individual chunk to a CSV or JSON file.
    Please use absolute file path strings.
    Please use "csv" or "json" for the file type to save as and import as.

    :param file_type: type of file to save as or import as.
    :param input_file_path: absolute file path of the input file.
    :param output_file_path: absolute file path of the output file.

    :return: None.
    """
    start_time = time.time()

    # Define size of chunks to read in.
    chunksize = 100000

    if file_type == "csv":
        # Read in the CSV file.
        twitter_data = \
            pd.read_csv(f"{input_file_path}", sep=",",
                        chunksize=chunksize)
    elif file_type == "json":
        # Read in the JSON file.
        twitter_data = pd.read_json(f"{input_file_path}",
                                    orient='records',
                                    lines=True,
                                    chunksize=chunksize)
    else:
        print("Invalid file type - aborting operation")
        return

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

def import_dataset(input_file_path, file_type):
    """
    This function imports a JSON or CSV dataset and puts it into a Pandas Dataframe while providing basic information
    on the contents of the data in the frame.

    Note: Does NOT import in chunks.  Assumes file will fit in system RAM.

    :return: the Pandas Dataframe containing the dataset.
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

        # Reindex and shuffle the data randomly.
    tweet_dataset_processed = tweet_dataset.reindex(
        pd.np.random.permutation(tweet_dataset.index))

    # Generate a Pandas dataframe.
    dataframe = pd.DataFrame(tweet_dataset_processed)

    # Print shape and column names.
    log.info(f"\nThe shape of our dataframe storing the contents of the {file_type} Tweet data is:\n")
    log.info(dataframe.shape)
    log.info(f"\nThe columns of our dataframe storing the contents of the {file_type} Tweet data is:\n")
    log.info(dataframe.columns)
    log.info(f"\nA sample from the dataframe storing the contents of the {file_type} Tweet data is:\n")
    with pd.option_context('display.max_rows', None, 'display.max_columns',
                           None, 'display.width', None, 'display.max_colwidth', 1000):
        log.info(f"\n{dataframe.sample(1, axis=0)}\n")

    return dataframe


################################################################################################################

def generalized_two_layer_nested_multi_field_extraction_function(input_file_path, output_file_path,
                                                                 top_level_field, nested_fields_to_extract, file_type):
    """
       This is a generalized function to extract multiple nested fields from the raw JSON Tweet file simultaneously.
       The data is read in by chunks to ensure they can fit in RAM.

       Note: Function assumes structure of a "top-level-field" that is a key with a dictionary of nested attributes as
       its value.  IF more than two layers of nesting, rerun function again specifying new "top-level-field" and list
       of nested attributes to extract.

       :param file_type: type of file to save as. ("json" or "csv")
       :param input_file_path: absolute file path of the input file to extract the field from.
       :param output_file_path: absolute file path of the output file to save the extracted field to.
       :param top_level_field: attribute name for top-most layer of nesting.
       :param nested_fields_to_extract: List of string names of the fields to extract in the nested layer.
       :return: None.

       TODO - find a faster and more efficient way to perform this function.
       FIXME - not working for CSV files.
       """
    start_time = time.time()

    # Define size of chunks to read in.
    chunksize = 100000

    if file_type == "csv":
        # Read in the CSV file.
        twitter_data = \
            pd.read_csv(f"{input_file_path}", sep=",",
                        chunksize=chunksize)
    elif file_type == "json":
        # Read in the JSON file.
        twitter_data = pd.read_json(f"{input_file_path}",
                                    orient='records',
                                    lines=True,
                                    chunksize=chunksize)
    else:
        print("Invalid file type - aborting operation")
        return

    # Create empty Pandas Dataframes.
    json_dataframe = pd.DataFrame()
    created_at_dataframe = pd.DataFrame()
    selected_field = pd.DataFrame()

    # Loop through each chunk of data from the JSON file.
    chunk_number = 0
    # TODO - emulate Professor Vanderlinden's code for the outer loop.
    for data in twitter_data:
        json_dataframe = json_dataframe.append(data, ignore_index=True)

        # Loop through each row in the dataframe that contains a top-level field and nested dictionary of fields.
        for element in json_dataframe[top_level_field]:
            # print(element)
            # TODO - use integer index values for keys (TypeError: string indices must be integers)
            # Append each nested attribute in specified List to the dataframe as a column in a row in new dataframe.
            for field in nested_fields_to_extract:
                # print(element[field])
                if element[field] is not None:
                    selected_field[field] = pd.Series(element[field])
                else:
                    selected_field[field] = "NaN"
            # print(selected_field.shape)
            # print(selected_field.sample)
            created_at_dataframe = created_at_dataframe.append(selected_field, ignore_index=True)

        # TODO - use apply instead of for loop, if possible.
        # json_dataframe[top_level_field].apply()

        # Clear dataframe and increment counter.
        json_dataframe = pd.DataFrame()
        chunk_number += 1

        # One chunk only for debug purposes.
        break

    file_path = \
        f"{output_file_path}\'{top_level_field}\'-top-level-attribute-" \
            f"{nested_fields_to_extract}-nested-attribute(s).{file_type}"

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

    log.info(
        f"The time taken to extract the fields \"{nested_fields_to_extract}\" "
        f"from the JSON file is {time_elapsed} minutes")
    log.info(f"The number of chunks is {chunk_number} based on chunk size of {chunksize} ")
    log.info('\n')

################################################################################################################


################################################################################################################

# Extract list of specified attributes from nested JSON dictionary structure. (debug test purposes)
# generalized_two_layer_nested_multi_field_extraction_function(
#     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/user-attribute.json",
#     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/",
#     "user", ["id", "name", "screen_name", "description"], "json")

################################################################################################################
