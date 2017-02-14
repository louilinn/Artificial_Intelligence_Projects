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

def dtl(examples,attributes,parent_examples,all_features):
    if examples.isEmpty():
        return plurality(parent_examples)
    elif attributes.isEmpty():
        return plurality(examples)
    else :
        index = 0
        attr = attributes[index] # attribut # replace with importance function
        node = Node(None, examples, A, [], None)
        attr_features = []
        for f in all_features:
            if attr in f:
                attr_features.append(f)
        for attr_f in attr_features: # t.ex. ['alt=No', 'alt=Yes']
            example_attr_values = examples[:][index] # all values of current feature
            exs_with_attr_f = []                       # init
            nbr_of_exs = example_attr_values.length
            for i in range(1, bbr_of_exs):
                val = example_attr_values[i]             # each val
                if val in attr_f:
                    exc_with_attr_f.append[examples[i]]
                    #end
                
                
            
                
        

class Node(object):
    def __init__(self, val, el, attr, childs, par):
        self.value = val    # attribute value  / answer
        self.elements = el # array
        self.split_attr = attr
        self.children = childs # array
        self.parent = par
        
        
#root = Node()
 
 #   def printme(self):
  #      print(self.value)
   #     for elements in self.children:
    #        sys.stdout.write('    ')           #print('    ')
     #       child.printme()

