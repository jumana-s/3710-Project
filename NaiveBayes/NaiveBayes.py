import pandas as pd
import numpy as np
from sklearn.naive_bayes import BernoulliNB

# to turn user symptoms into a valid list of 0s and 1s
from Convert import to_valid_list

def NaiveBayes(user_symptoms, disease):
    
    symptoms = to_valid_list(user_symptoms)
    symptoms_list = [symptoms]
    # load the datasets
    # training dataset (includes all the data for all the diseases)
    dataset = pd.read_csv("../disease.csv")

    # X = features of dataset
    X = dataset.drop(columns=['disease'])
    # y = target (classes) of dataset
    y = dataset['disease']

    # fit the model with the dataset using the Bernoulli classifier
    model = BernoulliNB()
    model.fit(X, y)
    
    # predict the target class (disease) for the user symptoms
    result = model.predict(symptoms_list[0:1])[0]
    # to get probabilities of all classes (diseases) for the user symptoms
    # used to get probability of the symptoms indicating a disease
    prob = pd.DataFrame(model.predict_proba(symptoms_list[0:1]), columns=model.classes_)

    # return value
    output = ""
    
    # return disease with highest probability and the probability of that disease
    if disease == "All diseases":
        pred_disease = "Based on the symptoms, the predicted disease is {}. The probability of your symptoms indicating {} is {}%".format(result, result, prob.at[0,result]*100)
        output = pred_disease
    # return probability of specific disease selected by user
    else:
        specific_disease = "The probability of your symptoms indicating {} is {}%".format(disease,prob.at[0,disease]*100)
        output = specific_disease
    
    return output

