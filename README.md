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
# Project Ideation

## Anomalies can be used to detect unusual behavior and subsequently instigate further inspection

### Ideas around anomaly detection use cases (Per Session):
1. Session behavior anomalies
    - intention: to detect, classify, and understand common session-wise behaviors 
    - questions: 
        1. how many session behavior modalities are there?
        2. is there a cluster more likely to have conversions? (if so, perhaps its valuable to subsequently look at common traits)        
        3. are there other metrics that would be valuable to understand?
    - method: thinking unsupervised learning, specifically k-means clustering to find common patterns of behavior     
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
        1. are there bots visible in the data set currently?
        2. what does the distribution of a avg-form-fill-time look like?
    - method: utilize unsupervised learning to detect outliers related to time taken for a session to fill out forms    
- Page behavior anomalies
    - intention to detect potentially negative UX issues
    - ex) latency, num of ajax calls, data transferred, num of events
- Per-page anomalies?

<br/><br/>

# Conclusion

Upon receiving the project instructions and schema from the stakeholders, a good initial amount of time was spent trying to understand the features in the data, thinking about how the data is collected and what kind of anomaly analysis/detection would be valuable.  With the kind of analysis mostly determined (see project ideation above), queries were developed for the BigQuery no-SQL DB (**queries.txt**) to facilite subsequent analysis.  Next, time was spent trying to further understand the nature of the data (**session_analysis.ipynb**), specifically the values held in the categorical variables and the distributions of the real-valued data.  Categorical variables were encoded, the real valued data were standardized/normalized and subsequently saved for the next phase of analysis.  The next phase (**session_data_prep.ipynb**) was spent exploring and peforming dimensionality reduction - per the stakeholder's request - to facilitate model building; several approaches were initially utilized.  The final phase (**session_data_modeling.ipynb**) was preparing for and developing models to try and accomplish some of the goals of the project.  Here, Kmeans clustering was used to try and better understand any underlying structure in the data and due to a large class imbalance, actions were taken to resolve this issue.  Predictive models, as well as a regressive models, were developed to accomplish the project's goal.

<br/>

## Future work
- Spend more time understanding the nature of the modalities of the data, SMEs would be a valuable resource here
- Currently, assumption under both Session and Page analyses is features are independent from Page Id - this would not be the case under future analysis
- Spend more time exploring modeling of real valued, positive conversion, data - specifically graphing and exploring other models

## Questions
- It appears the data, several of its features as well as the conversion rates, is largely multi-modeal (specifically bimodal) - I'm curious if this means there already exists anomalies in the data?







