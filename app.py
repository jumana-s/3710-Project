from flask import Flask, redirect, url_for, render_template, request
from NaiveBayes import NaiveBayes
from .DecisionTreeAlgorithms.SymptomsDiseases.DecisionTreeDiseases import BeginDecisionTree
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_post():
    symptoms = request.form['symptoms']
    decision = request.form['decision']

    list_s = symptoms.split(',')
    myset = set(list_s)
    mylist = list(myset)

    if request.form['submit_button'] == 'naive':
        result = "<head><link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6\" crossorigin=\"anonymous\"></head><body><div class=\"d-flex align-items-center justify-content-center\" style=\"height: 100vh\"><div class=\"card text-center\"> <div class=\"card-header\">Results</div><div class=\"card-body\"><h5 class=\"card-title\">For "+decision.title()+"</h5><p class=\"card-text\">"+NaiveBayes(symptoms, decision)+"</p><button onclick=\"goBack()\" class=\"btn btn-primary\">Go Back</button></div><div class=\"card-footer text-muted\"></div></div></div><script>function goBack() {window.history.back();}</script></body>"
    else:
        result = "<head><link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6\" crossorigin=\"anonymous\"></head><body><div class=\"d-flex align-items-center justify-content-center\" style=\"height: 100vh\"><div class=\"card text-center\"> <div class=\"card-header\">Results</div><div class=\"card-body\"><h5 class=\"card-title\">For All Diseases</h5><p class=\"card-text\">"+BeginDecisionTree(mylist)+"</p><button onclick=\"goBack()\" class=\"btn btn-primary\">Go Back</button></div><div class=\"card-footer text-muted\"></div></div></div><script>function goBack() {window.history.back();}</script></body>"
    return result

def do_it():
    result  = ""
# for(list.)

if __name__ == "__main__":
    app.run()
