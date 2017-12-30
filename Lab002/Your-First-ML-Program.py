# MY FIRST MACHINE LEARNING PROGRAM
# This is a 6 line-code Machine Learning Program

# import the Decision Tree classifier from the sklearn library
from sklearn import tree

# FIRST STEP: COLLECT TRAINING DATA
#====================================================================
# set features learned
features = [[130,1], [140,1], [150,0], [170,0]]
# set labels to those features
labels = [0,0,1,1]

# SECOND STEP: TRAIN THE CLASSIFIER
#====================================================================
# build an empty variable for the Decision Tree clasifier
clf = tree.DecisionTreeClassifier()
# find patterns in our training data (features and labels)
clf = clf.fit(features,labels)

# THIRD STEP: MAKE PREDICTIONS
#====================================================================
# call the Machine Learning algorithm for making a prediction
print(clf.predict([[160,0]]))

