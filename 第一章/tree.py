import numpy as np
import matplotlib.pyplot as plt
import treePlotter as tp

myTree = {'root':{0:'leaf node',1:{'level2':{0:'leaf node',1:'leaf node'}},2:{'level2':{0:'leaf node',1:'leaf node'}}}}

tp.createPlot(myTree)
