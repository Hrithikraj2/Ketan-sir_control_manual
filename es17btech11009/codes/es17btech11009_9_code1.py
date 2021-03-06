#Plots M and N circles with Nyquist pot
import control
import matplotlib.pyplot as plt
import numpy as np
from pylab import*

#if using termux
#import subprocess
#import shlex
#end if

num = [0,0,0,1000]
den = [1,18,119,342,1360]
G = control.tf(num,den) 

#Defining M and N circles
def M_circle(m):
  theta = np.linspace(0, 2*np.pi, 100)
  x0 = m**2/(1-m**2)
  y0 = 0
  r = np.absolute(m/(1-m**2))
  x = x0 + r*np.cos(theta)
  y = y0 + r*np.sin(theta)
  return x,y,r,x0,y0

def N_circle(n):
  theta = np.linspace(0, 2*np.pi, 100)
  x0 = -0.5
  y0 = 1/(2*n)
  r = np.sqrt((1/4) + (1/(4*n**2)))
  x = x0 + r*np.cos(theta)
  y = y0 + r*np.sin(theta)
  return x,y,r,x0,y0
  

#M circles plot  
subplot(2,1,1)

m=np.arange(0,3,0.2)
for num in m: 
    if num != 1:
      p=M_circle(num)
      plt.plot(p[0],p[1] )
      if (num >= 0.6 and num <= 1):
        plt.text(0.8*(p[3]+p[2]),0.8*(p[4]+p[2]),np.around(num,decimals=2))
      elif (num >=1.4  and num <= 1.6):  
        plt.text(0.8*(p[3]-p[2]),0.8*(p[4]-p[2]),np.around(num,decimals=2))

plt.axvline(x=-0.5,label='M=1')  
w=np.logspace(-100,100,1000)
control.nyquist(G,w,label='Rect coord')

plt.grid(True)
plt.title('M Contors in rect coordinates')
plt.axis('equal')
plt.xlim(-4,4)
plt.xlabel('Real')
plt.ylim(-3,3)
plt.ylabel('Imaginary')
plt.legend(loc='best',prop={'size':11})


#N circles plot
subplot(2,1,2)

n=np.arange(-2,2,0.2)
for num in n:
  if num != 0:
    q=N_circle(num)
    plt.plot(q[0],q[1] )
    if num == 0.2 :
        plt.text(1.25*(q[3]-q[2]),0.2*(q[4]+q[2]),np.around(num,decimals=2))
    elif num == 0.4 :
        plt.text(q[3]-q[2],0.2*(q[4]+q[2]),np.around(num,decimals=2))    
    elif num == -0.4:    
        plt.text(1.15*(q[3]-q[2]),0.65*(q[4]-q[2]),np.around(num,decimals=2))
    elif num == -0.6:    
        plt.text(0.6*(q[3]-q[2]),0.65*(q[4]-q[2]),np.around(num,decimals=2))
        
      
w=np.logspace(-100,100,1000)

control.nyquist(G,w,label='Rect coord')

plt.grid(True)
plt.title('N Contours in rect coordinates')
plt.axis('equal')
plt.xlim(-3,3)
plt.xlabel('Real')
plt.ylim(-4,4)
plt.ylabel('Imaginary')
plt.legend(loc='best',prop={'size':11})

#if using termux
#plt.savefig('./figs/ee18btech11017/ee18btech11017_fig1.pdf')
#plt.savefig('./figs/ee18btech11017/ee18btech11017_fig1.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11017/ee18btech11017_fig1.pdf"))

#else

plt.show()
