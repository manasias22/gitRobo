
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
def gitadd():
    sys('git add .')

def getcmtmsg():
    msg = input("Enter a commit msg:")
    sys(f'git commit -m \"{msg}\"')
# create root window
root = Tk()
 
# root window title and dimension
root.title("GitMeUp",)
root.geometry("380x400")
directory = Text(root, height = 10,
				width = 25,
				bg = "light yellow")
# creating button
btn = Button(root, text="Init", command=lambda: Init()).grid(column=10,row=10)
btn2 = Button(root, text="commit", command=lambda: getcmtmsg()).grid(column=10,row=20)
btn3 = Button(root, text="Dir", command=lambda: get_dir()).grid(column=10,row=30)
btn4 = Button(root, text="add", command=lambda: gitadd()).grid(column=10,row=40)
# btn.pack()
 
# running the main loop
root.mainloop()