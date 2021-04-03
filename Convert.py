import numpy as np
import pandas as pd

diseases = pd.read_csv('disease.csv')

columns = list(diseases.columns)[:-1]
#print(columns)

total_sym = len(columns)

def to_valid_list(user_sym_list):
    if type(user_sym)!=list:
        user_sym_list = to_list(user_sym_list)
    valid_list = []
    for i in range (0, total_sym-1):
        if columns[i] in user_sym_list:
            valid_list.append(1)
        else:
            valid_list.append(0)
    return(valid_list)

def to_list(string):
    user_sym_list = user_sym.split(",")
    user_sym_list = [x.strip(' ') for x in user_sym_list]
    return(user_sym_list)

user_sym = 'cough, mass in breast, hypercapnia, orthopnea'
print("ORIGINAL LIST: \n", user_sym, "\n")
new_list = to_valid_list(user_sym)
print("NEW LIST: \n", new_list)

for i in range(0, len(new_list)-1):
    if new_list[i] == 1:
        print(columns[i])
