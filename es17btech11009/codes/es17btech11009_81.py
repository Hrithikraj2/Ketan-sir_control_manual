

# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:33:12 2020

@author: Hrithik
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

gain = 1				
num = [0,0,0,10]
char_eq = [1,3,2,10]
zeros=np.roots(num)
poles=np.roots(char_eq)


gain_2 = (poles[0])*(poles[1])		# second order approximated transfer function
num_2 = [1]
zeros_2=np.roots(num_2)
poles_2=np.array([poles[0],poles[1]])

system = signal.lti(zeros,poles,np.array([gain]))
system_2 = signal.lti(zeros_2,poles_2,np.array([gain_2]))

T, yout = signal.step(system)			# step response without approximation
T_2, yout_2 = signal.step(system_2)		# step response with approximation

plt.plot(T,yout,label="Without approximation")
plt.plot(T_2,yout_2,'g',label="With approximation")
plt.grid()
plt.title("Step response")
plt.xlabel("Time")
plt.ylabel("y(t)")
plt.legend()

#if using termux
plt.savefig('./figs/es17btech11009_81.pdf')
plt.savefig('./figs/es17btech11009_81.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11009_81.pdf"))
#else
#plt.show()