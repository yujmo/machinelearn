from numpy import *

A = [[8,1,6],[3,5,7],[4,9,2]]
evals,evecs = linalg.eig(A)
print(evals,evecs) #特征值，特征向量

