The Classifeir module is initialized with a set of categories keywords.

It has a method 'categorize_document' that receives a document as an input (cleaned - text only), and returns a vector that represents its similarity to the list of categories.


How?
1. the document is broken to pargraphs, sentences and then tokenized.
2. Every sentence should be POS tagged
3. Every sentence should also be chunked 
4. pass the processed chunked sentenece through the classifier:
4.1 should use embedded representation?



Recommended modules:
Gensim: https://radimrehurek.com/gensim/

Optional approaches:
https://arxiv.org/pdf/1712.07004.pdf


ToDo:
1. Create different classes for each of the task, implementing different approaches; test and compare the results
2. Prepare a results summarization page, and show why the selected method was chosen 