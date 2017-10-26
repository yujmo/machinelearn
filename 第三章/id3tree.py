# -*- coding: utf-8 -*-
from numpy import *
import math
import copy
import pickle
class ID3DTree(object):
    def __init__(self):
        self.tree = {}
        self.dataSet = []
        self.labels = []
    def loadDataSet(self,path,labels):
        with open(path) as fp:
            content = fp.read()

