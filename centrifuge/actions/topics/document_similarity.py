from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models, similarities

import os
import nltk

class DocSimilarity(object):

    def __init__(self, base_filename='reasoning'):
        dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\'
        self.dictionary = corpora.Dictionary.load(dir_path + base_filename + '_corpura.dict')
        self.corpus = corpora.MmCorpus(dir_path + base_filename + '_bow.mm')

    def initialize_corpus(self):
        # Transformator:
        self.tfidf = models.TfidfModel(self.corpus)

        self.corpus_tfidf = self.tfidf[self.corpus]
        
        self.lsi_model = models.LsiModel(self.corpus_tfidf, id2word=self.dictionary, num_topics=20)
        self.corpus_lsi = self.lsi_model[self.corpus_tfidf]


    def tokenize(self, text):
        tokens = nltk.word_tokenize(text)
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
        vec_bow = self.dictionary.doc2bow(doc.lower().split())
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
        return sims
