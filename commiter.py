
# This is a bot to make any directory a git repo.
# you just need to run this code using python 3.10 + interpreter in your directory
# and input commit message and repo link. And that's it.
# Make changes and then just run this file.

import os
import time

# Make a list of files in your directory
dirlis = os.listdir()

# to check if .git folder exists
if ".git" not in dirlis:
    initializer = "git init"
    os.system(f"{initializer}")


k = 1

#to check if we have newo added in gits directory.
gitdirlis = os.listdir(".git\\refs\\remotes\\") 
os.system("git branch -m main")
# Infinite loop for infinite commits to git.
while True:
    msg = input("Commit message?\n")
    print("What would you like to add?\n 1 -> All files?\n 2 -> Recent modified file?")
    n = int(input())
    if n==2:
        os.system(f"git add \"{max(dirlis, key=os.path.getctime)}\"")
    else:
        os.system(f"git add .")

    os.system(f"git commit -m \"{msg}\"")
    yN =input("want to push (Y/N)?")
    yN.capitalize();
    if yN =='Y':
        if k==1:
            if not gitdirlis:
                repolink = str(input("What link?\n"))
                os.system("git remote add newo {}".format(repolink)) 
            k=k+1
        if k == 2:
            os.system("git push -f newo main")
        else:
            os.system("git push")
        time.sleep(100)
    else:
        continue
