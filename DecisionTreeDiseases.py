
import csv

inputSymptoms = ["cough", "fever"]

with open('disease.csv', newline='') as f: # read data in trainingData.csv
    reader = csv.reader(f) # define reader
    trainingData = list(reader) # set trainingData list to everything read by reader

header = [  "cough","fever","shortness of breath","pain chest","diarrhea","vomiting",
            "unresponsiveness","asthenia","dyspnea","pain abdominal","vertigo",
            "apyrexial","sweat","nausea","dizziness","fall","syncope","palpitation",
            "angina pectoris","hypokinesia","pressure chest","dyspnea on exertion",
            "orthopnea","chest tightness","jugular venous distention","rale,wheezing",
            "pleuritic pain","distress respiratory","sputum purulent","hypoxemia",
            "hypercapnia","sleeplessness","swelling","atypia","distended abdomen",
            "pain","stool color yellow","systolic murmur","frail","hypoproteinemia",
            "fatigue","haemorrhage","colic abdominal","ambidexterity","numbness",
            "splenomegaly","clonus","egophony","facial paresis","aphagia",
            "muscle twitch","paralyse","low back pain","charleyhorse","paraparesis",
            "gravida 0","mass in breast","tumor cell invasion","metastatic lesion",
            "pain neck","lung nodule","bleeding of vagina","hyperkalemia","bradycardia",
            "cicatrisation","mediastinal shift","impaired cognition","snuffle",
            "hepatosplenomegaly","headache","guaiac positive","decereased body weight",
            "sore to touch"] # define columns in dataset

cough = "0"
fever = "0"
shortness_of_breath = "0"
pain_chest = "0"
diarrhea = "0"
vomiting = "0"
unresponsiveness = "0"
asthenia = "0"
dyspnea = "0"
pain_abdominal = "0"
vertigo = "0"
apyrexial = "0"
sweat = "0"
nausea = "0"
dizziness = "0"
fall = "0"
syncope = "0"
palpitation = "0"
angina_pectoris = "0"
hypokinesia = "0"
pressure_chest = "0"
chest_discomfort = "0"
orthopnea = "0"
chest_tightness = "0"
jugular_venous_distention = "0"
rale = "0"
wheezing = "0"
pleuritic_pain = "0"
distress_respiratory = "0"
speech_slurred = "0"
hypercapnia = "0"
sleeplessness = "0"
swelling = "0"
atypia = "0"
hypotension = "0"
pain = "0"
stool_color_yellow = "0"
systolic_murmur = "0"
frail = "0"
hypoproteinemia = "0"
fatigue = "0"
haemorrhage = "0"
facial_paresis = "0"
ambidexterity = "0"
numbness = "0"
splenomegaly = "0"
clonus = "0"
egophony = "0"
st_segment_elevation = "0"
arthralgia = "0"
muscle_twitch = "0"
paralyse = "0"
low_back_pain = "0"
charleyhorse = "0"
paraparesis = "0"
gravida_0 = "0"
mass_in_breast = "0"
tumor_cell_invasion = "0"
metastatic_lesion = "0"
rhonchus = "0"
lung_nodule = "0"
bleeding_of_vagina = "0"
hyperkalemia = "0"
bradycardia = "0"
cicatrisation = "0"
mediastinal_shift = "0"
impaired_cognition = "0"
snuffle = "0"
chill = "0"
headache = "0"
guaiac_positive = "0"
decreased_body_weight = "0"
sore_to_touch = "0"

if "cough" in inputSymptoms :
    cough = "1"
if "fever" in inputSymptoms :
    fever = "1"
if "shortness of breath" in inputSymptoms :
    shortness_of_breath = "1"
if "pain chest" in inputSymptoms:
    pain_chest = "1"
if "diarrhea" in inputSymptoms:
    diarrhea = "1"
if "vomiting" in inputSymptoms:
    vomiting = "1"
if "unresponsiveness" in inputSymptoms:
    unresponsiveness = "1"
if "asthenia" in inputSymptoms:
    asthenia = "1"
if "dyspnea" in inputSymptoms:
    dyspnea = "1"
if "pain abdominal" in inputSymptoms:
    pain_abdominal = "1"
if "vertigo" in inputSymptoms:
    vertigo = "1"
if "apyrexial" in inputSymptoms:
    apyrexial = "1"
if "sweat" in inputSymptoms:
    sweat = "1"
if "nausea" in inputSymptoms:
    nausea = "1"
if "dizziness" in inputSymptoms:
    dizziness = "1"
if "fall" in inputSymptoms:
    fall = "1"
if "syncope" in inputSymptoms:
    syncope = "1"
if "palpitation" in inputSymptoms:
    palpitation = "1"
if "angina pectoris" in inputSymptoms:
    angina_pectoris = "1"
if "hypokinesia" in inputSymptoms:
    hypokinesia = "1"
if "pressure chest" in inputSymptoms:
    pressure_chest = "1"
if "chest discomfort" in inputSymptoms:
    chest_discomfort  = "1"
if "orthopnea" in inputSymptoms:
    orthopnea = "1"
if "chest tightness" in inputSymptoms:
    chest_tightness = "1"
if "jugular venous distention" in inputSymptoms:
    jugular_venous_distention = "1"
if "rale" in inputSymptoms:
    rale = "1"
if "wheezing" in inputSymptoms:
    wheezing = "1"
if "pleuritic pain" in inputSymptoms:
    pleuritic_pain = "1"
if "distress respiratory" in inputSymptoms:
    distress_respiratory = "1"
if "speech slurred" in inputSymptoms:
    speech_slurred = "1"
if "hypercapnia" in inputSymptoms:
    hypercapnia = "1"
if "sleeplessness" in inputSymptoms:
    sleeplessness = "1"
if "swelling" in inputSymptoms:
    swelling = "1"
if "atypia" in inputSymptoms:
    atypia = "1"
if "hypotension" in inputSymptoms:
    hypotension = "1"
if "pain" in inputSymptoms:
    pain = "1"
if "stool color yellow" in inputSymptoms:
    stool_color_yellow = "1"
if "systolic murmur" in inputSymptoms:
    systolic_murmur = "1"
if "frail" in inputSymptoms:
    frail = "1"
if "hypoproteinemia" in inputSymptoms:
    hypoproteinemia = "1"
if "fatigue" in inputSymptoms:
    fatigue = "1"
if "haemorrhage" in inputSymptoms:
    haemorrhage = "1"
if "facial paresis" in inputSymptoms:
    facial_paresis = "1"
if "ambidexterity" in inputSymptoms:
    ambidexterity = "1"
if "numbness" in inputSymptoms:
    numbness = "1"
if "splenomegaly" in inputSymptoms:
    splenomegaly = "1"
if "clonus" in inputSymptoms:
    clonus = "1"
if "egophony" in inputSymptoms:
    egophony = "1"
if "st segment elevation" in inputSymptoms:
    st_segment_elevation = "1"
if "arthralgia" in inputSymptoms:
    arthralgia = "1"
if "muscle twitch" in inputSymptoms:
    muscle_twitch = "1"
if "paralyse" in inputSymptoms:
    paralyse = "1"
if "low back pain" in inputSymptoms:
    low_back_pain = "1"
if "charleyhorse" in inputSymptoms:
    charleyhorse = "1"
if "paraparesis" in inputSymptoms:
    paraparesis = "1"
if "gravida 0" in inputSymptoms:
    gravida_0 = "1"
if "mass in breast" in inputSymptoms:
    mass_in_breast = "1"
if "tumor cell invasion" in inputSymptoms:
    tumor_cell_invasion = "1"
if "metastatic lesion" in inputSymptoms:
    metastatic_lesion = "1"
if "rhonchus" in inputSymptoms:
    rhonchus = "1"
if "lung nodule" in inputSymptoms:
    lung_nodule = "1"
if "bleeding of vagina" in inputSymptoms:
    bleeding_of_vagina = "1"
if "hyperkalemia" in inputSymptoms:
    hyperkalemia = "1"
if "bradycardia" in inputSymptoms:
    bradycardia = "1"
if "cicatrisation" in inputSymptoms:
    cicatrisation = "1"
if "mediastinal shift" in inputSymptoms:
    mediastinal_shift = "1"
if "impaired cognition" in inputSymptoms:
    impaired_cognition = "1"
if "snuffle" in inputSymptoms:
    snuffle = "1"
if "chill" in inputSymptoms:
    chill = "1"
if "headache" in inputSymptoms:
    headache = "1"
if "guaiac positive" in inputSymptoms:
    guaiac_positive = "1"
if "decreased body weight" in inputSymptoms:
    decreased_body_weight = "1"
if "sore to touch" in inputSymptoms:
    sore_to_touch = "1"


""" 
---------------------------------------------------------------------------------------------
FUNCTION TO CALCULATE NUMBER OF TIMES A LABEL IS REPEATED IN THE DATASET
---------------------------------------------------------------------------------------------
"""
def classCounts(rows):
    disease = ""
    counts = {}                     # a dictionary of a label is set to count
    for row in rows:                # for each row in the dataset:
        disease = disease + "   " + row[-1]
    return str(disease)

""" 
---------------------------------------------------------------------------------------------
CLASS TO CHECK CURRENT QUESTION
---------------------------------------------------------------------------------------------
"""
class Question: # used to partition a dataset, will record the column number (ie. 0 for colour) and a column value (ie Green)
    """ 
    ---------------------------------------------------------------------------------------------
    DEFINE SELF
    ---------------------------------------------------------------------------------------------
    """
    def __init__(self, column, value):
        self.column = column 
        self.value = value
    """ 
    ---------------------------------------------------------------------------------------------
    FUNCTION TO COMPARE AND MATCH ITEMS IN DATASET
    ---------------------------------------------------------------------------------------------
    """
    def match(self, example):
        currentValue = example[self.column]     # set the current value, depending on which column is currently being focused on
        return currentValue == self.value   # check for equivalence
    
    """ 
    ---------------------------------------------------------------------------------------------
    HELPER METHOD TO PRINT THE CURRENT QUESTION TO THE USER
    ---------------------------------------------------------------------------------------------
    """
    def __repr__(self): # helper method to print current question to the user
        condition = "==" # condition to be printed to the user
        return "%s %s %s?" % (header[self.column], condition, str(self.value)) # print the current question to the user

""" 
---------------------------------------------------------------------------------------------
METHOD TO DEFINE PARTITIONS IN THE DATASET
---------------------------------------------------------------------------------------------
"""
def partition(rows, question):          # define partitions in the given dataset
    rowsTrue = []                       # define list to save rows that satisfy the conditions
    rowsFalse = []                      # define list to save rows that do not satisfy the conditions

    for row in rows:                    # for each row in the dataset:
        if question.match(row):         # if the condition defined in the question matches the info in the current row:
            #print(question, "=", row)
            rowsTrue.append(row)        # satisfies, so add the row to rowsTrue list
        else:                           # if the condition defined in the question does not match the info in the current row:
            #print(question, "!=", row)
            rowsFalse.append(row)       # does not satisfy, so add the row to rowsFalse list
    return rowsTrue, rowsFalse          # return both lists


""" 
---------------------------------------------------------------------------------------------
STARTING METHOD
---------------------------------------------------------------------------------------------
"""

def BeginDecisionTree(inputSymptoms, trainingData):
    output = ""
    for x in inputSymptoms:
        print(x)
        if x == 'cough':
            q = Question(0, cough)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))

        if x == 'fever':
            q = Question(1, fever)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'shortness of breath':
            q = Question(2, shortness_of_breath)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))

        if x == 'pain_chest':
            q = Question(3, pain_chest)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'diarrhea':
            q = Question(4, diarrhea)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'vomiting':
            q = Question(5, vomiting)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'unresponsiveness':
            q = Question(6, unresponsiveness)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'asthenia':
            q = Question(7, asthenia)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'dyspnea':
            q = Question(8, dyspnea)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'pain abdominal':
            q = Question(9, pain_abdominal)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'vertigo':
            q = Question(10, vertigo)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'apyrexial':
            q = Question(11, apyrexial)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'sweat':
            q = Question(12, sweat)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'nausea':
            q = Question(13, nausea)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'dizziness':
            q = Question(14, dizziness)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'fall':
            q = Question(15, fall)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'syncope':
            q = Question(16, syncope)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'palpitation':
            q = Question(17, palpitation)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'angina_pectoris':
            q = Question(18, angina_pectoris)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'hypokinesia':
            q = Question(19, hypokinesia)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'pressure chest':
            q = Question(20, pressure_chest)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'chest discomfort':
            q = Question(21, chest_discomfort)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'orthopnea':
            q = Question(22, orthopnea)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'chest tightness':
            q = Question(23, chest_tightness)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'jugular venous distention':
            q = Question(24, jugular_venous_distention)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'rale':
            q = Question(25, rale)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'wheezing':
            q = Question(26, wheezing)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'pleuritic pain':
            q = Question(27, pleuritic_pain)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'distress respiratory':
            q = Question(28, distress_respiratory)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'speech slurred':
            q = Question(29, speech_slurred)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'hypercapnia':
            q = Question(30, hypercapnia)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'sleeplessness':
            q = Question(31, sleeplessness)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'swelling':
            q = Question(32, swelling)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'atypia':
            q = Question(33, atypia)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'hypotension':
            q = Question(34, hypotension)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'pain':
            q = Question(35, pain)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'stool color yellow':
            q = Question(36, stool_color_yellow)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'systolic murmur':
            q = Question(37, systolic_murmur)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'frail':
            q = Question(38, frail)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'hypoproteinemia':
            q = Question(39, hypoproteinemia)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'fatigue':
            q = Question(40, fatigue)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
            

        if x == 'haemorrhage':
            q = Question(41, haemorrhage)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'facial paresis':
            q = Question(42, facial_paresis)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'ambidexterity':
            q = Question(43, ambidexterity)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'numbness':
            q = Question(44, numbness)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'splenomegaly':
            q = Question(45, splenomegaly)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'clonus':
            q = Question(46, clonus)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'egophony':
            q = Question(47, egophony)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'st segment elevation':
            q = Question(48, st_segment_elevation)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'arthralgia':
            q = Question(49, arthralgia)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'muscle_twitch':
            q = Question(50, muscle_twitch)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'paralyse':
            q = Question(51, paralyse)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'low back pain':
            q = Question(52, low_back_pain)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'charleyhorse':
            q = Question(53, charleyhorse)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'paraparesis':
            q = Question(54, paraparesis)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'gravida_0':
            q = Question(55, gravida_0)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'mass_in_breast':
            q = Question(56, mass_in_breast)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'tumor cell invasion':
            q = Question(57, tumor_cell_invasion)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'metastatic lesion':
            q = Question(58, metastatic_lesion)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'rhonchus':
            q = Question(59, rhonchus)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'lung nodule':
            q = Question(60, lung_nodule)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'bleeding of vagina':
            q = Question(61, bleeding_of_vagina)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'hyperkalemia':
            q = Question(62, hyperkalemia)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'bradycardia':
            q = Question(63, bradycardia)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'cicatrisation':
            q = Question(64, cicatrisation)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'mediastinal shift':
            q = Question(65, mediastinal_shift)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'impaired cognition':
            q = Question(66, impaired_cognition)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'snuffle':
            q = Question(67, snuffle)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'chill':
            q = Question(68, chill)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'headache':
            q = Question(69, headache)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'guaiac positive':
            q = Question(70, guaiac_positive)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'decreased body weight':
            q = Question(71, decreased_body_weight)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))


        if x == 'sore to touch':
            q = Question(72, sore_to_touch)
            rowsTrue, rowsFalse = partition(trainingData, q) # get rowsTrue returned from partition() given rows and question
            trainingData = [x for x in trainingData if x not in rowsFalse]
            output = str(classCounts(trainingData))
    
    return "FINAL LIST OF DISEASES: " + output

print(BeginDecisionTree(inputSymptoms, trainingData))

