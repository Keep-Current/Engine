import pandas as pd

from gensim.corpora import HashDictionary, MmCorpus
from gensim import utils 

DEFAULT_DICT_SIZE = 100000

"""
Papers.csv is too big to upload to github.
Download it from:

    https://www.kaggle.com/benhamner/nips-papers/downloads/papers.csv/2

"""
papers = pd.read_csv('papers.csv')
corpus = list(papers['paper_text'])

print("corpus size: ", len(corpus))


# ToDo: check performance with lemmatization: gensim.utils.lemmatize

tokenized_corpus = [[utils.to_unicode(token) for token in 
                    utils.tokenize(corpus_item, lower=True, errors='ignore')]
                    for corpus_item in corpus]


hash_dictionary = HashDictionary(tokenized_corpus )

bow_corpus = [hash_dictionary.doc2bow(text) for text in corpus]
MmCorpus.serialize('nips_bow.mm', bow_corpus, progress_cnt=10000) 


hash_dictionary.filter_extremes(no_below=20, no_above=0.1, keep_n=DEFAULT_DICT_SIZE)
hash_dictionary.save_as_text('nips_wordids.txt.bz2')
