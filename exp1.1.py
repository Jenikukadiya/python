
import numpy as np 
import matplotlib.pyplot as plt 
x= np.linspace(0,10,400)
y = x-1
plt.plot(x,y,label ='x-y=1')
plt.fill_between(x,0,x-1,where =(x>=1),alpha =0.3 )
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()