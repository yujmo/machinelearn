import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5,200)
y = np.sin(x)
yn = y + np.random.rand(1,len(y)) * 1.5
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x,yn,c='blue',marker='o')
ax.plot(x,y+0.75,'r')
plt.show()
