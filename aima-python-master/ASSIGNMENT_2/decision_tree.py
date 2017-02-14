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
        
class Example(object):
    def __init__(self, index, features):
        self.index = index
        self.features = features
        
def Convert(object):
    def __init__(self, example, index):
        self.ex = example
        self.index = index

# building an (optimal) tree
def decision_tree_learning(examples, attributes, parent_examples, all_features, classifications):
    for i in range(0, examples.size):
       examples[i] = Convert(examples[i], i)    
       
    if examples.size == 0:
        return plurality_value(parent_examples)
    elif has_same_classification(examples, classifications):
        return examples[0].value
    elif attributes.isEmpty():
        return plurality_value(examples)
    else :
        index = 0
        attr = attributes[index] # attribut # replace with importance function
        node = Node(None, examples, attr, [], None)
        attr_features = []
        for f in all_features:
            if attr in f:
                attr_features.append(f)
        for attr_f in attr_features: # t.ex. ['alt=No', 'alt=Yes']
            example_attr_values = examples[:][index] # all values of current feature
            exs_with_attr_f = []                       # init
            nbr_of_exs = example_attr_values.length
            for i in range(1, nbr_of_exs):
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
    classification = y_symbols[index]
    for ex in examples:
        if y_symbols[ex.index] != classification:
            return False
    return True
