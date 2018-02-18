#import numpy as np
from numpy import *

#矩阵的初始化------------------------------------------------------------------
myZero = zeros([3,5]) #3x5的全0矩阵
print(myZero)

myOnes = ones([3,5])  #3x5的全1矩阵
print(myOnes)

myRand = random.rand(3,4) #3x4的0~1之间的矩阵
print(myRand)

myEye = eye(3) #3x3的单位矩阵
print(myEye)
#矩阵的初始化结束--------------------------------------------------------------

#矩阵的计算--------------------------------------------------------------------
print(myOnes + myZero) #矩阵相加

print(myZero - myOnes) #矩阵相减

#矩阵的数乘
myMatrix = mat([[1,2,3],[4,5,6],[7,8,9]])
a = 10
print(10*myMatrix)

print(sum(myMatrix)) #矩阵所有元素求和

print(multiply(myMatrix,2*ones([3,3]))) #矩阵各元素的积

print(power(myMatrix,2)) #矩阵各元素的n次幂

myMatrix1 = mat([[1,2,3],[4,5,6],[7,8,9]])
myMatrix2 = mat([[1],[2],[3]])
print(myMatrix*myMatrix) #矩阵相乘
#矩阵的计算结束----------------------------------------------------------------

#矩阵的进阶操作----------------------------------------------------------------
myMatrix = mat([[1,2,3],[4,5,6],[7,8,9]])
print(myMatrix.T) #矩阵的转置
myMatrix.transpose() #矩阵的转置
print(myMatrix)

#矩阵的其他操作：行列数、切片、复制、比较
myMatrix = mat([[1,2,3],[4,5,6],[7,8,9]])
(m,n)=shape(myMatrix)
print(m,n) #矩阵的行列数

print(myMatrix[0])

print(myMatrix.T[0])

a = myMatrix.copy()
print(a)

print(myMatrix < myMatrix.T) #矩阵元素的比较




A = mat([[1,2,4,5,7,],[9,12,11,8,2,],[6,4,3,2,1,],[9,1,3,4,5,],[0,2,3,4,1]])
print(linalg.det(A)) #方阵的行列式

print(linalg.inv(A)) #方阵的逆

print(A.T) #方阵的对称

print(linalg.matrix_rank(A)) #方阵的秩

from numpy import *

A = [[8,1,6],[3,5,7],[4,9,2]]
evals,evecs = linalg.eig(A)
print(evals,evecs) #特征值，特征向量

