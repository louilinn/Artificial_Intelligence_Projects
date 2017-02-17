# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:26:21 2017

@author: Louise
"""

# class for node in tree
class Node(object) :
    def __init__(self, value, el, attr, childs, par):
        self.value = value    # attribute value  / answer
        self.elements = el # array
        self.split_attr = attr
        self.children = childs # array
        self.parent = par
        
    def printme(self):
        print('Node')
        if (self.parent is not None):
            print(self.parent.attr + '=' + self.value +':')
         # print result conclusion about waiting
        for child in self.children:
            print('    ')           #print('    ') sys.stdout.write
            child.printme()            
            
class SimpleNode(Node):
    def __init__(self, label):
        self.label = label
    def printme(self):
        print(self.label) 
        

# building an (optimal) tree
def decision_tree_learning_(examples, attributes, parent_examples, label, p_label,
                           features, classifications, feature_matrix):
        # input
    # examples = indices of examples remaining (array of ints)
    # attributes = attributes remaining for rest of tree (array of strings)
    # parent_examples = indices of examples of parent node (array of ints)

        # constant globals
    # features = all the possible features of any example (array of string e.g. 'bar = No')
    # feature_matrix = feature boolean matrix with 0 / 1 for row example, column feature
    # classification = an array of int 0 or 1 (y-labels) (e.g. will_wait, in y_symbols)

    if len(examples) == 0:
        return plurality_value(parent_examples, classifications) 
        # loop elements and put together parent_elements

    elif has_same_classification(examples, classifications):
        print(classifications[examples[0]])
        if classifications[examples[0]] == 1: # same for any example, take first
            return SimpleNode('Yes')
        else:
            return SimpleNode('No')
   
    elif len(attributes) == 0: #isEmpty
        return plurality_value(examples, classifications)

    else:
        a_max = attributes[0]
        for a in attributes:
            if importance(a) > importance(a_max):
                a_max = a
        attr = a_max
        # attribut # replace with importance function
        attributes.remove(attr) # for sending to subtree
        # initialize a node / root of tree for inparameters
        tree = Node(label, examples, attr, [], None) 
                # (value, elements, attr, children, parents):
        
        # finding all features related to attribute for current examples
        feature_cols = []  # possible values          
        for f in features:
            if attr in f:
                feature_column = features.index(f)
                feature_cols.append(feature_column) 
                    
        # for each value of attribute attr
        for column in feature_cols: # column among relevant feature columns
            # extract a vector with 0/1 for a feature, for current examples
            examples_features = feature_matrix[examples,column]
            # init of vector with examples having 1 for the feature            
            exs_with_f = []                    
            nbr_of_exs = examples_features.shape[0]
            
            # finding the examples that have the feature
            for i in range(1, nbr_of_exs):
                feature_value = examples_features[i] # 0 or 1
                if feature_value == 1:
                    exs_with_f.append(examples[i])
                    
            # recursive
                    # subtree will eventually get classification value
            subtree = decision_tree_learning_(exs_with_f, attributes, examples, attr, label,
                                            features, classifications, feature_matrix)
            if ( isinstance(subtree, Node) ):
                subtree.value = features[column] # current feature 
                tree.children.append(subtree) 
            # then next feature
            
        return tree
                    #end
        # finish building node and return it
                
# unclear so far
def plurality_value(examples, classifications):
    true = 0
    false = 0
    for ex_i in examples:
        if classifications[ex_i] == 1:
            true += 1
        else:
            false += 1
            
    if (true > false):
        return SimpleNode('Yes')
    else:
        return SimpleNode('No')

# unclear so far
def importance(attribute):
    return 0;   
   
# if all elements in example are classified the same, return true
def has_same_classification(examples, y_symbols):
    first_index = examples[0]
    first_classification = y_symbols[first_index]
    for ex_i in examples:
        if y_symbols[ex_i] != first_classification:
            return False
    return True
