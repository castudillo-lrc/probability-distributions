from tkinter import *
from math import *
import tkinter as tk
from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np
global x
global r


def calculation():
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


def graph():
    plt.plot(x, r)
    plt.xlabel('number of success')
    plt.ylabel('probability of succeses')
    plt.show()


def delete():
    e.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


root = tk.Tk()
root.title("probability distributions")

g=StringVar()
v=StringVar()

w1 = tk.Label(text="BINOMIAL DISTRIBUTION", padx=10).grid(row=0)
w = tk.Label(text = "enter the number of trials (n): ", padx = 10).grid(row = 1)
e = Entry(root)
w2 = tk.Label(text="enter probabilty of success (p): ", padx=10).grid(row = 2)
e1 = Entry(root)
w3 = tk.Label(text="range of RV x starts from: ", padx=10, pady=10).grid(row=3)
e2 = Entry(root)
w4 = tk.Label(text="range of RV x ends at: ", padx=10, pady=10).grid(row=4)
e3 = Entry(root, bd = 3)
w5 = tk.Label(text="answer is: ", padx=10, pady = 10).grid(row=5)
w6 = tk.Label(text = "NORMAL DISTRIBUTION", padx = 10, pady = 10).grid(row = 8)

e.grid(row = 1, column =1)
e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3.grid(row =4, column = 1)
tk.Button( root, text="Calculate", command=calculation).grid(row=6, column=0, sticky = W)
tk.Button(root, text = "quit", command = root.quit).grid(row=6, column=1, padx = 5)
tk.Button(root, text = "clear", command = delete).grid(row = 6, column = 1, sticky = W)
tk.Button(root, text = "Show graph", command = graph).grid(row = 6, column =0, padx=15)
root.mainloop()