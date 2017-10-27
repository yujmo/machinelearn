from numpy import *
A = mat([[1,2,4,5,7,],[9,12,11,8,2,],[6,4,3,2,1,],[9,1,3,4,5,],[0,2,3,4,1]])
print(linalg.det(A)) #方阵的行列式

print(linalg.inv(A)) #方阵的逆

print(A.T) #方阵的对称

print(linalg.matrix_rank(A)) #方阵的秩

