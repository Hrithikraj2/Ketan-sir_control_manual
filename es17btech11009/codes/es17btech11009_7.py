import control
import matplotlib.pyplot as plt

num = [0,0,0,0,200]
den = [1,16,86,176,105]

#Transfer function GH = num/den
G = control.tf(num,den) 
control.nichols_plot(G)
plt.grid(True)
plt.scatter(-180,0,s=40)
plt.annotate("-180,0dB",(-180,0))
plt.scatter(180,0,s=40)
plt.annotate("(180,0dB)",(180,0))
plt.title('Nichols Chart')
plt.xlabel('Phase(deg) ')
plt.ylabel('Gain(dB)')
plt.show()

#if using termux
plt.savefig('./figs/es17btech11009_7.pdf')
plt.savefig('./figs/es17btech11009_7.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11009_7.pdf"))
#else
#plt.show()