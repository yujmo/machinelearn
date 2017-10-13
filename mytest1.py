# -*- coding: utf-8 -*-
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

dataSet = [[1.347183,3.175500],[-1.781871,9.097953],[-0.752157,6.538620],[-1.322371,7.152853],[0.423363,11.054677],[0.406704,7.067335],[0.667394,12.741452],[-2.460150,6.866805],[0.569411,9.548755],[-0.026632,10.427743],[0.850433,6.920334],[1.347183,13.175500],[1.176813,3.167020],[-1.781871,9.097953]]
#将数据集转为Numpy矩阵，并转置
dataMat = mat(dataSet).T

#绘制数据集散点图
plt.scatter(list(dataMat[0]),list(dataMat[1]),c='red',marker='o')

X = np.linspace(-2,2,100)
Y = 2.8 * X + 9 
plt.plot(X,Y)
plt.show()
