# Problem Statement

## ***"The overall objective will be to create an anomaly detection system that will alert a user when a metric is anomalous."***

## ***"How that is defined, what metric you choose, and what software you use is up to you."***



### ***"Using the transformed data, provide a model that helps predict anomalies based on any aggregatable measure/metric in our data.  This may be something like conversion rate, sum of revenue, or another such metric you think may be valuable.  As you will see, there is a large number of features that can be used to predict anomalies - please consider dimensionality reduction as part of your model (PCA, FA, etc), and explain why this is your approach."***

<br/><br/>
# Intial Data Exploration via BigQuery

- Data includes Session data related to user, device, os, location, and the referrer
    - also includes some summary stats related to conversion value and engagement
- For each session, data contains pages visited and its respective details such as general behavior on that page
    - also includes a collection of all events that occured on that page, detailing the event along with whether that event was considered a conversion 
    - also includes a collection of all the forms that were filled out on the page, detailing time to fill out those forms
    - also includes a collection of all clicks that occurred on the page

<br/><br/>
# Ideation

## Anomalies can be used to detect unusual behavior and subsequently instigate further inspection

### Ideas around anomaly detection use cases (Per Session): [jupyter notebook](./session_analyis.ipynb)
1. Session behavior anomalies
    - intention: to detect, classify, and understand common session-wise behaviors 
    - questions: 
        1. how many session behavior modalities are there?
        2. is there a cluster more likely to have conversions? (if so, perhaps its valuable to subsequently look at common traits)        
        3. are there other metrics that would be valuable to understand?
    - method: unsupervised learning, specifically k-means clustering to find common patterns of behavior     
2. Model to predict conversions
    - intention: 
        1. to see how well a model can predict conversion rate
        2. to see how particular features contribute to conversion rate    
    - method: simple linear regression
        1. anomalies would then be identified by its error

### Uses cases for anomaly detection(Per page):
- Bot Detection
    - intention: detect bots
    - questions:
        1. are there \[sufficient\] bots visible in the data set currently?
        2. what does the distribution of a avg-form-fill-time look like?        
    - method: utilize unsupervised learning to detect outliers related to time taken for a session to fill out forms    
- Page behavior anomalies
    - intention to detect potentially negative UX issues
    - ex) latency, num of ajax calls, data transferred, num of events
- (stretch goal) Per-page anomalies?

<br/><br/>

# Conclusion

## Questions
- It appears the data, several of its features as well as the conversion rates, is largely bimodal - I'm therefore curious if this means there already exists anomalies in the data?

## Future work
- Currently, assumption under both Session and Page analyses is features are independent from Page Id - this would not be the case under future analysis


