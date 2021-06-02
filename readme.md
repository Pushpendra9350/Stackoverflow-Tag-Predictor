# Stackoverflow Tag Predictor

## VIDEO DEMO: https://youtu.be/ToN2-lN5FAM

## Table Of Content 
[Overview](#overview)<br>
[Motivation](#motivation)<br>
[Screenshots](#screenshots)<br>
[How to run it](#runit)<br>
[Technical Aspects & architecture](#tech)<br>
[Future Scope](#future)<br>
[References](#ref)<br>


<a name="overview"></a>
### Overview 
This is a web-based application in which we are solving a Multilabel classification problem. Here we need to enter the StackOverflow question title and description and it will predict tags for the questions. Here we are calculating Micro F1 score and we are getting 0.49 with only 100K data points.<br>
**Problem Statement**: Whenever an new question arrive on stackoverflow then we need to predict tags about that question based on the question content.

<a name="motivation"></a>
### Motivation
Motive to make this application
* To learn how to work with text data
* To know how to solve multilabel problem
* To learn NLP techniques for text dataset
* To handle large dataset

<a name="screenshots"></a>
### Screenshots
<img width="600" alt="Stackoverflow screenshot" src="https://user-images.githubusercontent.com/43174363/118759378-8f102980-b88e-11eb-98c5-e6e9fc356909.png">

<a name="runit"></a>
### How to run
NOTE: Model size is big then I am not able to upload here to download it follow the links given in these steps.
* First, Download templates and app.py files from this github repository
* Then download Model with https://drive.google.com/file/d/1w2L7xBO-iHTaRMxQIojsCFSen1oz0Ppi/view?usp=sharing
* To download vectorizer with https://drive.google.com/file/d/1aYz8YtmhworWtZ8ITHxgKY85c9VCJF_l/view?usp=sharing
* To download tag list with https://drive.google.com/file/d/1vObP_nooSik4RQklx9T-CjzqDSCw-6W9/view?usp=sharing
* Next all these files should be in the same folder and make sure all required libraries need to be installed
* Go to terminal and run "python app.py" DONE.

<a name="tech"></a>
### Technical Aspects

#### Architecture
![photo_2021-06-02 19 49 36](https://user-images.githubusercontent.com/43174363/120502136-cd096380-c3df-11eb-92d3-a827d4d0c885.jpeg)

#### About Dataset
To download dataset: https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction/data
* **Train.csv:** Have 4 dimensions: Id,Title,Body,Tags.
    * Id: Question id
    * Title: Title of the question
    * Body: Where we have actual explaination of the question
    * Tags: Tags related to that question
Dataset screenshot<br><br>
<img width="871" alt="Screenshot 2021-06-02 at 8 49 42 PM" src="https://user-images.githubusercontent.com/43174363/120507003-122f9480-c3e4-11eb-9cfd-60f2d95a2684.png">
<br>

* **Test.csv:** contains the same columns but without the Tags, we need to predict them.
* **Size of Train.csv:** 6.75GB --> Compressed form 2.19GB
* **Size of Test.csv:** 2GB --> Compressed form 725.1MB
* **Number of rows in Train.csv:** 6034195 or 6.03 Millions

Actually this is a quite large dataset to work on a small machine.

#### Modeling 
* Here we are going to use Logistic regression algorithm to train our model.<br>
**BUT WHY LOGISTIC REGRESSION USED ONLY**<br>
This problem is a multilabel classification and text problem.
* Due to vectorization with TFIDF dimensionality of dataset is very high and if dimensionality is very then LINEAR MODELS works perfect.
* Other Non-linear models(SVM(rbf), Random Forest, GBDT etc.) do not work very well in high dimensions.
* Any we are not considering Linear SVM here because time complexity of SVM is high and here we have train 500 model in final case so Logistic regression works very well in this case and performace for both are very similar.

To reduce the complexity and increase the accuracy of the model I did small feature engineering which is select only to 500 tags and give 3 time weight to title. Let see how this works.<br>
<img width="600" alt="Screenshot 2021-05-21 at 11 11 33 PM" src="https://user-images.githubusercontent.com/43174363/120507012-152a8500-c3e4-11eb-8977-cb903d38c92a.png"><br><br>
We have try variuos types of models like Linear SVM, Logisticregression with 4 grams, and SGD with logloss all are performing same<br>

#### Technology and tools used
* Python
* Flask
* Sklearn
* Jupyter notebook
* etc

<a name="future"></a>
#### Future Scope
* We can train our model with complete dataset which will improve performance drastically.
* We can use this application in fashion website to add tags in each product.

<a name="ref"></a>
#### References
* https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction/code
* https://medium.datadriveninvestor.com/predicting-tags-for-the-questions-in-stack-overflow-29438367261e


Thanks For Reading.
