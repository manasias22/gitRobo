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
def gitpush():
    sys('git push')
def getcmtmsg():
    msg = input("Enter a commit msg:")
    sys(f'git commit -m \"{msg}\"')
def gituser():
    uname = input("Enter your github username: ")
    sys(f'git config --global user.name \"{uname}\"')
def gitmail():
    mailid = input("Enter mail id associated to your github acc: ")
    sys(f'git config --global user.mail \"{mailid}\"')
def status():
    sys(f'git status')

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
btn4 = Button(root, text="Push", command=lambda: gitpush()).grid(column=10,row=50)
btn5 = Button(root, text="Username", command=lambda: gituser()).grid(column=10,row=60)
btn6 = Button(root, text="mail", command=lambda: gitmail()).grid(column=20,row=60)
btn7 = Button(root, text="mail", command=lambda: gitmail()).grid(column=15,row=70)
# btn.pack()
 
# running the main loop
root.mainloop()