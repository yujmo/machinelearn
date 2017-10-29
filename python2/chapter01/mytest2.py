# -*- coding: utf-8 -*-
import numpy as np 
#---------------------------------------------
mylist,a = [1,2,3,4,5],10
for indx in range(len(mylist)):
	mylist[indx] = a*mylist[indx]
print(mylist)
#---------------------------------------------

#---------------------------------------------
mylist,a = [1,2,3,4,5],10
mymatrix = np.mat(mylist)
print(a*mymatrix)
#---------------------------------------------

