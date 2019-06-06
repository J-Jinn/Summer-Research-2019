"""
SLO Topic Modeling
Advisor: Professor VanderLinden
Name: Joseph Jinn
Date: 5-29-19

Scikit-Learn: LDA - Latent Dirichlet Allocation

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

# Import libraries.
import logging as log
import warnings
import tensorflow as tf
import time
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

# Import custom utility functions.
import slo_lda_topic_extraction_utility_functions as lda_util

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
tf.logging.set_verbosity(tf.logging.INFO)

################################################################################################################
################################################################################################################

# Import the dataset.
tweet_dataset_processed = \
    pd.read_csv("datasets/dataset_20100101-20180510_tok_LDA_PROCESSED.csv", sep=",")

# Reindex and shuffle the data randomly.
tweet_dataset_processed = tweet_dataset_processed.reindex(
    pd.np.random.permutation(tweet_dataset_processed.index))

# Generate a Pandas dataframe.
tweet_dataframe_processed = pd.DataFrame(tweet_dataset_processed)

# Print shape and column names.
log.info("\n")
log.info("The shape of our preprocessed SLO dataframe:")
log.info(tweet_dataframe_processed.shape)
log.info("\n")
log.info("The columns of our preprocessed SLO dataframe:")
log.info(tweet_dataframe_processed.head)
log.info("\n")

# Drop any NaN or empty Tweet rows in dataframe (or else CountVectorizer will blow up).
tweet_dataframe_processed = tweet_dataframe_processed.dropna()

# Print shape and column names.
log.info("\n")
log.info("The shape of our preprocessed SLO dataframe with NaN (empty) rows dropped:")
log.info(tweet_dataframe_processed.shape)
log.info("\n")
log.info("The columns of our preprocessed SLO dataframe with NaN (empty) rows dropped:")
log.info(tweet_dataframe_processed.head)
log.info("\n")

# Reindex everything.
tweet_dataframe_processed.index = pd.RangeIndex(len(tweet_dataframe_processed.index))

# Assign column names.
tweet_dataframe_processed_column_names = ['Tweet']

# Rename column in dataframe.
tweet_dataframe_processed.columns = tweet_dataframe_processed_column_names

# Create input feature.
selected_features = tweet_dataframe_processed[tweet_dataframe_processed_column_names]
processed_features = selected_features.copy()

# Check what we are using as inputs.
log.debug("\n")
log.debug("The Tweets in our input feature:")
log.debug(processed_features['Tweet'])
log.debug("\n")

# Create feature set.
slo_feature_set = processed_features['Tweet']


################################################################################################################

def latent_dirichlet_allocation_topic_extraction():
    """
    Function performs topic extraction on Tweets using Scikit-Learn LDA model.

    :return: None.
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
    lda_util.display_topics(lda, tf_feature_names, 10)


################################################################################################################

def latent_dirichlet_allocation_grid_search():
    """
    Function performs exhaustive grid search for Scikit-Learn LDA model.

    :return: None.
    """
    from sklearn.decomposition import LatentDirichletAllocation
    from sklearn.model_selection import GridSearchCV

    # Construct the pipeline.
    latent_dirichlet_allocation_clf = Pipeline([
        ('vect', CountVectorizer(max_df=0.95, min_df=2, max_features=1000, stop_words='english')),
        ('clf', LatentDirichletAllocation()),
    ])

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

    # View all the information stored in the model after training it.
    classifier_results = pd.DataFrame(latent_dirichlet_allocation_clf.cv_results_)
    log.debug("The shape of the Latent Dirichlet Allocation model's result data structure is:")
    log.debug(classifier_results.shape)
    log.debug(
        "The contents of the Latent Dirichlet Allocation model's result data structure is:")
    log.debug(classifier_results.head())

    # Display the optimal parameters.
    log.info("The optimal parameters found for the Latent Dirichlet Allocation is:")
    for param_name in sorted(parameters.keys()):
        log.info("%s: %r" % (param_name, latent_dirichlet_allocation_clf.best_params_[param_name]))
    log.info("\n")


################################################################################################################

############################################################################################

"""
Main function.  Execute the program.
"""
if __name__ == '__main__':
    start_time = time.time()
    ################################################
    """
    Perform the Twitter dataset preprocessing.
    """
    # lda_util.tweet_dataset_preprocessor("datasets/dataset_20100101-20180510_tok_PROCESSED.csv",
    #                                     "datasets/dataset_20100101-20180510_tok_LDA_PROCESSED2.csv", "tweet_t")
    """
    Perform exhaustive grid search.
    """
    # latent_dirichlet_allocation_grid_search()
    """
    Perform the topic extraction.
    """
    # latent_dirichlet_allocation_topic_extraction()
    ################################################
    end_time = time.time()

    log.info("The time taken to perform the operation is: ")
    total_time = end_time - start_time
    log.info(str(total_time))
    log.info("\n")

    # For debugging purposes for Jupyter notebook.
    lda_util.test_function()

############################################################################################
