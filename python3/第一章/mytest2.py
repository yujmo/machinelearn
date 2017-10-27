# -*- coding: utf-8 -*- 
from numpy import * 
import matplotlib.pyplot as plt 
dist = mat([[0.1,0.1],[0.9,0.5],[0.9,0.1],[0.45,0.9],[0.9,0.8],[0.7,0.9],[0.1,0.45],[0.45,0.1]]) 
m,n = shape(dist) 
fig = plt.figure() 
# 绘图 
ax = fig.add_subplot(111) 
ax.scatter(list(dist.T[0]),list(dist.T[1]),c='blue',marker='o') # 问题在这句 
for point in dist.tolist(): 
  plt.annotate("("+str(point[0])+", "+str(point[1])+")",xy = (point[0],point[1])) 
xlist = []
ylist = [] 
for px,py in zip(dist.T.tolist()[0],dist.T.tolist()[1]): 
  xlist.append([px]) 
  ylist.append([py]) 
ax.plot(xlist,ylist,'r') 
plt.show()

  
