""" 
---------------------------------------------------------------------------------------------
IMPORT INFORMATION
---------------------------------------------------------------------------------------------
"""



""" 
---------------------------------------------------------------------------------------------
DEFINE THE DATASET (WILL BE TRANSFERRED TO A FILE FOR LARGER DATASET)
---------------------------------------------------------------------------------------------
"""

trainingData = [ # this dataset contains 15 items, alternating between Red, Blue, or Green Circles and Squares
    ['Red', 'Square'],
    ['Red', 'Circle'],
    ['Red', 'Square'],
    ['Red', 'Square'],
    ['Blue', 'Square'],
    ['Blue', 'Square'],
    ['Red', 'Circle'],
    ['Blue', 'Circle'],
    ['Green', 'Square'],
    ['Green', 'Square'],
    ['Red', 'Square'],
    ['Green', 'Circle'],
    ['Red', 'Circle'],
    ['Green', 'Square'],
    ['Blue', 'Square']
]

header = ["colour", "shape"] # difne columns in dataset

""" 
---------------------------------------------------------------------------------------------
FUNCTION TO DETERMINE UNIQUE VALUES IN A CURRENT COLUMN
---------------------------------------------------------------------------------------------
"""
def uniqueValue(rows, col):                 
    return set([row[col] for row in rows])  # find and return the unique values for a column in the dataset


""" 
---------------------------------------------------------------------------------------------
FUNCTION TO CALCULATE NUMBER OF TIMES A LABEL IS REPEATED IN THE DATASET
---------------------------------------------------------------------------------------------
"""
def classCounts(rows): 
    counts = {}                     # a dictionary of a label is set to count
    for row in rows:                # for each row in the dataset:
        label = row[-1]             # begin at the last row, saving the label names
        if label not in counts:     # if the label is not already saved in the counts dictionary:
            counts[label] = 0       # save current label in index 0 of counts
        counts[label] += 1          # increase counter
    return counts                   # return the dictionary

""" 
---------------------------------------------------------------------------------------------
FUNCTION TO DETERMINE IF INPUT IS AN INTEGER OR A FLOAT
---------------------------------------------------------------------------------------------
"""
def isNumeric(value): 
    return isinstance(value, int) or isinstance(value,float) # true if value is an integer or a float

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
        if isNumeric(currentValue):             # if we are checking for a numeric value (is not required if dataset does not contain any numbers):
            return currentValue >= self.value   # look for >= (can be changed depending on dataset)
        else:                                   # no numbers:
            return currentValue == self.value   # check for equivalence
    
    """ 
    ---------------------------------------------------------------------------------------------
    HELPER METHOD TO PRINT THE CURRENT QUESTION TO THE USER
    ---------------------------------------------------------------------------------------------
    """
    def __repr__(self): # helper method to print current question to the user
        condition = "==" # condition to be printed to the user
        if isNumeric(self.value): # if the value is numeric
            condition = ">=" # change condition to >=
        return "Is %s %s %s?" % (header[self.column], condition, str(self.value)) # print the current question to the user

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
            rowsTrue.append(row)        # satisfies, so add the row to rowsTrue list
        else:                           # if the condition defined in the question does not match the info in the current row:
            rowsFalse.append(row)       # does not satisfy, so add the row to rowsFalse list
    return rowsTrue, rowsFalse          # return both lists

rowsTrue, rowsFalse = partition(trainingData, Question(0, 'Red')) # get rowsTrue returned from partition() given rows and question

""" 
---------------------------------------------------------------------------------------------
METHOD TO CALCULATE GINI VALUES
---------------------------------------------------------------------------------------------
"""
def giniImpurity(rows): 
    counts = classCounts(rows)                                  # count num times rows is repeated in the dataset by calling classCounts()
    impurity = 1                                                # set default impurity to 1
    for label in counts:                                        # for each label in counts
        probabilityOfLabel = counts[label] / float(len(rows))   # set probability of label being mistaken to (num label repeated / num rows)
        impurity -= probabilityOfLabel**2                       # set impurity
    return impurity

""" 
---------------------------------------------------------------------------------------------
METHOD FOR GINI FORMULA
---------------------------------------------------------------------------------------------
"""
def giniFormula(left, right, uncertainty):
    p = float(len(left)) / (len(left) + len(right))
    return (uncertainty - p*giniImpurity(left) - ((1 - p) * giniImpurity(right)))

uncertainty = giniImpurity(trainingData)
rowsTrue, rowsFalse = partition(trainingData, Question(0, 'Red'))

""" 
---------------------------------------------------------------------------------------------
METHOD TO FIND BEST SPLIT IN THE DATASET
---------------------------------------------------------------------------------------------
"""
def bestSplit(rows):
    bestInformationInput = 0                                # to keep track of the best information gain from gini formula
    bestQuestion = None                                     # to keep track of the next best question to ask

    uncertainty = giniImpurity(rows)                        # to calculate the gini impurity
    numColumns = len(rows[0]) - 1                           # to get the number of columns

    for column in range(numColumns):
        values = set([row[column] for row in rows])         # to set the unique values in the column
        for value in values:                                # for each value in the set of values from column:
            question = Question(column, value)              # create a new question

            rowsTrue, rowsFalse = partition(rows, question) # determine satisfactory and non-satisfactory rows

            if len(rowsTrue) == 0 or len(rowsFalse) == 0:   # if either lists are empty:
                continue                                    # back to beginning of for loop

            formulaResult = giniFormula(rowsTrue, rowsFalse, uncertainty)

            if formulaResult >= bestInformationInput:
                bestInformationInput, bestQuestion = formulaResult, question
    
    return bestInformationInput, bestQuestion

bestInformationInput, bestQuestion = bestSplit(trainingData)

""" 
---------------------------------------------------------------------------------------------
PRINT TO USER
---------------------------------------------------------------------------------------------
"""

print("\nPRINT TRAINING SET:")
print("------------------------------------------------")
print(trainingData)

print("\nPRINT ALL UNIQUE VALUES IN THE SHAPE CATEGORY:")
print("------------------------------------------------")
print(uniqueValue(trainingData, 0))

print("\nPRINT REPEATED SHAPES:")
print("------------------------------------------------")
print(classCounts(trainingData))

print("\nCHECK IF SOMETHING IS NUMERIC (in this case, 'Red'):")
print("------------------------------------------------")
print(isNumeric("Red"))

q = Question(0, "Red")
example = trainingData[0]

print("\nPRINT CURRENT QUESTION BEING ASKED:")
print("------------------------------------------------")
print( q, example,":", q.match(example))

print("\nPRINT ROWS THAT SATISFY CONDITON:")
print("------------------------------------------------")
print(rowsTrue) # print rows that satisfy conditions
print("\nPRINT ROWS THAT DO NOT SATISFY CONDITON:")
print("------------------------------------------------")
print(rowsFalse) # print rows that do not satisfy conditions

pure = [['Red'], ['Red']]
print("\nPRINT PROBABILITY THAT CLASSIFICATION WILL RESULT IN ERROR (red, red):")
print("------------------------------------------------")
print((giniImpurity(pure)*100),"%") # prints 0.0 %

smallMix = [['Red'], ['Blue']]
print("\nPRINT PROBABILITY THAT CLASSIFICATION WILL RESULT IN ERROR (red, blue):")
print("------------------------------------------------")
print((giniImpurity(smallMix)*100),"%") # prints 50.0% (50% chance of misclassifying a random example from the dataset)

bigMix = [['Red'], ['Blue'], ['Green']]
print("\nPRINT PROBABILITY THAT CLASSIFICATION WILL RESULT IN ERROR (red, blue, green):")
print("------------------------------------------------")
print((giniImpurity(bigMix)*100),"%") # prints 66.6666%

print("\nPRINT GINI IMPURITY OF DATA SET:")
print("------------------------------------------------")
print((uncertainty)*100,"%")
print("\nPRINT ROWS THAT SATISFY THE CONDITION:")
print("------------------------------------------------")
print(rowsTrue)
print("\nPRINT ROWS THAT DO NOT SATISFY THE CONDITION:")
print("------------------------------------------------")
print(rowsFalse)

print("\nUNCERTAINTY WHEN PARTITIONING RED:")
print("------------------------------------------------")
print(giniFormula(rowsTrue, rowsFalse, uncertainty)*100, "%")

print("\nPRINT CURRENT QUESTION:")
print("------------------------------------------------")
print(bestQuestion)
print("\nPRINT RESULT FROM QUESTION:")
print("------------------------------------------------")
print((bestInformationInput)*100, "%")


