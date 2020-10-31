import pandas as pd
import numpy as np
data=pd.read_csv("new_deaths.csv")
n=len(data["us"])
y=data["us"][n-201:n-1]
x=np.arange(n-201,n-1)
from scipy.optimize import curve_fit
def func(x,a,b,c,d,e,f,g):
 return a*x*x*x*x*x*x+b*x*x*x*x*x+c*x*x*x*x+d*x*x*x+e*x*x+f*x+g
param=curve_fit(func,x,y)
[a,b,c,d,e,f,g]=param[0]
print(a,b,c,d,e,f,g)
import matplotlib.pyplot as plt
print("Nov. 6 deaths",int(func(305+7,a,b,c,d,e,f,g)))
print("Nov. 13 deaths",int(func(305+14,a,b,c,d,e,f,g)))
print("Nov. 20 deaths",int(func(305+21,a,b,c,d,e,f,g)))
plt.plot(x,y)
plt.plot(x,func(x,a,b,c,d,e,f,g))
x1=np.arange(n-201,330)
plt.plot(305+7,func(305+7,a,b,c,d,e,f,g),'ro')
plt.plot(305+14,func(305+14,a,b,c,d,e,f,g),'ro')
plt.plot(305+21,func(305+21,a,b,c,d,e,f,g),'ro')
plt.plot(x1,func(x1,a,b,c,d,e,f,g))
plt.show()
