import pandas as pd
import glob
import nltk
import re

from pathlib import Path

from gensim.corpora import Dictionary, HashDictionary, MmCorpus
from gensim import models, utils

# ToDo: check performance with lemmatization: gensim.utils.lemmatize

nltk.download('punkt')
nltk.download('stopwords')

DEFAULT_DICT_SIZE = 100000
SPECIAL_CHARS = '[^A-Za-z0-9 ]+'
STOPWORDS = nltk.corpus.stopwords.words('english')

def preprocess(text):
    tokens = [re.sub(SPECIAL_CHARS, '', word.lower()) for word in nltk.word_tokenize(text)]
    tokens = [word for word in tokens if word not in STOPWORDS]
    tokens = list(filter(None, tokens))
    return tokens


class Corpus(object):
    def __iter__(self):
        for file in glob.glob("*.txt"):
            print(file)
            paper = Path(file).read_text(encoding='utf8')
            yield paper


corpus_memory_friendly = Corpus()
papers = list(corpus_memory_friendly)

texts = [list(preprocess(t)) for t in papers]

# define the dictionary:
dictionary = Dictionary(texts)
dictionary.save('reasoning_corpura.dict')

corpus = [dictionary.doc2bow(text) for text in texts]
MmCorpus.serialize('reasoning_bow.mm', corpus)


hash_dictionary = HashDictionary(texts )
hash_dictionary.filter_extremes(no_below=20, no_above=0.1, keep_n=DEFAULT_DICT_SIZE)
hash_dictionary.save_as_text('reasoning_wordids.txt.bz2')
hash_dictionary.save('reasoning_corpura_hash.dict')

