from numpy import *
#范数
A = [8,1,6]
print(linalg.norm(A))

#闵可夫斯基距离：一组距离的定义

#欧式距离
vector1 = mat([1,2,3])
vector2 = mat([4,5,6])
print(sqrt((vector1-vector2)*(vector1-vector2).T))

#曼哈顿距离
vector1 = mat([1,2,3])
vector2 = mat([4,5,6])
print(sum(abs(vector1-vector2)))

#切比雪夫距离
vector1 = mat([1,2,3])
vector2 = mat([4,7,5])
print(abs(vector1-vector2).max())

#夹角余弦
vector1 = mat([4,5,6])
vector2 = mat([4,5,6])
print((dot(vector1,vector2.T))/(linalg.norm(vector1)*linalg.norm(vector2)))







