# COMP-3710 Final Project - Medical Diagnosis System
## Submitted By: Group 10 - Saffa Alvi, Nour ElKott, Salwa Mohamed 

## Introduction
This program accepts user symptoms as an input and returns the probability of them having diseases from the dataset based on their symptoms.
The Decision Tree and Naive Bayes algorithms were used to predict the diseases and probabilities that the symptoms indicated.
The dataset used to obtain the information on diseases and symptoms can be found here: https://impact.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/index.html.
A new dataset was created using the information in the original dataset so symptoms associated with the disease will have a value of 1 and symptoms not associated with the disease will have a value of 0. This dataset, [diseases.csv](https://github.com/jumana-s/3710-Project/blob/main/disease.csv), was then used to train the decision tree and naive bayes models.

## Deployment
This program is deployed and available to test at: https://disease-checker.herokuapp.com/

## Implementation 
**Naive Bayes**
The Naive Bayes algorithm implementation includes the following files:
- [NaiveBayes.py](https://github.com/jumana-s/3710-Project/blob/main/NaiveBayes.py): Contains the algorithm that trains the model with the Bernoulli Classifier, predicts and returns the diseases and probability.
```
dataset = pd.read_csv('disease.csv')
X = dataset.drop(columns=['disease'])
y = dataset['disease']

model = BernoulliNB()
model.fit(X, y)

result = model.predict(symptoms_list[0:1])[0]
prob = pd.DataFrame(model.predict_proba(symptoms_list[0:1]), columns=model.classes_)
```
- [Convert.py](https://github.com/jumana-s/3710-Project/blob/main/Convert.py): Used to convert the user symptom input into a valid list of 0s and 1s to pass into the NaiveBayes function.

The two files above have corresponding Jupyter Notebook files, (NaiveBayes.ipynb)[https://github.com/jumana-s/3710-Project/blob/main/NaiveBayes.ipynb] and (Convert.ipynb)[https://github.com/jumana-s/3710-Project/blob/main/Convert.ipynb], that provide more detail with sample outputs.

**Decision Tree**

**User Interface**
