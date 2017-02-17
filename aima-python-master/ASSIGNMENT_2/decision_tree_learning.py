# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:26:21 2017

@author: Louise, Miriam
"""
from math import log

# class for node in tree
class Node(object) :
    def __init__(self, value, el, attr, childs, par, indent):
        self.value = value    # attribute value  / answer
        self.elements = el # array
        self.split_attr = attr
        self.children = childs # array
        self.parent = par # unnec
        self.indent = indent
        
    def stringme(self):
        #node_string = ''
        if (self.value is not None): # unnec
            #print(self.parent.split_attr,'=',self.value,':')
            #node_string = '    ', self.value,': '
            print(self.indent, self.value,': ')
        # print result conclusion about waiting
        #children_string = ''
        for child in self.children:
            #print('    ')           #print('    ') sys.stdout.write
            #children_string = children_string, child.stringme()
            child.printme(self.indent)
       # return node_string, children_string
    def printme(self, indent):
        self.stringme()
            
class SimpleNode(Node):
    def __init__(self, label):
        self.label = label
    def printme(self, indent):
        print(indent, self.label) 

        

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
        print('no examples of this')
        return plurality_value(parent_examples, classifications) 
        # loop elements and put together parent_elements

    elif has_same_classification(examples, classifications):
        print('all have same classification')# + classifications[examples[0]])
        if classifications[examples[0]] == 1: # same for any example, take first
            print('    Yes')            
            return SimpleNode('Yes')
        else:
            print('    Yes')  
            return SimpleNode('No')
   
    elif len(attributes) == 0: #isEmpty
        print('run out of attributes to filter on - plurality value:', plurality_value(examples, classifications))
        
        return plurality_value(examples, classifications)

    else:
        print('recursive case going to next level')
        a_max = attributes[0]
        for a in attributes:
            importance_a = importance(a, examples, features, feature_matrix, classifications)
            importance_a_max = importance(a_max, examples, features, feature_matrix, classifications)
            if importance_a > importance_a_max:
                a_max = a
        attr = a_max
        # attribut # replace with importance function
        # initialize a node / root of tree for inparameters
        tree = Node(label, examples, attr, [], None, '') 
                # (value, elements, attr, children, parents):
        
        # finding all features related to attribute for current examples
        feature_cols = []  # possible values          
        for f in features:
            if attr in f:
                feature_column = features.index(f)
                feature_cols.append(feature_column) 
        #attributes.remove(attr) # for sending to subtree            
        # for each value of attribute attr
        for column in feature_cols: # column among relevant feature columns
            # extract a vector with 0/1 for a feature, for current examples
            examples_features = feature_matrix[examples,column]
            # init of vector with examples having 1 for the feature            
            exs_with_f = []                    
            nbr_of_exs = examples_features.shape[0]
            
            # finding the examples that have the feature
            for i in range(0, nbr_of_exs):
                feature_value = examples_features[i] # 0 or 1
                if feature_value == 1:
                    exs_with_f.append(examples[i])
            print(features[column])
            print(exs_with_f)
            #print(attributes)
            # recursive
                    # subtree will eventually get classification value
            remaining_attributes = []            
            for i in attributes:
                if (i != attr):
                    remaining_attributes.append(i)
            #print(remaining_attributes)

            subtree = decision_tree_learning_(exs_with_f, remaining_attributes, examples, attr, label,
                                            features, classifications, feature_matrix)
            if ( isinstance(subtree, Node) ):
                subtree.value = features[column] # current feature 
                tree.children.append(subtree) 
                subtree.parent = tree
                subtree.split_attr = attr
                subtree.indent = (subtree.parent.indent, '    ')
                
            # then next feature
            #tree.printme('')
            print()
        
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
    if (true >= false):
        return SimpleNode('Yes')
    else:
        return SimpleNode('No')

# unclear so far
def importance(attr, exs, features, feature_matrix, classs):
    rel_feats = feature_matrix[exs,:]
    rel_class = []
    for i in exs:
        rel_class.append(classs[i])
    
    feature_cols = []  # possible values          
    for f in features:
        if attr in f:
            feature_column = features.index(f)
            feature_cols.append(feature_column) 
    gain = 1
    for col in feature_cols:
        R = ratio_vec(rel_feats[:,col])*B_func(ratio_vec(rel_class))
        gain = gain - R
    return gain;   
   
def ratio_vec(bin_vec):
    #print('ratio', sum(bin_vec)/len(bin_vec))
    return sum(bin_vec)/len(bin_vec)

def B_func(q):
    if q == 0:
        return 0
    if q == 1:
        return 0
    return - (q * log(q,2) + (1-q) * log(1-q,2))

# if all elements in example are classified the same, return true
def has_same_classification(examples, y_symbols):
    first_index = examples[0]
    first_classification = y_symbols[first_index]
    for ex_i in examples:
        if y_symbols[ex_i] != first_classification:
            return False
    return True
