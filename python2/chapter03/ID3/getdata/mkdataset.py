import sys  
from numpy import *
dataset = [[0,0,0,0,"no"],[0,0,0,1,"no"],[0,1,0,0,"no"],[0,2,1,0,"yes"],[0,1,1,1,"yes"],
[1,0,0,0,"yes"],[1,2,1,1,"yes"], [1,1,0,1,"yes"],[1,0,1,0,"yes"],[2,1,0,0,"yes"],[2,2,1,0,"yes"],
[2,2,1,1,"no"],[2,1,1,0,"yes"],[2,1,0,1,"no"]]
numlist = [64,64,128,64,64,128,64,32,32,60,64,64,132,64]
datalines =[]

for element,num in zip(dataset,numlist):
	liststr =""
	for cell in element:
		liststr += str(cell)+"\t"
	liststr = liststr[:-1]	
	for i in range(num):
		datalines.append(liststr)
	
with open("data.dat","w") as fp:
    fp.write("\n".join(datalines)) 
