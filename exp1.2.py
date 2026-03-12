import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(0,6,400)

y1=2-x
y2=5-x

plt.plot(x,y1,label= 'x+y=2')
plt.plot(x,y2,label ='x+y = 5')

plt.fill_between(x, y1, -10, alpha=0.3)

plt.fill_between(x, y2, 10, alpha=0.3)

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
