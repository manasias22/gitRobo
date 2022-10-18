
# This is a bot to make any directory a git repo.
# you just need to run this code using python 3.10 + interpreter in your directory
# and input commit message and repo link. And that's it.
# Make changes and then just run this file.
import timer
import os
dirlis = os.listdir()
if ".git" not in dirlis:
    initializer = "git init"
    os.system(f"{initializer}")
k = 1

def rec():
    os.system("git add .")
    msg = input("Commit message?\n")
    os.system(f"git commit -m {msg}")
    yN = input("want to push (Y/N)?")
    yN.capitalize();
    if yN =='Y':
        if k==1:
            repolink = str(input("What link?\n"))
            os.system("git remote add newo {}".format(repolink)) 
            k=k+1
        if k == 2:
            os.system("git push -f newo main")
        else:
            os.system("git push")
    else:
        pass

while True:
    timer.set_timer(1000,rec())