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
import warnings
import tensorflow as tf
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
debug_preprocess_tweets = False
# Debug create_training_and_test_set() function.
debug_train_test_set_creation = False

################################################################################################################
################################################################################################################

# Import the datasets.
tweet_dataset_processed1 = \
    pd.read_csv("datasets/tbl_kvlinden_PROCESSED.csv", sep=",")

tweet_dataset_processed2 = \
    pd.read_csv("datasets/tbl_training_set_PROCESSED.csv", sep=",")

# Reindex and shuffle the data randomly.
tweet_dataset_processed1 = tweet_dataset_processed1.reindex(
    pd.np.random.permutation(tweet_dataset_processed1.index))

tweet_dataset_processed2 = tweet_dataset_processed2.reindex(
    pd.np.random.permutation(tweet_dataset_processed2.index))

# Generate a Pandas dataframe.
tweet_dataframe_processed1 = pd.DataFrame(tweet_dataset_processed1)
tweet_dataframe_processed2 = pd.DataFrame(tweet_dataset_processed2)

if debug_preprocess_tweets:
    # Print shape and column names.
    log.debug("\n")
    log.debug("The shape of our SLO dataframe 1:")
    log.debug(tweet_dataframe_processed1.shape)
    log.debug("\n")
    log.debug("The columns of our SLO dataframe 1:")
    log.debug(tweet_dataframe_processed1.head)
    log.debug("\n")
    # Print shape and column names.
    log.debug("\n")
    log.debug("The shape of our SLO dataframe 2:")
    log.debug(tweet_dataframe_processed2.shape)
    log.debug("\n")
    log.debug("The columns of our SLO dataframe 2:")
    log.debug(tweet_dataframe_processed2.head)
    log.debug("\n")

# Concatenate the individual datasets together.
frames = [tweet_dataframe_processed1, tweet_dataframe_processed2]
slo_dataframe_combined = pd.concat(frames, ignore_index=True)

# Reindex everything.
slo_dataframe_combined.index = pd.RangeIndex(len(slo_dataframe_combined.index))
# slo_dataframe_combined.index = range(len(slo_dataframe_combined.index))

# Assign column names.
tweet_dataframe_processed_column_names = ['Tweet', 'SLO']

# Create input features.
selected_features = slo_dataframe_combined[tweet_dataframe_processed_column_names]
processed_features = selected_features.copy()

if debug_preprocess_tweets:
    # Check what we are using as inputs.
    log.debug("\n")
    log.debug("The Tweets in our input feature:")
    log.debug(processed_features['Tweet'])
    log.debug("\n")
    log.debug("SLO TBL topic classification label for each Tweet:")
    log.debug(processed_features['SLO'])
    log.debug("\n")

# Create feature set and target sets.
slo_feature_set = processed_features['Tweet']
slo_target_set = processed_features['SLO']


#######################################################
def create_training_and_test_set():
    """
    This functions splits the feature and target set into training and test sets for each set.

    Note: We use this to generate a randomized training and target set in order to average our results over
    n iterations.

    random_state = rng (where rng = random number seed generator)

    :return: Nothing.  Global variables are established.
    """
    global tweet_train, tweet_test, target_train, target_test, target_train_encoded, target_test_encoded

    from sklearn.model_selection import train_test_split

    import random
    rng = random.randint(1, 1000000)
    # Split feature and target set into training and test sets for each set.
    tweet_train, tweet_test, target_train, target_test = train_test_split(slo_feature_set, slo_target_set,
                                                                          test_size=0.33,
                                                                          random_state=rng)

    if debug_train_test_set_creation:
        log.debug("Shape of tweet training set:")
        log.debug(tweet_train.data.shape)
        log.debug("Shape of tweet test set:")
        log.debug(tweet_test.data.shape)
        log.debug("Shape of target training set:")
        log.debug(target_train.data.shape)
        log.debug("Shape of target test set:")
        log.debug(target_test.data.shape)
        log.debug("\n")

    #######################################################

    # Use Sci-kit learn to encode labels into integer values - one assigned integer value per class.
    from sklearn import preprocessing

    target_label_encoder = preprocessing.LabelEncoder()
    target_train_encoded = target_label_encoder.fit_transform(target_train)
    target_test_encoded = target_label_encoder.fit_transform(target_test)

    target_train_decoded = target_label_encoder.inverse_transform(target_train_encoded)
    target_test_decoded = target_label_encoder.inverse_transform(target_test_encoded)

    if debug_train_test_set_creation:
        log.debug("Encoded target training labels:")
        log.debug(target_train_encoded)
        log.debug("Decoded target training labels:")
        log.debug(target_train_decoded)
        log.debug("\n")
        log.debug("Encoded target test labels:")
        log.debug(target_test_encoded)
        log.debug("Decoded target test labels:")
        log.debug(target_test_decoded)
        log.debug("\n")

    # return [tweet_train, tweet_test, target_train, target_test, target_train_encoded, target_test_encoded]


################################################################################################################

def topic_extraction_nmf_lda_example():
    """
       Function performs topic extraction using Non-Negative Matrix Factorization (NMF) and
       Latent Dirichlet Allocation (LDA).

       :return: Nothing.
       """

    # Author: Olivier Grisel <olivier.grisel@ensta.org>
    #         Lars Buitinck
    #         Chyi-Kwei Yau <chyikwei.yau@gmail.com>
    # License: BSD 3 clause

    from time import time

    from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
    from sklearn.decomposition import NMF, LatentDirichletAllocation
    from sklearn.datasets import fetch_20newsgroups

    n_samples = 2000
    n_features = 1000
    n_components = 10
    n_top_words = 20

    def print_top_words(model, feature_names, n_top_words):
        for topic_idx, topic in enumerate(model.components_):
            message = "Topic #%d: " % topic_idx
            message += " ".join([feature_names[i]
                                 for i in topic.argsort()[:-n_top_words - 1:-1]])
            print(message)
        print()

    # Load the 20 newsgroups dataset and vectorize it. We use a few heuristics
    # to filter out useless terms early on: the posts are stripped of headers,
    # footers and quoted replies, and common English words, words occurring in
    # only one document or in at least 95% of the documents are removed.

    print("Loading dataset...")
    t0 = time()
    dataset = fetch_20newsgroups(shuffle=True, random_state=1,
                                 remove=('headers', 'footers', 'quotes'))
    data_samples = dataset.data[:n_samples]
    print("done in %0.3fs." % (time() - t0))

    # Use tf-idf features for NMF.
    print("Extracting tf-idf features for NMF...")
    tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,
                                       max_features=n_features,
                                       stop_words='english')
    t0 = time()
    tfidf = tfidf_vectorizer.fit_transform(data_samples)
    print("done in %0.3fs." % (time() - t0))

    # Use tf (raw term count) features for LDA.
    print("Extracting tf features for LDA...")
    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2,
                                    max_features=n_features,
                                    stop_words='english')
    t0 = time()
    tf = tf_vectorizer.fit_transform(data_samples)
    print("done in %0.3fs." % (time() - t0))
    print()

    # Fit the NMF model
    print("Fitting the NMF model (Frobenius norm) with tf-idf features, "
          "n_samples=%d and n_features=%d..."
          % (n_samples, n_features))
    t0 = time()
    nmf = NMF(n_components=n_components, random_state=1,
              alpha=.1, l1_ratio=.5).fit(tfidf)
    print("done in %0.3fs." % (time() - t0))

    print("\nTopics in NMF model (Frobenius norm):")
    tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    print_top_words(nmf, tfidf_feature_names, n_top_words)

    # Fit the NMF model
    print("Fitting the NMF model (generalized Kullback-Leibler divergence) with "
          "tf-idf features, n_samples=%d and n_features=%d..."
          % (n_samples, n_features))
    t0 = time()
    nmf = NMF(n_components=n_components, random_state=1,
              beta_loss='kullback-leibler', solver='mu', max_iter=1000, alpha=.1,
              l1_ratio=.5).fit(tfidf)
    print("done in %0.3fs." % (time() - t0))

    print("\nTopics in NMF model (generalized Kullback-Leibler divergence):")
    tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    print_top_words(nmf, tfidf_feature_names, n_top_words)

    print("Fitting LDA models with tf features, "
          "n_samples=%d and n_features=%d..."
          % (n_samples, n_features))
    lda = LatentDirichletAllocation(n_components=n_components, max_iter=5,
                                    learning_method='online',
                                    learning_offset=50.,
                                    random_state=0)
    t0 = time()
    lda.fit(tf)
    print("done in %0.3fs." % (time() - t0))

    print("\nTopics in LDA model:")
    tf_feature_names = tf_vectorizer.get_feature_names()
    print_top_words(lda, tf_feature_names, n_top_words)


################################################################################################################

def latent_dirichlet_allocation_grid_search():
    """
    Function performs exhaustive grid search for LDA.

    :return: None.
    """
    from sklearn.decomposition import LatentDirichletAllocation

    # Create randomized training and test set using our dataset.
    create_training_and_test_set()

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
    latent_dirichlet_allocation_clf.fit(tweet_train)

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

    # Create randomized training and test set using our dataset.
    create_training_and_test_set()

    # LDA can only use raw term counts for LDA because it is a probabilistic graphical model.
    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=1000, stop_words='english')
    tf = tf_vectorizer.fit_transform(tweet_train)
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
    :param feature_names: feature names from CounteVectorizer
    :param num_top_words: # of words to display for each topic.
    :return: none.
    """
    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d:" % (topic_idx))
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-num_top_words - 1:-1]]))


############################################################################################

"""
Main function.  Execute the program.
"""
import time

if __name__ == '__main__':

    start_time = time.time()

    ################################################
    """
    Scikit-Learn NMF-LDA example.
    """
    # topic_extraction_nmf_lda_example()

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
        log.debug("The time taken to perform LDA is: ")
        total_time = end_time - start_time
        log.debug(str(total_time))
        log.debug("\n")

############################################################################################
