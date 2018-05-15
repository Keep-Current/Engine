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
The name was intentionally was not set to be 'vector-distance-measure' or anything in this direction, in order to leave room for creativity as for how should the relativity of one document to another is measured.

Ideas to consider:
- using the [coritcal.io semantical folding](http://www.cortical.io/static/downloads/semantic-folding-theory-white-paper.pdf) approach for classifciation 
- using LDA
- different methods for vector-distance
- identifying clusters within matrices 