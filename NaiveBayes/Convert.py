import numpy as np
import pandas as pd

diseases = pd.read_csv("disease.csv")
columns = list(diseases.columns)[:-1]

total_sym = len(columns)

def to_valid_list(user_sym_list):
    if type(user_sym_list) != list:
        user_sym_list = to_list(user_sym_list)
    valid_list = []
    for i in range (0, total_sym):
        if columns[i] in user_sym_list:
            valid_list.append(1)
        else:
            valid_list.append(0)
    return(valid_list)

def to_list(string):
    user_sym_list = string.split(",")
    user_sym_list = [x.strip(' ') for x in user_sym_list]
    return(user_sym_list)
