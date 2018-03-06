## Objective:
To decide if a document should enter the aggregated user's document list.

### Input:
- retrieve from the DB users key interest topics (represented as a vector)
- a parsed document representation (vector? matrix?)

### ouput:
- the distance between each user's vector to the given document 

OR:

- the probability of a positve relation between a certain document to the users' interest vector



### How?
- consider using the [coritcal.io semantical folding](http://www.cortical.io/static/downloads/semantic-folding-theory-white-paper.pdf) approach for classifciation 