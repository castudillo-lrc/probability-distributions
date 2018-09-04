from tkinter import *
from math import *
import tkinter as tk
from scipy.stats import binom
from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np


def binom_cal():
    n = int(e.get())
    p = float(e1.get())
    x1 = int(e2.get())
    x2 = int(e3.get())
    global x
    x = np.arange(x1, x2)
    global r
    r = binom.pmf(x, n, p)
    print(r)
    total = 0

    for add in r:
        #total = 0
        total+=add
    print(total)
    global e4
    e4 = Entry(root)
    e4.grid(row = 5, column = 1)
    e4.insert(10, str(total))

def norm_cal():
    global m, sd, s
    m = float(e5.get())
    sd = float(e6.get())
    s = np.random.normal(m, sd, 1000)
    norm_graph()

def poisson_cal():
    a = int(e7.get())
    b = int(e8.get())
    c = float(e9.get())
    global x
    global s
    x = np.arange(a, b)
    s = poisson.pmf(x, c)
    total = 0
    for d in s:
        total+=d
    print(total)
    e10 = Entry(root)
    e10.grid(row = 16, column = 1)
    e10.insert(10, str(total))

def binom_graph():
    plt.plot(x, r, 'o-')
    plt.xlabel('number of success')
    plt.ylabel('probability of succeses')
    plt.show()

def norm_graph():
    count, bins, ignored = plt.hist(s, 30, density=True)
    plt.xlabel("value of random variable")
    plt.ylabel("Probability")
    plt.plot(bins, 1 / (sd * np.sqrt(2 * np.pi)) *
             np.exp(- (bins - m) ** 2 / (2 * sd ** 2)),
             linewidth=2, color='r')
    plt.show()

def poisson_graph():
    plt.plot(x, s, 'o-')
    plt.xlabel("no. of events")
    plt.ylabel("probability of success")
    plt.show()


def delete():
    e.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


root = tk.Tk()
frame = Frame(root)
scrollbar = Scrollbar(frame)
#scrollbar.pack( side = RIGHT, fill = Y )
#scrollbar.grid(side = RIGHT, fill = Y)
root.title("probability distributions")

g=StringVar()
v=StringVar()

w1 = tk.Label(text="BINOMIAL DISTRIBUTION", padx=10, fg = "red").grid(row=0)
w = tk.Label(text = "enter the number of trials (n): ", padx = 10, pady = 10).grid(row = 1)
e = Entry(root)
w2 = tk.Label(text="enter probabilty of success (p): ", padx=10, pady = 10).grid(row = 2)
e1 = Entry(root)
w3 = tk.Label(text="range of RV x starts from: ", padx=10, pady=10).grid(row=3)
e2 = Entry(root)
w4 = tk.Label(text="range of RV x ends at: ", padx=10, pady=10).grid(row=4)
e3 = Entry(root, bd = 3)
w5 = tk.Label(text="answer is: ", padx=10, pady = 10).grid(row=5)
w6 = tk.Label(text="NORMAL DISTRIBUTION", padx = 10, pady = 10, fg = "red").grid(row = 8)
w7 = tk.Label(text = "enter mean: ", padx = 10, pady = 10).grid(row = 9)
e5 = Entry(root)
w8 = tk.Label(text = "enter Std. Deviation: ", padx = 10, pady = 10).grid(row = 10)
e6 = Entry(root)
w9 = tk.Label(text = "POISSON DISTRIBUTION", padx= 10, pady = 10, fg = "red").grid(row =12)
w10 = tk.Label(text = "range of k starts from : ", padx = 10, pady = 10).grid(row = 13)
e7 = Entry(root)
w11 = tk.Label(text = "range of k ends at : ", padx = 10, pady = 10).grid(row = 14)
e8 = Entry(root)
w12 = tk.Label(text = "Enter mean (lambda) : ", padx = 10, pady = 10).grid(row = 15)
e9 = Entry(root)
w13 = tk.Label(text = "answer is: ", padx = 10, pady = 10).grid(row = 16)
w14 = tk.Label(text = "UNIFORM DISTRIBUTION: ", padx = 10, pady = 10, fg = "red").grid(row =0, column = 8, padx = 100, sticky = E)
w15 = tk.Label(text = "Enter lower boundary : ", padx = 10, pady = 10).grid(row =1, column = 8, padx = 100, sticky = E)
e11 = Entry(root)
w16 = tk.Label(text = "Enter upper boundary : ", padx = 10, pady = 10).grid(row =2, column = 8, padx = 100, sticky = E)
e12 = Entry(root)
w17 = tk.Label(text = "Enter size of samples : ", padx = 10, pady = 10).grid(row =3, column = 8, padx = 100, sticky = E)
e13 = Entry(root)


e.grid(row = 1, column =1)
e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3.grid(row =4, column = 1)
e5.grid(row = 9, column = 1)
e6.grid(row = 10, column = 1)
e7.grid(row = 13, column =1)
e8.grid(row = 14, column = 1)
e9.grid(row = 15, column = 1)
e11.grid(row = 1, column = 9)
e12.grid(row = 2, column = 9)
e13.grid(row = 3, column = 9)


tk.Button( root, text="Calculate", command=binom_cal).grid(row=6, column=0, sticky = W,padx=0)
tk.Button(root, text = "Show graph", command = binom_graph).grid(row = 6, column =0, padx=5, sticky = E)
tk.Button(root, text = "quit", command = root.quit).grid(row=6, column=1, padx = 5)
tk.Button(root, text = "clear", command = delete).grid(row = 6, column = 1, sticky = W)
tk.Button( root, text="Calculate and show graph", command=norm_cal).grid(row=11, column=1, sticky = W)
tk.Button(root, text = "Calculate", command = poisson_cal).grid(row = 17, column = 0, sticky = W)
tk.Button(root, text = "Show graph", command = poisson_graph).grid(row = 17, column = 1)
root.mainloop()