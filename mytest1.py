# -*- coding: utf-8 -*-
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

dataSet = [[1.347183,3.175500],[-1.781871,9.097953]]
#将数据集转为Numpy矩阵，并转置
dataMat = mat(dataSet).T
print(dataMat)

#绘制数据集散点图
plt.scatter(dataMat[0],dataMat[1],c='red',marker='0')

X = np.linspace(-2,2,100)
Y = 2.8 * X + 9 
plt.plot(X,Y)
plt.show()
