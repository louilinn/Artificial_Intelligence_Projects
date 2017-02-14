# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 09:56:02 2017

@author: Louise
"""


#import arff
#attr_dict = arff.load(open('restaurant_example2.arff', 'r'))
#attr = attr_dict.attributes

import csv
column_names = ['alt', 'bar', 'fri', 'hun', 'pat', 'price', 'rain', 'res',
                'type', 'est', 'will_wait']
attributes = column_names[:-1]

dataset = list(csv.DictReader(open('restaurant_example.csv'),
fieldnames=column_names))

import copy

def extrect_feats(dataset, class_name):
    X_dict = copy.deepcopy(dataset)
    y_symbols = [obs.pop(class_name,None) for obs in X_dict]
    return X_dict, y_symbols
    
X_dict, y_symbols =  extrect_feats(dataset, 'will_wait')

y = [0 if symb == 'No' else 1 for symb in y_symbols]

from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer(sparse=False) # Should be true
X = vec.fit_transform(X_dict) # y values not included

features = vec.get_feature_names()
param = vec.get_params(deep=True)

from decision_tree import decision_tree_learning 
# DECISION TREE BUILDING

decision_tree_learning(X, attributes, X, features, y_symbols)

        

        
#root = Node()
 
 #   def printme(self):
  #      print(self.value)
   #     for elements in self.children:
    #        sys.stdout.write('    ')           #print('    ')
     #       child.printme()

