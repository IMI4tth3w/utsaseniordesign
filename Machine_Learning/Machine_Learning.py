# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 14:01:38 2016

@author: Heath

Install Anaconda Python 2.7
pip install scikit-learn

sudo apt-get install texlive texlive-latex-extra pandoc

"""

#import sklearn #Machine Learning library
from sklearn import tree

#predict apple or orange

#Features = measurements of object, discrimination of object

#Label = what feature combinations make up your object

#Training Data = features and lables in a table
# features = [weight in grams, (1=smooth, 0 = bumpy)]
features = [[140, 1], [130, 1], [150, 0], [170, 0]]

#labels = [(0=apple, 1=orange)]
labels = [0,0,1,1]

#Train your classifier
#decision tree classifier

clf = tree.DecisionTreeClassifier() # tell it what classifier to use
clf = clf.fit(features, labels) # training algorithm find patterns in data

print "0 = apple, 1 = orange"
print clf.predict([[150,0]]) #object is 150 grams and bumpy