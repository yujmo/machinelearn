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

#相关系数
featuremat = mat([[88.5,96.8,104.1,111.3,117.7,124.0,130.0,135.4,140.2,145.3,151.9,159.5,165.9,169.8,171.6,172.3,172.7],
    [12.54,14.65,16.64,18.98,21.26,24.06,27.33,30.46,33.74,37.69,42.49,48.08,53.37,57.08,59.35,60.68,61.40]])
print(featuremat)

mv1 = mean(featuremat[0])
mv2 = mean(featuremat[1])
print(mv1,mv2) #打印均值

dv1 = std(featuremat[0])
dv2 = std(featuremat[1])
print(dv1,dv2) #两列标准差

corref = mean(multiply(featuremat[0]-mv1,featuremat[1]-mv2)/(dv1*dv2))
print(corref)

print(corrcoef(featuremat))



