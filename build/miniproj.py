# importing tkinter
# from os import os.systemtem as os.system
import os
from tkinter import *
# defining function
 
def get_dir():
    dry= directory.get('1.0',"end-1c")
    os.system(f"cd {dry}")
def remote_link():
    pass
def Init():
    os.system("git init")
def gitadd():
    os.system('git add .')
def gitpush():
    try:
        os.system('git push -u origin main')
    except:
        os.system("git push")
def gitusname():
    print('your mail id is: ')
    os.system('git config --global user.mail')
def gitusmail():
    print('your username is: ')
    os.system('git config --global user.name')
def getcmtmsg():
    msg = input("Enter a commit msg:")
    os.system(f'git commit -m \"{msg}\"')
def mgituser():
    uname = input("Enter your github username: ")
    os.system(f'git config --global user.name \"{uname}\"')
def gitmail():
    mailid = input("Enter mail id associated to your github acc: ")
    os.system(f'git config --global user.mail \"{mailid}\"')
def status():
    os.system(f'git status')
def chd():
    d = input("Enter the absolute path:")
    try:
        os.chdir(d)
    except (FileNotFoundError):
        os.mkdir(d)
        os.chdir(d)
def gitrmtadd():
    link = input("Enter git link")
    if ".git" in link:
        os.system(f"git remote add origin {link}")
    else:
        print("incorrect link")

def directory():
    print(os.getcwd())
# create root window
root = Tk()
# root window title and dimension
root.title("GitMeUp",)
root.geometry("380x400")
directory = Text(root, height = 10,
				width = 25,
				bg = "light yellow")
# creating button
b = Button(root,text="Select Directory",command=lambda: chd()).grid(column=10,row=20)
btn = Button(root, text="Init", command=lambda: Init()).grid(column=10,row=30)
btnadd = Button(root, text="add", command=lambda: gitadd()).grid(column=10,row=40)
btnaddrmt = Button(root, text="add remote repo", command=lambda: gitrmtadd()).grid(column=20,row=40)
btncommit = Button(root, text="commit", command=lambda: getcmtmsg()).grid(column=10,row=50)
btnpush = Button(root, text="Push", command=lambda: gitpush()).grid(column=10,row=60)
btnusrnm = Button(root, text="Modify my Username", command=lambda: gituser()).grid(column=10,row=70)
btnusrname = Button(root, text="Show me my Mail id", command=lambda: gitusname()).grid(column=20,row=70)
btnmail = Button(root, text="Modify my mail", command=lambda: gitmail()).grid(column=10,row=80)
btnusmail = Button(root, text="Show me my user name", command=lambda: gitusmail()).grid(column=20,row=80)
btnsts = Button(root, text="status", command=lambda: status()).grid(column=10,row=90)
btnexit = Button(root, text="EXIT", command=lambda: exit()).grid(column=10,row=100)
# btn.pack()
 
# running the main loop
root.mainloop()