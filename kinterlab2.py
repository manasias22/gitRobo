
# importing tkinter
from os import system as sys
from tkinter import *
 
# defining function
 
def get_dir():
    dry= directory.get('1.0',"end-1c")
    sys(f"cd {dry}")
def remote_link():
    pass
def Init():
    sys("git init")

# create root window
root = Tk()
 
# root window title and dimension
root.title("GitMeUp")
root.geometry("380x400")
directory = Text(root, height = 10,
				width = 25,
				bg = "light yellow")
# creating button
btn = Button(root, text="Init", command=lambda: Init()).grid(column=10,row=0)
btn = Button(root, text="Dir", command=lambda: get_dir()).grid(column=10,row=10)
# btn.pack()
 
# running the main loop
root.mainloop()