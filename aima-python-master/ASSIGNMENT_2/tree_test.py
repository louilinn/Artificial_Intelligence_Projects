# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:19:06 2017

@author: Louise
"""
import sys

class Tree(object):
    def __init__(self):
        self.children = []
        self.data = None
        
    def printme(self):
        print(self.data)
        for child in self.children:
            sys.stdout.write('    ')           #print('    ')
            child.printme()

root = Tree()
root.data = 'alt'
root.children = [Tree(), Tree()]
root.children[0].data = 'bar'
root.children[1].data = 'hun'
root.children[0].children = [Tree()]
root.children[0].children[0].data = 'Miriam'

root.printme()

