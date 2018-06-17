import os
import re
import nltk

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models, similarities

class DocSimilarity(object):

    def __init__(self, base_filename='reasoning'):
        """
        The reasoning corpus contains 4 documents (papers).
        
        """
        dir_path = os.path.dirname(os.path.realpath(__file__)) + '/'
        self.dictionary = corpora.Dictionary.load(dir_path + base_filename + '_corpura.dict')
        self.corpus = corpora.MmCorpus(dir_path + base_filename + '_bow.mm')

        self.SPECIAL_CHARS = '[^A-Za-z0-9 ]+'
        self.stopwords = nltk.corpus.stopwords.words('english')

    def initialize_corpus(self):
        # Transformator:
        # self.tfidf = models.TfidfModel(self.corpus)
        # self.corpus_tfidf = self.tfidf[self.corpus]        
        self.lsi_model = models.LsiModel(self.corpus, 
                                         id2word=self.dictionary, 
                                         num_topics=20)
        
        # self.corpus_lsi = self.lsi_model[self.corpus_tfidf]

    def preprocess(self, text):
        tokens = [re.sub(self.SPECIAL_CHARS, '', word.lower()) for word in nltk.word_tokenize(text)]
        tokens = [word for word in tokens if word not in self.stopwords]
        tokens = list(filter(None, tokens))
        return tokens

    def tokenize(self, text):
        tokens = self.preprocess(text)
        stems = []
        for item in tokens:
            stems.append(PorterStemmer().stem(item))
        return stems

    def doc_to_bow(self, doc):
        return self.dictionary.doc2bow(doc.lower().split())

    def doc_to_tfidf(self, doc):
        """Transforming a document into a bag-of-words
        
        Arguments:
            doc {string} -- a document to be transformed
        """
        return self.tfidf[self.doc_to_bow(doc)]

    def doc_to_lsi(self, doc):
        """Transforming a document into a bag-of-words
        
        Arguments:
            doc {string} -- a document to be transformed
        """
        return self.lsi_model[self.doc_to_bow(doc)]

    def compare_doc(self, index, doc):
        tokens = self.preprocess(doc)
        vec_bow = self.dictionary.doc2bow(tokens)
        vec_lsi = self.lsi_model[vec_bow]
        yield index[vec_lsi]
    
    def compare_docs(self, doc_list):
        """
        returns a score for each doc in the list, and its relativity to 
        the current corpora.
        """
        # get the base corpus space
        index = similarities.MatrixSimilarity(self.lsi_model[self.corpus]) 
        
        sims = [self.compare_doc(index, doc) for doc in doc_list]
        avg_idx, special_idx = self.filter_top_results(sims)

        avg_docs = [doc_list[idx] for idx in avg_idx]
        special_docs = [doc_list[idx] for idx in special_idx]

        return avg_docs +special_docs

    def filter_top_results(self, sims):
        # let's filter the top matches
        THRESHOLD = 0.7
        SPECIAL_THRESHOLD = 0.95

        df = pd.DataFrame(sims)

        results_special = df[df > SPECIAL_THRESHOLD]
        results_special = results_special.dropna(how='all')

        df = df.assign(S=df.loc[:,:].sum(1))
        results_avg = df[df > THRESHOLD].dropna().sort_values(by='S', axis=0)

        return results_avg.index.values.tolist(), results_special.index.values.tolist()