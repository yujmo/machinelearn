from numpy import *
matV = mat([[1,1,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,1,1]])
smstr = nonzero(matV[0]-matV[1])
#print(shape(smstr[0])[1])
print(smstr)
print(shape(smstr[0])[1])
