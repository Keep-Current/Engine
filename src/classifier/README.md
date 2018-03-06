## Requirements:
It should classify documents by converting them into a vector/matrix representing the topic.

Input: a document (text file)
Output: a vector representing the document


## How?
1. it parses the document: semantic representation?  
2. it converts it into a vector/matrix representation

## To Consider:
1. Use different preprocessing and classification approaches: embedded representation of words (gloVe, FastText), different ways to represent a document vector / matrix out of a document.
2. Create different classes for each task, implementing different approaches with a similar interface, so that one can be easily replaced with the other. 
3. test and compare the results
4. Prepare a results summarization page, and explain why the selected method was chosen 

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
