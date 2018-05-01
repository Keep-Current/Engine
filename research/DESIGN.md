# Keep-Current Engine - Design (Draft)
> Engine makes recommendation of documents a user should read.

Description: Based on language patterns in documents and user ratings, the engine recommends new documents to users. This will be accomplished by a) analysing and comparing NLP patterns in the documents and b) collaborative filtering (wisdom of the crowd) technigues. Both tactics should be combined to create a list of documents, a user should read.


## Dev Stages
_STAGE_01_ (Deadline 17.05.2018)

* Doc_Similarity only: based on tf-idf or doc2vec combined with nearest neighbor search
* Recommendation: top-N docs from Doc_Similarity

_STAGE_02_

* Doc_Similarity: taken from STAGE_01
* User_Similarity: item-based collaborative filtering or model-based collaborative filtering (SVD or NMF)
* Recommendation: top-N docs from Doc_Similarity + top-N docs from User_Similarity

... TBA ...

_STAGE_X_

* Doc_Similarity: learned with deep learning techniques (word embeddings, siamese networks, ...)
* User_Similarity: taken from deep learned matrix (embedding, ...)
* Topic_Modeling: learn keywords from documents
* Recommendation: combination based on learned weights


## Architecture (Draft)

### INPUT

| Input    |      | via  |      | From                          |
| -------- |:----:|:----:|:----:|:------------------------------|
| Document |  <=  |  DB  |  <=  | Keep-Current/Crawler-Scrapper |
| User     |  <=  |  DB  |  <=  | Keep-Current/WebApp           |


#### Document

* Doc_ID
* Src_URL
* ? Keywords
* Authors
* Text
* ? Abstract
* ...

#### User

* User_ID
* Likes [Doc_ID]
* Dislikes [Doc_ID]
* Refused_docs [Doc_ID]
* ...



### THROUGHPUT

| From     |      | via             |      |        | To             |
| -------- |:----:|:----------------|:----:|:-------|:---------------|
| Document |  =>  | Doc_Similarity  |  =>  |        |                |
|          |  =>  |                 |      |  +  => | Recommendation |
|          |  +   |                 |      |        |                |
| User     |  =>  | Item_Similarity |  =>  |        |                |


#### Doc_Similarity

Approaches to evaluate: tf-idf + similiarity_measure (eg cosine similarity), doc2vec, ...

Evaluation:

|What                                | Measure        | Metric       |
|:-----------------------------------|:---------------|:-------------|
| Discriminate clusters of documents | Correct topics | TBA          |
| Discriminate writing style         | Correct author | TBA          |


#### Item_Similarity

Approaches to evaluate: model-based CF (SVD, PMF, NMF), if poor performance hard-code a item-based CF algorithm


#### Recommendation

STAGE_01: top-N from Doc_Similarity only



### OUTPUT

| From           |            | To                  |
| -------------- |:----------:| --------------------|
| Recommendation |     =>     | Keep-Current/WebApp |
|                |     =>     | DB                  |


## Evaluation

STAGE_01: Bootstrapped test dataset, TBA

Later: User feedback loop


