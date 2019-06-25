"""
Social License to Operate
Advisor: Professor VanderLinden
Name: Joseph Jinn
Date: 5-29-19
Version: 1.0

SLO Twitter Dataset Analysis

###########################################################
Notes:

Perpetual work-in-progress.

TODO - use Pandas to drop row 102 and save out as a new CSV file.
TODO - create a new CSV dataset file after getting "polyglot" functional on Unix/Linux Lab Machines.

Do not "save as" in Microsoft Excel as a utf-8 or any type of encoded CSV comma, delimited file.  Pandas will not be
able to read it back in as a utf-8 encoded file and this may result in character decryption issues.  If needs to modify
the dataset, use Pandas and Python code to do so, then export to a new CSV file.  Do NOT use Microsoft Excel to avoid
potential contamination/corruption of the data.

TODO - IMPORTANT NOTE: Ensure we delete any test file BEFORE creating the new dataset file!!!!!!!!!!!!!!!!!!!!!!!

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
import pandas as pd
import seaborn as sns

# Import custom utility functions.
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
# Matplotlib log settings.
mylog = log.getLogger("matplotlib")
mylog.setLevel(log.INFO)

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
    # single_company_only_df_2 = tweet_dataframe.loc[tweet_dataframe['company_derived_designation'] != "multiple"]

    # Number of rows associated with only one company.
    number_rows_one_company = single_company_only_df.shape[0]

    print(f"The # of Tweets associated with multiple companies is {number_rows_total - number_rows_one_company}")
    print(f"The # of Tweets associated with one company is {number_rows_one_company}")


################################################################################################################

def tweet_count_by_timedate_time_series(tweet_dataframe):
    """
    Function computes time series statistics and visualizations on Tweet Creation Time-Date Stamp.

    :param tweet_dataframe: the Twitter dataset in a Pandas dataframe.
    :return: None.
    """
    start_time = time.time()

    # Select only rows with one associated company. (don't graph company combos)
    # single_company_only_df = tweet_dataframe.loc[tweet_dataframe['multiple_companies_derived_count'] == 1]

    # 1st Plot.
    plt.figure(figsize=(18.5, 10.5), dpi=300)
    plt.title(f"Tweet Creation Time-Date Count")
    plt.xlabel("Tweet Creation Date")
    plt.ylabel("Tweet Count")
    pd.to_datetime(tweet_dataframe['tweet_created_at']).value_counts().resample('1D').sum().plot()
    plt.show()

    # 2nd Plot.
    plt.figure()
    print("Tweet Creation Time-Date Count by Company Association")
    grid = sns.FacetGrid(tweet_dataframe[['tweet_created_at', 'company_derived_designation']],
                         row='company_derived_designation', size=2, aspect=10, sharey=False)
    grid.map_dataframe(tweet_util_v2.ts_plot, 'tweet_created_at')
    grid.set_titles('{row_name}')
    grid.set_xlabels("Tweet Creation Date")
    grid.set_ylabels("Tweet Count")
    plt.show()

    # # 3rd Plot.
    # # FIXME - not working as intended.
    # plt.figure()
    # print("Twweet Creation Time-Date Count by Company Association and Retweeted Status")
    # grid = sns.FacetGrid(tweet_dataframe[['retweeted_derived', 'tweet_created_at', 'company_derived_designation']],
    #                      row='company_derived_designation', size=2, aspect=10, sharey=False)
    # grid.map_dataframe(tweet_util_v2.ts_plot_2, 'tweet_created_at')
    # grid.set_titles('{row_name}')
    # grid.set_xlabels("Tweet Creation Date")
    # grid.set_ylabels("Tweet Count")
    # plt.show()

    end_time = time.time()
    time_elapsed_seconds = end_time - start_time
    time_elapsed_minutes = (end_time - start_time) / 60.0
    time_elapsed_hours = (end_time - start_time) / 60.0 / 60.0
    log.debug(f"The time taken to visualize the statistics is {time_elapsed_seconds} seconds, "
              f"{time_elapsed_minutes} minutes, {time_elapsed_hours} hours")


################################################################################################################

def retweet_statistics(tweet_dataframe):
    """
    Re-Tweet statistics and visualizations for Twitter Dataset.
    Uses the Pandas "value_counts()" function to display unique values for the attribute.
    Groups user-specified attribute by the company the Tweet is associated with.

    :param tweet_dataframe: the Twitter dataset in a Pandas dataframe.
    :return: None.
    """
    start_time = time.time()

    # Select only rows with one associated company. (don't graph company combos)
    # single_company_only_df = tweet_dataframe.loc[tweet_dataframe['multiple_companies_derived_count'] == 1]

    print(f"ReTweeted Statistics for entire Twitter dataset:")
    print(tweet_dataframe["retweeted_derived"].value_counts())
    print()

    print(f"ReTweeted Statistics for Tweets by Company for entire Twitter dataset:")
    print(tweet_dataframe.groupby(['company_derived_designation', "retweeted_derived"]).size())
    print()

    # Graph the Statistics.
    print(f"Percentage of All Tweets for a Company that Are or Aren't ReTweets: ")
    plt.figure()
    grid = sns.FacetGrid(tweet_dataframe[["retweeted_derived", 'company_derived_designation']],
                         col='company_derived_designation', col_wrap=6, ylim=(0, 1))
    grid.map_dataframe(tweet_util_v2.bar_plot, "retweeted_derived")
    grid.set_titles('{col_name}')
    grid.set_xlabels("ReTweet - 0.0 No, 1.0 Yes").set_ylabels("Percentage of All Tweets")
    plt.show()

    plt.figure()
    print(f"Percentage Composition of All Tweets for a Company for Most ReTweeted Tweets by their ReTweet Counts:")
    grid = sns.FacetGrid(tweet_dataframe[['tweet_id', 'company_derived_designation']],
                         col='company_derived_designation', col_wrap=6, ylim=(0, 1), xlim=(0, 10))
    grid.map_dataframe(tweet_util_v2.bar_plot_zipf, 'tweet_id')
    grid.set_titles('{col_name}')
    grid.set_xlabels('ReTweeted Count').set_ylabels("Percentage of All Tweets")
    plt.show()

    print(f"\nReTweet counts for the Top (most) Retweeted Tweets.\n")
    print(tweet_dataframe[['company_derived_designation', 'tweet_id']].groupby('company_derived_designation')
          .apply(lambda x: x['tweet_id'].value_counts().value_counts(normalize=False)
                 .sort_index(ascending=False).head(3)))

    print(f"\nWhat Percentage of All Tweets for Given Company does the Top (most) Retweeted Tweets Comprise?.\n")
    print(tweet_dataframe[['company_derived_designation', 'tweet_id']].groupby('company_derived_designation')
          .apply(lambda x: x['tweet_id'].value_counts(normalize=True).head(5)))

    end_time = time.time()
    time_elapsed_seconds = end_time - start_time
    time_elapsed_minutes = (end_time - start_time) / 60.0
    time_elapsed_hours = (end_time - start_time) / 60.0 / 60.0
    log.debug(f"The time taken to visualize the statistics is {time_elapsed_seconds} seconds, "
              f"{time_elapsed_minutes} minutes, {time_elapsed_hours} hours")


################################################################################################################

def retweet_statistics_2(tweet_dataframe):
    """
    Function provides additional ReTweet Statistics.
    TODO - graph retweet counts for all Tweets (distribution).
    TODO - graph rewteet versus non-retweet text length for all Tweets (distribution).

    Resources:

    https://stackoverflow.com/questions/19384532/get-statistics-for-each-group-such-as-count-mean-etc-using-pandas-groupby

    :param tweet_dataframe: the Twitter dataset in a Pandas dataframe.
    :return: None.
    """

    has_retweeted_text = tweet_dataframe.loc[tweet_dataframe["retweeted_status_full_text"].notnull()]
    print(f"# of re-tweets with included original text of the original re-tweeted Tweet is: {has_retweeted_text.shape}")

    print("Note: These values based on 'retweeted_derived' boolean attribute:")

    yes_reweeted = tweet_dataframe.loc[tweet_dataframe['retweeted_derived'] == True]
    print(f"The number of Re-Tweets in the dataset: {yes_reweeted.shape}")
    no_reweeted = tweet_dataframe.loc[tweet_dataframe['retweeted_derived'] == False]
    print(f"The number of Non Re-Tweets in the dataset: {no_reweeted.shape}")
    yes_df = pd.DataFrame(yes_reweeted).groupby("company_derived_designation")

    retweet_frequency = tweet_dataframe[["tweet_id", "tweet_retweet_count"]]
    print("Tweet ID's and ReTweet Count for the Original ReTweeted Tweet (Descending head):")
    print(retweet_frequency.sort_values(by=["tweet_retweet_count"], ascending=False).head(10))

    print("Retweet counts by company:")
    yes_by_company = \
        pd.DataFrame(yes_reweeted).groupby(["company_derived_designation"]).size().reset_index(name="counts")
    print(f"{yes_by_company}\n")
    print("Non Retweet counts by company:")
    no_by_company = \
        pd.DataFrame(no_reweeted).groupby(["company_derived_designation"]).size().reset_index(name="counts")
    print(f"{no_by_company}\n")


################################################################################################################

def user_screen_name_statistics(tweet_dataframe):
    """
    User screen-name by associated company related statistics and visualizations.

    :param tweet_dataframe: the Twitter dataset in a Pandas dataframe.
    :return: None.
    """
    start_time = time.time()

    # Select only rows with one associated company. (don't graph company combos)
    # single_company_only_df = tweet_dataframe.loc[tweet_dataframe['multiple_companies_derived_count'] == 1]

    print("User Statistics for Tweets by Associated Company: ")
    print("Unique Users with Most (highest) Tweet Counts by Associated Company.")
    print(tweet_dataframe[['company_derived_designation', 'user_screen_name']].groupby(
        'company_derived_designation').apply(lambda x: x['user_screen_name'].value_counts(normalize=False).head())
          # .value_counts(normalize=True)\
          # .sort_index(ascending=False).head())
          )

    # Graph the User Statistics.
    print("\nNumber of Times a Percentage of Users Appears as the Tweet Author for a Given Company: ")
    plt.figure()
    grid = sns.FacetGrid(tweet_dataframe[['user_screen_name', 'company_derived_designation']],
                         col='company_derived_designation', col_wrap=6, ylim=(0, 1), xlim=(0, 10))
    grid.map_dataframe(tweet_util_v2.bar_plot_zipf, 'user_screen_name')
    grid.set_titles('{col_name}')
    grid.set_xlabels('Tweet Author Appearance Count').set_ylabels("Percentage of all Users")
    plt.show()

    end_time = time.time()
    time_elapsed_seconds = end_time - start_time
    time_elapsed_minutes = (end_time - start_time) / 60.0
    time_elapsed_hours = (end_time - start_time) / 60.0 / 60.0
    log.debug(f"The time taken to visualize the statistics is {time_elapsed_seconds} seconds, "
              f"{time_elapsed_minutes} minutes, {time_elapsed_hours} hours")


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

def tweet_character_counts(tweet_dataframe):
    """
    Character count for Tweet text by associated company related statistics and visualizations.

    :param tweet_dataframe: the Twitter dataset in a Pandas dataframe.
    :return: None.
    """
    start_time = time.time()

    # Select only rows with one associated company. (don't graph company combos)
    # single_company_only_df = tweet_dataframe.loc[tweet_dataframe['multiple_companies_derived_count'] == 1]

    print("Character Count Statistics of Tweet Text by Associated Company: ")
    print("Character Count Relative Frequency Histogram: ")
    plt.figure()
    grid = sns.FacetGrid(tweet_dataframe[['text_derived', 'company_derived_designation']],
                         col='company_derived_designation', col_wrap=6, ylim=(0, 1))
    grid.map_dataframe(tweet_util_v2.relhist_proc, 'text_derived', bins=10, proc=tweet_util_v2.char_len)
    grid.set_titles('{col_name}')
    grid.set_xlabels("# of Characters").set_ylabels("Percentage of All Tweets")
    plt.show()

    print("Character Count Statistics of User Description Text by Associated Company: ")
    print("Character Count Relative Frequency Histogram: ")
    plt.figure()
    grid = sns.FacetGrid(tweet_dataframe[['user_description', 'company_derived_designation']],
                         col='company_derived_designation', col_wrap=6, ylim=(0, 1))
    grid.map_dataframe(tweet_util_v2.relhist_proc, 'user_description', bins=10, proc=tweet_util_v2.char_len)
    grid.set_titles('{col_name}')
    grid.set_xlabels("# of Characters").set_ylabels("Percentage of all Tweets")
    plt.show()

    character_length = 140
    print(f"The total number of Tweets in the dataset is: {tweet_dataframe.shape[0]}")

    long_tweets = tweet_dataframe.loc[tweet_dataframe["tweet_text_length_derived"] > character_length]
    print(f"The number of Tweets over {character_length} characters is {long_tweets.shape[0]}")

    long_description = tweet_dataframe.loc[tweet_dataframe["user_description_text_length"] > character_length]
    print(f"The number of user descriptions over {character_length} characters is {long_description.shape[0]}")

    end_time = time.time()
    time_elapsed_seconds = end_time - start_time
    time_elapsed_minutes = (end_time - start_time) / 60.0
    time_elapsed_hours = (end_time - start_time) / 60.0 / 60.0
    log.debug(f"The time taken to visualize the statistics is {time_elapsed_seconds} seconds, "
              f"{time_elapsed_minutes} minutes, {time_elapsed_hours} hours")


################################################################################################################

def hashtag_statistics(tweet_dataframe):
    """
    Hashtag related statistics and visualizations.

    :param tweet_dataframe: the Twitter dataset in a dataframe.
    :return: None.
    FIXME - graphs functional; text stats non-functional (TypeError: 'float' object is not iterable)
    """
    start_time = time.time()

    # Select only rows with one associated company. (don't graph company combos)
    # single_company_only_df = tweet_dataframe.loc[tweet_dataframe['multiple_companies_derived_count'] == 1]

    print(f"The Number of Hashtags within each Tweet:")
    tweet_dataframe['#hashtags'] = tweet_dataframe['tweet_entities_hashtags'].apply(
        lambda x: len(x) if x is not None and not isinstance(x, float) else 0)
    # companies = df['company']

    print("Hashtag Count for Tweets by Percentage of All Tweets Associated with a Given Company:")
    plt.figure()
    grid = sns.FacetGrid(
        tweet_dataframe[['#hashtags', 'company_derived_designation']], col='company_derived_designation', col_wrap=6,
        ylim=(0, 1), xlim=(-1, 10))
    grid.map_dataframe(tweet_util_v2.bar_plot, '#hashtags')
    grid.set_titles('{col_name}')
    grid.set_xlabels("# of Hashtags").set_ylabels("Percentage of All Tweets")
    plt.show()

    # print("Appearance Count of Most Popular Hashtags:")
    # tweet_dataframe[['company_derived_designation', 'tweet_entities_hashtags']] \
    #     .groupby('company_derived_designation') \
    #     .apply(lambda x: pd.Series([hashtag
    #                                 for hashtags in x['tweet_entities_hashtags'] if hashtags is not None
    #                                 for hashtag in hashtags])
    #            .value_counts(normalize=False).head())
    #
    # print("Appearance Count of Most Popular Hashtags (all characters to lower-case):")
    # tweet_dataframe[['company_derived_designation', 'tweet_entities_hashtags']] \
    #     .groupby('company_derived_designation') \
    #     .apply(lambda x: pd.Series([hashtag.lower()
    #                                 for hashtags in x['tweet_entities_hashtags'] if hashtags is not None
    #                                 for hashtag in hashtags])
    #            .value_counts(normalize=False).head())

    end_time = time.time()
    time_elapsed_seconds = end_time - start_time
    time_elapsed_minutes = (end_time - start_time) / 60.0
    time_elapsed_hours = (end_time - start_time) / 60.0 / 60.0
    log.debug(f"The time taken to visualize the statistics is {time_elapsed_seconds} seconds, "
              f"{time_elapsed_minutes} minutes, {time_elapsed_hours} hours")


################################################################################################################

def mentions_statistics(tweet_dataframe):
    """
    Mentions related statistics and visualizations.

    :param tweet_dataframe: the Twitter dataset in a dataframe.
    :return: None.
    """
    start_time = time.time()

    # Select only rows with one associated company. (don't graph company combos)
    # single_company_only_df = tweet_dataframe.loc[tweet_dataframe['multiple_companies_derived_count'] == 1]

    print("Percentage of Tweets with User Mentions:")
    print(f"(Number of Tweets with User Mentions divided by Number of Tweets in Dataset)")
    print(tweet_dataframe['tweet_entities_user_mentions_id'].count() / len(tweet_dataframe))

    print("Percentage of Tweets that are Replies to Other Tweets:")
    print(f"(Number of Tweets that are Replies to Another Tweet divided by Number of Tweets in Dataset)")
    print(tweet_dataframe['tweet_in_reply_to_status_id'].count() / len(tweet_dataframe))

    print(f"\nUser Mentions Count by Percentage of All Tweets for a Given Company:")
    tweet_dataframe['#mentions'] = tweet_dataframe['tweet_entities_user_mentions_id']. \
        apply(lambda x: len(x) if isinstance(x, list) else 0)

    plt.figure()
    grid = sns.FacetGrid(tweet_dataframe[['#mentions', 'company_derived_designation']],
                         col='company_derived_designation', col_wrap=6, ylim=(0, 1), xlim=(-1, 10))
    grid.map_dataframe(tweet_util_v2.bar_plot, '#mentions')
    grid.set_titles('{col_name}')
    grid.set_xlabels("Number of Mentions").set_ylabels("Percentage of All Tweets")
    plt.show()

    print(f"Top (Most) Mentions for a Company by User Mentions ID")
    print(f"Top (highest) Mentions Count for a Given Company by the ID of the User that has been Mentioned")
    print(
        tweet_dataframe[['company_derived_designation', 'tweet_entities_user_mentions_id']].groupby(
            'company_derived_designation').apply(
            lambda x: pd.Series([mention
                                 for mentions in x['tweet_entities_user_mentions_id'] if mentions is not None
                                 for mention in mentions]).value_counts(normalize=False).head()))

    end_time = time.time()
    time_elapsed_seconds = end_time - start_time
    time_elapsed_minutes = (end_time - start_time) / 60.0
    time_elapsed_hours = (end_time - start_time) / 60.0 / 60.0
    log.debug(f"The time taken to visualize the statistics is {time_elapsed_seconds} seconds, "
              f"{time_elapsed_minutes} minutes, {time_elapsed_hours} hours")


################################################################################################################

def attribute_describe(input_file_path, attribute_name_list, file_type):
    """
    Function utilizes Pandas "describe" function to return dataframe statistics.

    https://chrisalbon.com/python/data_wrangling/pandas_dataframe_descriptive_stats/

    Note: This function will not work for attributes whose values are "objects" themselves.
    (can only be numeric type or string)

    :param input_file_path: absolute file path of the dataset in CSV or JSON format.
    :param attribute_name_list:  list of names of the attributes we are analyzing.
    :param file_type: type of input file. (JSON or CSV)
    :return: None.
    """
    start_time = time.time()

    if file_type == "csv":
        twitter_data = pd.read_csv(f"{input_file_path}", sep=",", encoding="ISO-8859-1", dtype=object)
    elif file_type == "json":
        twitter_data = pd.read_json(f"{input_file_path}", orient='records', lines=True)
    else:
        print(f"Invalid file type entered - aborting operation")
        return

    # Create a empty Pandas dataframe.
    dataframe = pd.DataFrame(twitter_data)

    if len(attribute_name_list) > 0:
        for attribute_name in attribute_name_list:
            print(f"\nPandas describe() for \"{attribute_name}\":\n")
            print(dataframe[attribute_name].describe(include='all'))
    else:
        print(f"\nPandas describe() for the entire dataframe/dataset:\n")
        print(dataframe.describe(include='all'))

    end_time = time.time()
    time_elapsed_seconds = end_time - start_time
    time_elapsed_minutes = (end_time - start_time) / 60.0
    time_elapsed_hours = (end_time - start_time) / 60.0 / 60.0
    log.debug(f"The time taken to visualize the statistics is {time_elapsed_seconds} seconds, "
              f"{time_elapsed_minutes} minutes, {time_elapsed_hours} hours")


################################################################################################################

def count_nan_non_nan(input_file_path, attribute_name_list, file_type):
    """
    Function counts the number of NaN and non-Nan examples in a Pandas dataframe for the specified columns.

    :param input_file_path: absolute file path of the dataset in CSV or JSON format.
    :param attribute_name_list:  list of names of the attributes we are analyzing.
    :param file_type: type of input file. (JSON or CSV)
    :return: None.
    """
    start_time = time.time()

    if file_type == "csv":
        twitter_data = pd.read_csv(f"{input_file_path}", sep=",", encoding="ISO-8859-1", dtype=object)
    elif file_type == "json":
        twitter_data = pd.read_json(f"{input_file_path}", orient='records', lines=True)
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
    time_elapsed_seconds = end_time - start_time
    time_elapsed_minutes = (end_time - start_time) / 60.0
    time_elapsed_hours = (end_time - start_time) / 60.0 / 60.0
    log.debug(f"The time taken to visualize the statistics is {time_elapsed_seconds} seconds, "
              f"{time_elapsed_minutes} minutes, {time_elapsed_hours} hours")


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

    TODO - is this function even necessary/useful? Not tested yet.
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

"""
Main function.  Execute the program.
"""
if __name__ == '__main__':
    my_start_time = time.time()

    # # Example function call to import libraries and configure virtual environment for data analysis.
    # tweet_util_v2.import_and_config()

    # # Import CSV dataset and convert to dataframe.
    # tweet_csv_dataframe = tweet_util_v2.import_dataset(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/twitter-dataset-flatten-json-test.json",
    #     "json")

    # Import CSV dataset and convert to dataframe.
    tweet_csv_dataframe = tweet_util_v2.import_dataset(
        "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/"
        "twitter-dataset-6-22-19-fixed.csv",
        "csv", False)

    # # Drop the extra header.
    # tweet_csv_dataframe.drop(102, inplace=True)

    # # Save out to CSV file.
    # tweet_util_v2.export_to_csv_json(
    #     tweet_csv_dataframe, [],
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/"
    #     "twitter-dataset-6-22-19-extra-header-removed", "w", "csv")

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

    # # Determine if a Tweet is a ReTweet.
    # tweet_util_v2.indicate_is_retweet(tweet_csv_dataframe)

    ##############################################################

    # # Isolate multi-company associated Tweets for data analysis and export to new CSV file.
    # tweet_util_v2.export_multi_company_tweets(tweet_csv_dataframe)
    #
    # # Import CSV dataset and convert to dataframe.
    # multi_company_tweets_df = tweet_util_v2.import_dataset(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/multi-company-tweets-6-22-19.csv",
    #     "csv", False)
    #
    # # Analyze the multi-company associated Tweets.
    # attribute_describe("D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/"
    #                    "data-analysis-datasets/multi-company-tweets.csv",
    #                    [], "csv")

    ##############################################################################################

    # Find rows containing mixed data types.
    # tweet_util_v2.find_mixed_data_types_in_dataset_rows(tweet_csv_dataframe)

    # # Display Tweet count by time-date time series statistics.
    # tweet_count_by_timedate_time_series(tweet_csv_dataframe)
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
    # hashtag_statistics(tweet_csv_dataframe)
    #
    # # Mentions Statistics.
    # mentions_statistics(tweet_csv_dataframe)
    #
    # # Tweets associated with one or multiple companies.
    # tweets_number_associated_companies(tweet_csv_dataframe)

    # # Unique Tweet Author Statistics.
    # unique_authors_tweet_counts(tweet_csv_dataframe)

    # # More ReTweet statistics.
    # retweet_statistics_2(tweet_csv_dataframe)

    ##############################################################################################

    # # Read in JSON/CSV data as chunks and export to CSV/JSON files.
    # tweet_util_v2.generalized_data_chunking_file_export_function(
    #     "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json",
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/dataset-chunks/", "csv")

    # # Extract various nested attributes from a outer attribute in the raw JSON file and export to CSV or JSON file.
    # # We extract 13 different attributes (some nested).
    # tweet_util_v2.flatten_extract_nested_json_attributes(
    #     "D:/Dropbox/summer-research-2019/json/dataset_slo_20100101-20180510.json",
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/retweeted-nested-attributes.csv",
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

    # Original Tweet object attribute names present in raw JSON file.
    original_tweet_object_field_names = [
        'created_at', 'id', 'full_text', 'in_reply_to_status_id', 'in_reply_to_user_id',
        'in_reply_to_screen_name', 'retweet_count', 'favorite_count', 'lang']

    # Names to rename main Tweet object attributes.
    tweet_object_fields = [
        'tweet_created_at', 'tweet_id', 'tweet_full_text', 'tweet_in_reply_to_status_id',
        'tweet_in_reply_to_user_id', 'tweet_in_reply_to_screen_name', 'tweet_retweet_count',
        'tweet_favorite_count', 'tweet_lang']

    # Names to give "user" object attributes.
    user_object_fields = [
        'user_id', 'user_name', 'user_screen_name', 'user_location', 'user_description',
        'user_followers_count', 'user_friends_count', 'user_listed_count', 'user_favourites_count',
        'user_statuses_count', 'user_created_at', 'user_time_zone', 'user_lang']

    # Names to give "entities" object attributes.
    entities_object_fields = [
        "tweet_entities_expanded_urls", "tweet_entities_hashtags", "tweet_entities_user_mentions_id",
        "tweet_entities_user_mentions_name", "tweet_entities_user_mentions_screen_name",
        "tweet_entities_symbols"]

    # Names to give "retweeted_status" object attributes.
    retweeted_status_object_fields = [
        'retweeted_status_created_at', 'retweeted_status_id', 'retweeted_status_full_text',
        'retweeted_status_in_reply_to_status_id', 'retweeted_status_in_reply_to_user_id',
        'retweeted_status_in_reply_to_screen_name', 'retweeted_status_retweet_count',
        'retweeted_status_favorite_count', 'retweeted_status_lang',
        'retweeted_status_entities',
        'retweeted_status_user', 'retweeted_status_coordinates', 'retweeted_status_place']

    # Names to give "user" object attributes.
    retweeted_status_user_object_fields = [
        'retweeted_status_user_id', 'retweeted_status_user_name', 'retweeted_status_user_screen_name',
        'retweeted_status_user_location', 'retweeted_status_user_description', 'retweeted_status_user_followers_count',
        'retweeted_status_user_friends_count', 'retweeted_status_user_listed_count',
        'retweeted_status_user_favourites_count', 'retweeted_status_user_statuses_count',
        'retweeted_status_user_created_at', 'retweeted_status_user_time_zone', 'retweeted_status_user_lang']

    # Modify these to determine what to export to CSV.
    required_fields = ['retweeted_derived', 'company_derived', 'text_derived',  # "tweet_quoted_status_id",
                       'tweet_url_link_derived', 'multiple_companies_derived_count', "company_derived_designation",
                       'tweet_text_length_derived', "spaCy_language_detect", "user_description_text_length"] \
                      + tweet_object_fields + user_object_fields + entities_object_fields \
                      + retweeted_status_object_fields

    # # Analyze full-text.
    # attribute_describe(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/twitter-dataset-6-22-19-fixed.csv",
    #     required_fields, "csv")

    # # Determine the number of NaN and non-NaN rows for a attribute in a dataset.
    # count_nan_non_nan(
    #     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/twitter-dataset-6-22-19-fixed.csv",
    #     required_fields, "csv")

    ################################################################################################################

    my_end_time = time.time()

    time_elapsed_in_seconds = (my_end_time - my_start_time)
    time_elapsed_in_minutes = (my_end_time - my_start_time) / 60.0
    time_elapsed_in_hours = (my_end_time - my_start_time) / 60.0 / 60.0
    print(f"Time taken to process dataset: {time_elapsed_in_seconds} seconds, "
          f"{time_elapsed_in_minutes} minutes, {time_elapsed_in_hours} hours")

    ################################################################################################################