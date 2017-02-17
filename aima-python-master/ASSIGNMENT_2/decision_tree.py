# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:26:21 2017

@author: Louise
"""

# class for node in tree
class Node(object) :
    def __init__(self, val, el, attr, childs, par):
        self.value = val    # attribute value  / answer
        self.elements = el # array
        self.split_attr = attr
        self.children = childs # array
        self.parent = par
        
class Example(object): # kanske bättre med en dictionary key:index feature värde
    def __init__(self, index, features):
        self.index = index
        self.features = features
        
def convert(example, index):
    return Example(index, example)

# building an (optimal) tree
def decision_tree_learning(examples, attributes, parent_examples, all_features, classifications): 
       
       if examples.size == 0:
           return plurality_value(parent_examples) # loop elements and put together parent_elements
   
       elif has_same_classification(examples, classifications):
           index_for_one_example = examples[0].index
           return classifications[index_for_one_example] 

        elif attributes.isEmpty():
            return plurality_value(examples)
            
        else :
            index = 0
            attr = attributes[index] # attribut # replace with importance function
            node = Node(None, examples, attr, [], None)
            feature_cols = []  # possible values
            
            for f in all_features:
                if attr in f:
                    feature_column = all_features.index(f)
                    feature_cols.append(feature_column) 
                    
            for column in feature_cols: # column among relevant feature columns
               examples_features = examples[:,column] # all values of current feature
               exs_with_f = []                    # init
               nbr_of_exs = examples_features.length
               
               for i in range(1, nbr_of_exs):
                   feature_value = examples_features[i]
                   if feature_value == 1:
                       exs_with_f.append(example[i])
                  
                  val = example_attr_values[i]             # each val
                   if val in attr_f:
                       exs_with_attr_f.append[examples[i]]
                    #end
        # finish building node and return it
                
# unclear so far
def plurality_value(parent_examples):
    return 0;
   
# if all elements in example are classified the same, return true
def has_same_classification(examples, y_symbols):
    index = examples[0].index
    first_classification = y_symbols[index]
    for ex in examples:
        if y_symbols[ex.index] != first_classification:
            return False
    return True
