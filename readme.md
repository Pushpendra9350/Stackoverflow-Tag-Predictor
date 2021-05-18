# Stackoverflow Tag Predictor

## VIDEO DEMO: https://youtu.be/ToN2-lN5FAM

### Problem statement: 
* Whenever an new question arrive on stackoverflow then we need to predict tags about that question based on the question content.

### About Dataset
To download dataset: https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction/data?select=Train.zip
* **Train.csv:** Have 4 dimensions: Id,Title,Body,Tags.
    * Id: Question id
    * Title: Title of the question
    * Body: Where we have actual explaination of the question
    * Tags: Tags related to that question
* **Test.csv:** contains the same columns but without the Tags, we need to predict them.
* **Size of Train.csv:** 6.75GB --> Compressed form 2.19GB
* **Size of Test.csv:** 2GB --> Compressed form 725.1MB
* **Number of rows in Train.csv:** 6034195 or 6.03 Millions

Actually this is a quite large dataset to work on a small machine.

This project is not have model.py file because i did it in the ipynb and save the models with 100k Datapoints due lack of memory<br>
To download Model: https://drive.google.com/file/d/1JBUZqcDuzp1uxK2t1Od4BBSnb3AZvatZ/view?usp=sharing<br>
To Download Vectorizer: https://drive.google.com/file/d/1vgMJ9skOE7ydpS6nRKk0w4ZAaEhETCfY/view?usp=sharing<br>
To download top 5500 Tag list: https://drive.google.com/file/d/1vObP_nooSik4RQklx9T-CjzqDSCw-6W9/view?usp=sharing<br>

To run this application first we need to download all three files which links are given above then put them into the same folder then run python app.py
