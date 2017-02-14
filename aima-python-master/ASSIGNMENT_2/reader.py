# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:42:20 2017

@author: Louise
"""

import arff
X_dict = arff.load(open('restaurant_example2.arff', 'r'))

dataset = list(X_dict)

print(dataset)

from sklearn.feature_extraction import DictVectorizer

vec = DictVectorizer(sparse=True) # Should be true
#vec.get_feature_names()
X = vec.fit_transform(X_dict)
