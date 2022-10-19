
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
mk = 1
gitdirlis = os.listdir(".git\\refs\\")
#to check if we have newo added in gits directory.
if mk ==1:
    if "remotes" not in gitdirlis:
        repolink = str(input("GIthub link?\n"))
        if ".git" in repolink:
            os.system("git remote add newo {}".format(repolink)) 
        mk = 2
    else:
        print("Github link exists.")    

os.system("git branch -m main")
# Infinite loop for infinite commits to git.
while True:
    msg = input("Commit message?\n")
    os.system("git add .")
    os.system(f"git commit -m \"{msg}\"")
    yN =input("want to push (Y/N)?")
    yN.capitalize();
    if yN =='Y':
        if k==1:
            os.system("git push -f newo main")
            k += 1
        else:
            os.system("git push")
        time.sleep(100)
    else:
        continue
