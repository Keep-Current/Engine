import pandas as pd
import glob

from pathlib import Path

from gensim.corpora import Dictionary, HashDictionary, MmCorpus
from gensim import utils 

DEFAULT_DICT_SIZE = 100000

# ToDo: check performance with lemmatization: gensim.utils.lemmatize



class Corpus(object):
     def __iter__(self):
         for file in glob.glob("*.txt"):
             print(file)
             paper = Path(file).read_text(encoding='utf8')
             # assume there's one document per line, tokens separated by whitespace
             yield paper.lower().split()

corpus_memory_friendly = Corpus()
corpus = list(corpus_memory_friendly)
dictionary = Dictionary(corpus)
dictionary.save('reasoning_corpura.dict')

class BowCorpus(object):
     def __iter__(self):
         for file in glob.glob("*.txt"):
             print(file)
             paper = Path(file).read_text(encoding='utf8')
             # assume there's one document per line, tokens separated by whitespace
             yield dictionary.doc2bow(paper.lower().split())



corpus_memory_friendly = BowCorpus()
bow_corpus = list(corpus_memory_friendly)
MmCorpus.serialize('reasoning_bow.mm', bow_corpus, progress_cnt=10000) 


hash_dictionary = HashDictionary(corpus )
hash_dictionary.filter_extremes(no_below=20, no_above=0.1, keep_n=DEFAULT_DICT_SIZE)
hash_dictionary.save_as_text('reasoning_wordids.txt.bz2')
hash_dictionary.save('reasoning_corpura_hash.dict')

