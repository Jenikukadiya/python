import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,400)

y1=(8-x)/2
y2=9-3*x

plt.plot(x,y1,label='x+2y=8')
plt.plot(x,y2,label ='3x+y=9')

plt.fill_between(x, 0, np.minimum(y1, y2), where=(x <= 3), alpha=0.3)
points = [(0,0), (3,0), (2,3), (0,4)]
for p in points:
    plt.plot(p[0], p[1], 'ro')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()


