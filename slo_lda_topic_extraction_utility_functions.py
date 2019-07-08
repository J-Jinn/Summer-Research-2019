"""
SLO Topic Modeling
Advisor: Professor VanderLinden
Name: Joseph Jinn
Date: 6-5-19

SLO LDA Utility Functions.

###########################################################
Notes:

Adapted code from SLO TBL Topic Classification code-base for use in LDA Tweet pre-processing.

###########################################################
Resources Used:

https://github.com/Calvin-CS/slo-classifiers/blob/master/stance/data/tweet_preprocessor.py
https://github.com/Calvin-CS/slo-classifiers/blob/master/stance/data/dataset_processor.py
https://github.com/Calvin-CS/slo-classifiers/blob/topic/topic/final_derek/Preprocessing.py

"""

################################################################################################################
################################################################################################################

# Import libraries.
import logging as log
import re
import string
import warnings
import pandas as pd
# import tensorflow as tf
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

# Import custom utility functions.
import slo_twitter_data_analysis_utility_functions as tweet_util_v2

#############################################################

# Miscellaneous parameter adjustments for pandas and python.
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)

"""
Turn debug log statements for various sections of code on/off.
(adjust log level as necessary)
"""
log.basicConfig(level=log.INFO)


# tf.logging.set_verbosity("INFO")


################################################################################################################
################################################################################################################

def preprocess_tweet_text(tweet_text):
    """
    Helper function performs text pre-processing using regular expressions and other Python functions.

    Notes:
    TODO - shrink character elongations
    TODO - remove non-english tweets
    TODO - remove non-company associated tweets
    TODO - remove year and time.
    TODO - remove cash items?

    Resources Used:
    https://thispointer.com/python-how-to-convert-a-list-to-string/
    http://jonathansoma.com/lede/foundations/classes/pandas%20columns%20and%20functions/apply-a-function-to-every-row-in-a-pandas-dataframe/

    :return: the processed Tweet.
    """

    # Remove "RT" tags.
    preprocessed_tweet_text = re.sub("rt", "", tweet_text)

    # Remove URL's.
    preprocessed_tweet_text = re.sub("http[s]?://\S+", "slo_url", preprocessed_tweet_text)

    # Remove Tweet mentions.
    preprocessed_tweet_text = re.sub("@\S+", "slo_mention", preprocessed_tweet_text)

    # Remove Tweet hashtags.
    preprocessed_tweet_text = re.sub("#\S+", "slo_hashtag", preprocessed_tweet_text)

    # Remove all punctuation.
    preprocessed_tweet_text = preprocessed_tweet_text.translate(str.maketrans('', '', string.punctuation))

    # Remove irrelevant words from Tweets.
    delete_list = ["slo_url", "slo_mention", "word_n", "slo_year", "slo_cash", "woodside", "auspol", "adani",
                   "stopadani",
                   "ausbiz", "santos", "whitehaven", "tinto", "fortescue", "bhp", "adelaide", "billiton", "csg",
                   "nswpol",
                   "nsw", "lng", "don", "rio", "pilliga", "australia", "asx", "just", "today", "great", "says", "like",
                   "big", "better", "rite", "would", "SCREEN_NAME", "mining", "former", "qldpod", "qldpol", "qld", "wr",
                   "melbourne", "andrew", "fuck", "spadani", "greg", "th", "australians", "http", "https", "rt",
                   "goadani",
                   "co", "amp", "riotinto", "carmichael", "abbot", "bill shorten",
                   "slourl", "slomention", "slohashtag", "sloyear", "slocash"]

    # Convert series to string.
    tweet_string = str(preprocessed_tweet_text)

    # Split Tweet into individual words.
    words = tweet_string.split()

    # Check to see if a word is irrelevant or not.
    words_relevant = []
    for w in words:
        if w not in delete_list:
            words_relevant.append(w)
        else:
            log.debug("Irrelevant word found: ")
            log.debug(w)
            log.debug('\n')

    # Convert list back into original Tweet text minus irrelevant words.
    tweet_string = ' '.join(words_relevant)
    # Convert back to a series object.
    tweet_series = pd.Series(tweet_string)

    log.debug("Tweet text with irrelevant words removed: ")
    log.debug(tweet_series)
    log.debug('\n')

    return tweet_series


################################################################################################################

def tweet_dataset_preprocessor(input_file_path, output_file_path, column_name):
    """
     Function pre-processes specified dataset in preparation for LDA topic extraction.

    :param input_file_path: relative filepath from project root directory for location of dataset to process.
    :param output_file_path: relative filepath from project root directory for location to save .csv file.
    :param column_name: name of the column in the dataset that we are pre-processing.
    :return: Nothing. Saves to CSV file.
    """

    # Import the dataset.
    slo_dataset_cmu = \
        pd.read_csv(str(input_file_path), sep=",")

    # Shuffle the data randomly.
    slo_dataset_cmu = slo_dataset_cmu.reindex(
        pd.np.random.permutation(slo_dataset_cmu.index))

    # Generate a Pandas dataframe.
    slo_dataframe_cmu = pd.DataFrame(slo_dataset_cmu[str(column_name)])

    # Print shape and column names.
    log.info("\n")
    log.info("The shape of our raw SLO dataframe:")
    log.info(slo_dataframe_cmu.shape)
    log.info("\n")
    log.info("The columns of our raw SLO dataframe:")
    log.info(slo_dataframe_cmu.head)
    log.info("\n")

    #######################################################

    # Down-case all text.
    slo_dataframe_cmu[column_name] = slo_dataframe_cmu[column_name].str.lower()

    # Pre-process each tweet individually (calls a helper function).
    slo_dataframe_cmu[str(column_name)] = slo_dataframe_cmu[str(column_name)].apply(preprocess_tweet_text)

    # Reindex everything.
    slo_dataframe_cmu.index = pd.RangeIndex(len(slo_dataframe_cmu.index))
    # slo_dataframe_combined.index = range(len(slo_dataframe_combined.index))

    # Save to CSV file.
    slo_dataframe_cmu.to_csv(str(output_file_path), sep=',',
                             encoding='utf-8', index=False)

    print("Dataset preprocessing finished.")
    print("Saved to: " + output_file_path)


################################################################################################################

def display_topics(model, feature_names, num_top_words):
    """
    Helper function to display the top words for each topic in the LDA model.

    :param model: the LDA model
    :param feature_names: feature names from CountVectorizer.
    :param num_top_words: # of words to display for each topic.
    :return: None.
    """
    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d:" % (topic_idx))
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-num_top_words - 1:-1]]))


################################################################################################################

def latent_dirichlet_allocation_grid_search(dataframe, search_parameters):
    """
    Function performs exhaustive grid search for Scikit-Learn LDA model.

    :return: None.
    """
    from sklearn.decomposition import LatentDirichletAllocation
    from sklearn.model_selection import GridSearchCV

    # Construct the pipeline.
    latent_dirichlet_allocation_clf = Pipeline([
        ('vect', CountVectorizer()),
        ('clf', LatentDirichletAllocation()),
    ])

    # Perform the grid search.
    latent_dirichlet_allocation_clf = GridSearchCV(latent_dirichlet_allocation_clf, search_parameters, cv=5, iid=False
                                                   , n_jobs=-1)
    latent_dirichlet_allocation_clf.fit(dataframe)

    # View all the information stored in the model after training it.
    classifier_results = pd.DataFrame(latent_dirichlet_allocation_clf.cv_results_)
    log.debug("The shape of the Latent Dirichlet Allocation model's result data structure is:")
    log.debug(classifier_results.shape)
    log.debug(
        "The contents of the Latent Dirichlet Allocation model's result data structure is:")
    log.debug(classifier_results.head())

    # Display the optimal parameters.
    log.info("The optimal parameters found for the Latent Dirichlet Allocation is:")
    for param_name in sorted(search_parameters.keys()):
        log.info("%s: %r" % (param_name, latent_dirichlet_allocation_clf.best_params_[param_name]))
    log.info("\n")


################################################################################################################

def dataframe_subset(tweet_dataset, sample_size):
    """
    Function slices the Twitter dataset into a smaller dataset for the purposes of saving compute time on using
    exhaustive grid search to find initial optimal hyper parameters for LDA topic modeling and extraction.

    :param tweet_dataset: the dataset to generate a subset from.
    :param sample_size: size of the subset to construct.
    :return: feature set to use for GridSearchCV.
    """

    # Check that user passed in dataset from which we can generate a dataframe.
    try:
        tweet_dataframe_processed = pd.DataFrame(tweet_dataset)
    except Exception:
        print("Failed to generate Dataframe for subsetting operation:")
        return

    # Drop any NaN or empty Tweet rows in dataframe (or else CountVectorizer will blow up).
    tweet_dataframe_processed = tweet_dataframe_processed.dropna()

    # Reindex everything.
    tweet_dataframe_processed.index = pd.RangeIndex(len(tweet_dataframe_processed.index))

    # Subset of the dataframe.
    tweet_dataframe_processed.sample(n=sample_size)

    # Assign column names.
    tweet_dataframe_processed_column_names = ['Tweet']

    # Rename column in dataframe.
    tweet_dataframe_processed.columns = tweet_dataframe_processed_column_names

    # Create input feature.
    selected_features = tweet_dataframe_processed[tweet_dataframe_processed_column_names]
    processed_features = selected_features.copy()

    # Create feature set.
    slo_feature_set = processed_features['Tweet']

    return slo_feature_set


################################################################################################################

def topic_author_model(tweet_dataframe):
    """
    Function to combine all Tweets by the same author into one document (example) for topic extraction.

    :param tweet_dataframe: Pandas dataframe containing Twitter dataset.
    :return: None.
    """

    def combine_tweets(data):
        """
        Function to combine all Tweets by a common author into a single document(example)
        :param data:
        :return:
        """
        dataframe = pd.DataFrame(data)
        print(dataframe.shape)

    tweet_dataframe = pd.DataFrame(tweet_dataframe)

    df = tweet_dataframe[["user_id", "tweet_full_text"]].groupby("user_id").apply(combine_tweets)
    print(df.shape)


################################################################################################################

def test_function():
    print("This is a test function")


################################################################################################################

# # Import CSV dataset and convert to dataframe.
# tweet_csv_dataframe = tweet_util_v2.import_dataset(
#     "D:/Dropbox/summer-research-2019/jupyter-notebooks/attribute-datasets/"
#     "twitter-dataset-6-27-19.csv",
#     "csv", False)
#
# # Create author-topic model dataframe.
# topic_author_model(tweet_csv_dataframe)
