## Requirements:
It should classify documents by their relevance to a specific topic list
It should be adjustable according to a set of keywords that represent the desired categories

Input: parsed & Chunked document
Output: probabilities of relevance for each of the given keywords (categories)


## How?
1. It is initialized with a set of categories keywords.
2. Parse the document (embedded representation?)
3. run a classifier algorithm (i.e. CNN)

## To Consider:
1. Use different preprocessing and classification approaches: embedded representation of words (gloVe, FastText), CNN, character-level CNN, LDA...
2. Create different classes for each task, implementing different approaches 
3. test and compare the results
4. Prepare a results summarization page, and show why the selected method was chosen 

## Resources
Optional modules to use:
* [Gensim](https://radimrehurek.com/gensim/)

Optional approaches and recommended reading:
* [Any-gram Kernels for Sentence Classification: A Sentiment Analysis Case Study
](https://arxiv.org/abs/1712.07004)
* [Very Deep Convolutional Networks for Text Classification](https://arxiv.org/abs/1606.01781)
* [Character-level Convolutional Networks for Text Classification](https://arxiv.org/abs/1509.01626)
* [A Primer on Neural Network Models for Natural Language Processing](https://arxiv.org/abs/1510.00726)
* [A Sensitivity Analysis of (and Practitioners' Guide to) Convolutional Neural Networks for Sentence Classification](https://arxiv.org/abs/1510.03820)
