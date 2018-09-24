#possion graph
from scipy.stats import hypergeom
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *



def Poss():
   Values  = list(map(float,txt.get().split(',')))  # float type list is created
   Popu=np.float_(Values[0])
   Randomdrawn=np.float_(Values[1])
   Numberofsuccess = np.float_(Values[2])
   valu=hypergeom(Popu,Randomdrawn,Numberofsuccess)
   print(valu)
   x = np.arange(0,Randomdrawn+1)
   print(x)
   poss = valu.pmf(x)
   print(poss)
   plt.plot(x, poss, 'o-')
   plt.xlabel("Total Number of success in population ")
   plt.ylabel("probability of each success")
   plt.title("Poisson graph")
   plt.show()








#GUI CODE Starts here.
root = Tk()
root.title("MFCS Assignment 1")
Label(root,text="Poisson distribution").grid(row=0,column=0,sticky=W,pady=10)

#GUI CODE for Poisson Starts here.
Label(root,text="Enter N,n,k: ").grid(row=1,column=0,sticky=W)
txt = StringVar()
Entry(root,textvariable=txt).grid(row=1,column=1,sticky=W)
Button(root,text="Plot Graph Of H.P.D",command= Poss).grid(row=5,column=2,sticky=W)





root.mainloop()