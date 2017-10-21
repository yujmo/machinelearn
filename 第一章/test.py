# -*- coding: utf-8 -*-
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
dataSet  =  [[0,0],[3,8],[2,2],[1,1],[5,3],[4,8],[6,3],[5,4],[6,4],[7,5]]
dataMat = mat(dataSet).T

#绘制数据集散点图
plt.scatter(list(dataMat[0]),list(dataMat[1]),c='red',marker='o')

X = np.linspace(-1,1,10)
Y =  X  * 0
plt.plot(X,Y)
plt.show()
