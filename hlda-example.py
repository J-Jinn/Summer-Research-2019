# %load_ext autoreload
# %autoreload 2
# %matplotlib inline

import sys
import os

basedir = '..'
sys.path.append(os.path.join(basedir))

import pylab as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from wordcloud import WordCloud
from hlda.sampler import HierarchicalLDA
from ipywidgets import widgets
from IPython.core.display import HTML, display
import numpy as np
import string
import glob

nltk.download('stopwords')
stopset = stopwords.words('english') + list(string.punctuation) + ['will', 'also', 'said']

corpus = []
all_docs = []
vocab = set()

stemmer = PorterStemmer()
for filename in glob.glob(os.path.join(basedir, 'bbc', 'tech', '*.txt')):
    with open(filename) as f:
        try:

            doc = f.read().splitlines()
            doc = filter(None, doc)  # remove empty string
            doc = '. '.join(doc)

            to_remove = string.punctuation
            table = str.maketrans("", "", to_remove)
            doc = doc.translate(table)  # strip punctuations

            to_remove = "0123456789"
            table = str.maketrans("", "", to_remove)
            doc = doc.translate(table)  # strip numbers

            doc = doc.encode("utf8").decode('ascii', 'ignore')  # ignore fancy unicode chars
            all_docs.append(doc)

            tokens = word_tokenize(str(doc))
            filtered = []
            for w in tokens:
                w = stemmer.stem(w.lower())  # use Porter's stemmer
                if len(w) < 3:  # remove short tokens
                    continue
                if w in stopset:  # remove stop words
                    continue
                filtered.append(w)

            vocab.update(filtered)
            corpus.append(filtered)

        except UnicodeDecodeError:
            print('Failed to load', filename)

print("Done.")

vocab = sorted(list(vocab))
vocab_index = {}
for i, w in enumerate(vocab):
    vocab_index[w] = i

print(len(all_docs))

print(len(vocab))
print(vocab[0:100])

# wordcloud = WordCloud(background_color='white').generate(' '.join(all_docs))
# plt.figure(figsize=(12, 12))
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()
#
# print(len(vocab), len(corpus), len(corpus[0]), len(corpus[1]))

new_corpus = []
for doc in corpus:
    new_doc = []
    for word in doc:
        word_idx = vocab_index[word]
        new_doc.append(word_idx)
    new_corpus.append(new_doc)

# print(len(vocab), len(new_corpus))
# print(corpus[0][0:10])
# print(new_corpus[0][0:10])

n_samples = 500       # no of iterations for the sampler
alpha = 10.0          # smoothing over level distributions
gamma = 1.0           # CRP smoothing parameter; number of imaginary customers at next, as yet unused table
eta = 0.1             # smoothing over topic-word distributions
num_levels = 3        # the number of levels in the tree
display_topics = 50   # the number of iterations between printing a brief summary of the topics so far
n_words = 5           # the number of most probable words to print for each topic after model estimation
with_weights = False  # whether to print the words with the weights

hlda = HierarchicalLDA(new_corpus, vocab, alpha=alpha, gamma=gamma, eta=eta, num_levels=num_levels)
hlda.estimate(n_samples, display_topics=display_topics, n_words=n_words, with_weights=with_weights)
