import numpy as np 
import matplotlib.pyplot as plt 
x = np.linspace(0,10,400)
y=(8-x)/2

plt.plot(x,y,label='x+2y=8')
plt.fill_between (x,0,y,where=(y>=0),alpha =0.2)

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()