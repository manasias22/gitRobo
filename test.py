import tkinter as tk
from tkinter import ttk

win = tk.Tk()

v = tk.StringVar()
def setText(word):
    v.set(word)

a = ttk.Button(win, text="plant", command=setText("plant"))
a.pack()
b = ttk.Button(win, text="animal", command=setText("animal"))
b.pack()
c = ttk.Entry(win, textvariable=v)
c.pack()
win.mainloop()