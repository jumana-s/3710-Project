import pandas as pd
import numpy as np
from sklearn.naive_bayes import BernoulliNB
from Convert import to_valid_list

def NaiveBayes(user_symptoms, disease):
    
    symptoms = to_valid_list(user_symptoms)
    symptoms_list = [symptoms]
    # load the datasets
    # training dataset (includes all the data for all the diseases)
    dataset = pd.read_csv('disease.csv')

    # X = features of dataset
    X = dataset.drop(columns=['disease'])
    # y = target (classes) of dataset
    y = dataset['disease']

    model = BernoulliNB()
    model.fit(X, y)
    
    result = model.predict(symptoms_list[0:1])[0]
    prob = pd.DataFrame(model.predict_proba(symptoms_list[0:1]), columns=model.classes_)
    output = ""
    
    if disease == "All diseases":
        pred_disease = "Based on the symptoms, the predicted disease is {}. The probability of your symptoms indicating {} is {}%".format(result, result, prob.at[0,result]*100)
        output = pred_disease
    else:
        specific_disease = "The probability of your symptoms indicating {} is {}%".format(disease,prob.at[0,disease]*100)
        output = specific_disease
    
    return output
