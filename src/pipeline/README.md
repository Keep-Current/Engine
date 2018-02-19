## The pipeline
The pipeline is responsible of running the different modules together.

## How?
Every document from the scrapper is running through the pipeline, in order to be categorized and extracted.
The pipeline should define an common interface for the packages to implement, in order to be able in the future to replace one module with another (one implementation with another). 