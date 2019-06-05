"""
SLO Topic Modeling
Advisor: Professor VanderLinden
Name: Joseph Jinn
Date: 5-29-19

LDA - Latent Dirichlet Allocation

###########################################################
Notes:

LDA can only use raw term counts (CANNOT use tfidf transformer)

###########################################################
Resources Used:

https://scikit-learn.org/stable/modules/decomposition.html#latentdirichletallocation

https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation

https://medium.com/mlreview/topic-modeling-with-scikit-learn-e80d33668730

"""

################################################################################################################
################################################################################################################

import logging as log
import re
import string
import warnings
import tensorflow as tf
import time
from tensorflow import keras
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.pipeline import Pipeline
from sklearn import metrics

#############################################################

# Note: Need to set level AND turn on debug variables in order to see all debug output.
log.basicConfig(level=log.DEBUG)
tf.logging.set_verbosity(tf.logging.ERROR)

# Miscellaneous parameter adjustments for pandas and python.
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)

"""
Turn debug log statements for various sections of code on/off.
"""
# Debug the GridSearch functions for each Classifier.
debug_pipeline = True
# Debug the initial dataset import and feature/target set creation.
debug_preprocess_tweets = True
# Debug create_training_and_test_set() function.
debug_train_test_set_creation = False

################################################################################################################
################################################################################################################

# Import the datasets.
tweet_dataset_processed1 = \
    pd.read_csv("datasets/tbl_kvlinden_LDA_PROCESSED.csv", sep=",")

tweet_dataset_processed2 = \
    pd.read_csv("datasets/tbl_training_set_LDA_PROCESSED.csv", sep=",")

tweet_dataset_processed3 = \
    pd.read_csv("datasets/dataset_20100101-20180510_tok_LDA_PROCESSED.csv", sep=",")

# Reindex and shuffle the data randomly.
tweet_dataset_processed1 = tweet_dataset_processed1.reindex(
    pd.np.random.permutation(tweet_dataset_processed1.index))

tweet_dataset_processed2 = tweet_dataset_processed2.reindex(
    pd.np.random.permutation(tweet_dataset_processed2.index))

tweet_dataset_processed3 = tweet_dataset_processed3.reindex(
    pd.np.random.permutation(tweet_dataset_processed3.index))

# Generate a Pandas dataframe.
tweet_dataframe_processed1 = pd.DataFrame(tweet_dataset_processed1)
tweet_dataframe_processed2 = pd.DataFrame(tweet_dataset_processed2)
tweet_dataframe_processed3 = pd.DataFrame(tweet_dataset_processed3)

if debug_preprocess_tweets:
    # Print shape and column names.
    log.info("\n")
    log.info("The shape of our SLO dataframe 1:")
    log.info(tweet_dataframe_processed1.shape)
    log.info("\n")
    log.info("The columns of our SLO dataframe 1:")
    log.info(tweet_dataframe_processed1.head)
    log.info("\n")
    # Print shape and column names.
    log.info("\n")
    log.info("The shape of our SLO dataframe 2:")
    log.info(tweet_dataframe_processed2.shape)
    log.info("\n")
    log.info("The columns of our SLO dataframe 2:")
    log.info(tweet_dataframe_processed2.head)
    log.info("\n")
    # Print shape and column names.
    log.info("\n")
    log.info("The shape of our SLO dataframe 3:")
    log.info(tweet_dataframe_processed3.shape)
    log.info("\n")
    log.info("The columns of our SLO dataframe 3:")
    log.info(tweet_dataframe_processed3.head)
    log.info("\n")

# Rename column in 3rd dataframe for concatenation purposes.
tweet_dataframe_processed3.columns = ['Tweet']

# Drop any NaN or empty Tweet rows in 3rd dataframe (or else CountVectorizer will blow up).
tweet_dataframe_processed3 = tweet_dataframe_processed3.dropna()

# Concatenate the individual datasets together.
frames = [tweet_dataframe_processed1, tweet_dataframe_processed2, tweet_dataframe_processed3]
slo_dataframe_combined = pd.concat(frames, ignore_index=True)

if debug_preprocess_tweets:
    # Print shape and column names.
    log.debug("\n")
    log.debug("The shape of our SLO dataframe combined:")
    log.debug(slo_dataframe_combined.shape)
    log.debug("\n")
    log.debug("The columns of our SLO dataframe combined:")
    log.debug(slo_dataframe_combined.head)
    log.debug("\n")

# Reindex everything.
slo_dataframe_combined.index = pd.RangeIndex(len(slo_dataframe_combined.index))
# slo_dataframe_combined.index = range(len(slo_dataframe_combined.index))

# Assign column names.
tweet_dataframe_processed_column_names = ['Tweet']

# Create input features.
selected_features = slo_dataframe_combined[tweet_dataframe_processed_column_names]
processed_features = selected_features.copy()

if debug_preprocess_tweets:
    # Check what we are using as inputs.
    log.debug("\n")
    log.debug("The Tweets in our input feature:")
    log.debug(processed_features['Tweet'])
    log.debug("\n")

# Create feature set.
slo_feature_set = processed_features['Tweet']


################################################################################################################

def latent_dirichlet_allocation_grid_search():
    """
    Function performs exhaustive grid search for LDA.

    :return: None.
    """
    from sklearn.decomposition import LatentDirichletAllocation

    # Construct the pipeline.
    latent_dirichlet_allocation_clf = Pipeline([
        ('vect', CountVectorizer(max_df=0.95, min_df=2, max_features=1000, stop_words='english')),
        ('clf', LatentDirichletAllocation()),
    ])

    from sklearn.model_selection import GridSearchCV

    # What parameters do we search for?
    parameters = {
        'vect__ngram_range': [(1, 1), (1, 2), (1, 3), (1, 4)],
        'clf__n_components': [1, 5, 10, 15],
        'clf__doc_topic_prior': [None],
        'clf__topic_word_prior': [None],
        'clf__learning_method': ['batch', 'online'],
        'clf__learning_decay': [0.5, 0.7, 0.9],
        'clf__learning_offset': [5, 10, 15],
        'clf__max_iter': [5, 10, 15],
        'clf__batch_size': [64, 128, 256],
        'clf__evaluate_every': [0],
        'clf__total_samples': [1e4, 1e6, 1e8],
        'clf__perp_tol': [1e-1, 1e-2, 1e-3],
        'clf__mean_change_tol': [1e-1, 1e-3, 1e-5],
        'clf__max_doc_update_iter': [50, 100, 150],
        'clf__n_jobs': [-1],
        'clf__verbose': [0],
        'clf__random_state': [None],
    }

    # Perform the grid search.
    latent_dirichlet_allocation_clf = GridSearchCV(latent_dirichlet_allocation_clf, parameters, cv=5, iid=False,
                                                   n_jobs=-1)
    latent_dirichlet_allocation_clf.fit(slo_feature_set)

    if debug_pipeline:
        # View all the information stored in the model after training it.
        classifier_results = pd.DataFrame(latent_dirichlet_allocation_clf.cv_results_)
        log.debug("The shape of the Latent Dirichlet Allocation model's result data structure is:")
        log.debug(classifier_results.shape)
        log.debug(
            "The contents of the Latent Dirichlet Allocation model's result data structure is:")
        log.debug(classifier_results.head())

    # Display the optimal parameters.
    log.debug("The optimal parameters found for the Latent Dirichlet Allocation is:")
    for param_name in sorted(parameters.keys()):
        log.debug("%s: %r" % (param_name, latent_dirichlet_allocation_clf.best_params_[param_name]))
    log.debug("\n")


################################################################################################################

def latent_dirichlet_allocation_topic_extraction():
    """
    Function performs topic extraction on Tweets using LDA.

    :return: none.
    """
    from sklearn.decomposition import LatentDirichletAllocation

    # LDA can only use raw term counts for LDA because it is a probabilistic graphical model.
    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=1000, stop_words='english')
    tf = tf_vectorizer.fit_transform(slo_feature_set)
    tf_feature_names = tf_vectorizer.get_feature_names()

    # Run LDA.
    lda = LatentDirichletAllocation(n_topics=20, max_iter=5, learning_method='online', learning_offset=50.,
                                    random_state=0).fit(tf)

    # Display the top words for each topic.
    display_topics(lda, tf_feature_names, 10)


################################################################################################################

def display_topics(model, feature_names, num_top_words):
    """
    Helper function to display the top words for each topic in the LDA model.

    :param model: the LDA model
    :param feature_names: feature names from CounteVectorizer.
    :param num_top_words: # of words to display for each topic.
    :return: none.
    """
    for topic_idx, topic in enumerate(model.components_):
        log.debug("Topic %d:" % (topic_idx))
        log.debug(" ".join([feature_names[i]
                            for i in topic.argsort()[:-num_top_words - 1:-1]]))


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

    # # Remove "RT" tags.
    # preprocessed_tweet_text = re.sub("rt", "", tweet_text)
    #
    # # Remove URL's.
    # preprocessed_tweet_text = re.sub("http[s]?://\S+", "slo_url", preprocessed_tweet_text)
    #
    # # Remove Tweet mentions.
    # preprocessed_tweet_text = re.sub("@\S+", "slo_mention", preprocessed_tweet_text)
    #
    # # Remove Tweet hashtags.
    # preprocessed_tweet_text = re.sub("#\S+", "slo_hashtag", preprocessed_tweet_text)
    #
    # # Remove all punctuation.
    # preprocessed_tweet_text = preprocessed_tweet_text.translate(str.maketrans('', '', string.punctuation))

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
    tweet_string = str(tweet_text)

    if debug_preprocess_tweets:
        log.debug("Tweet text as string:")
        log.debug(tweet_string)
        log.debug('\n')

    # Split Tweet into individual words.
    words = tweet_string.split()

    if debug_preprocess_tweets:
        log.debug("Tweet text as list:")
        log.debug(words)
        log.debug('\n')

    # Check to see if a word is irrelevant or not.
    words_relevant = []
    for w in words:
        if w not in delete_list:
            words_relevant.append(w)
        else:
            if debug_preprocess_tweets:
                log.debug("Irrelevant word found: ")
                log.debug(w)
                log.debug('\n')

    if debug_preprocess_tweets:
        log.debug("List of relevant words in Tweet: ")
        log.debug(words_relevant)
        log.debug('\n')

    # Convert list back into original Tweet text minus irrelevant words.
    tweet_string = ' '.join(words_relevant)
    # Convert back to a series object.
    tweet_series = pd.Series(tweet_string)

    if debug_preprocess_tweets:
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

    if debug_preprocess_tweets:
        # Print shape and column names.
        log.debug("\n")
        log.debug("The shape of our SLO CMU dataframe:")
        log.debug(slo_dataframe_cmu.shape)
        log.debug("\n")
        log.debug("The columns of our SLO CMU dataframe:")
        log.debug(slo_dataframe_cmu.head)
        log.debug("\n")

    #######################################################

    # # Down-case all text.
    # slo_dataframe_cmu['tweet_t'] = slo_dataframe_cmu['tweet_t'].str.lower()

    # Pre-process each tweet individually.
    slo_dataframe_cmu[str(column_name)] = slo_dataframe_cmu[str(column_name)].apply(preprocess_tweet_text)

    # Reindex everything.
    slo_dataframe_cmu.index = pd.RangeIndex(len(slo_dataframe_cmu.index))
    # slo_dataframe_combined.index = range(len(slo_dataframe_combined.index))

    # Save to CSV file.
    slo_dataframe_cmu.to_csv(str(output_file_path), sep=',',
                             encoding='utf-8', index=False)


############################################################################################

"""
Main function.  Execute the program.
"""
if __name__ == '__main__':

    start_time = time.time()
    ################################################
    """
    Perform the Tweet preprocessing.
    """
    # tweet_dataset_preprocessor("datasets/dataset_20100101-20180510_tok_PROCESSED.csv",
    #                            "datasets/dataset_20100101-20180510_tok_LDA_PROCESSED.csv", "tweet_t")
    # tweet_dataset_preprocessor("datasets/tbl_kvlinden_PROCESSED.csv",
    #                            "datasets/tbl_kvlinden_LDA_PROCESSED.csv", "Tweet")
    # tweet_dataset_preprocessor("datasets/tbl_training_set_PROCESSED.csv",
    #                            "datasets/tbl_training_set_LDA_PROCESSED.csv", "Tweet")
    """
    Perform exhaustive grid search.
    """
    # latent_dirichlet_allocation_grid_search()
    """
    Perform the topic extraction.
    """
    latent_dirichlet_allocation_topic_extraction()
    ################################################
    end_time = time.time()

    if debug_pipeline:
        log.debug("The time taken to perform the operation is: ")
        total_time = end_time - start_time
        log.debug(str(total_time))
        log.debug("\n")

############################################################################################
