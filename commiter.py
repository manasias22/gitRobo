
# This is a bot to make any directory a git repo.
# you just need to run this code using python 3.10 + interpreter in your directory
# and input commit message and repo link. And that's it.
# Make changes and then just run this file.

import os

# Make a list of files in your directory
dirlis = os.listdir()

# to check if .git folder exists
if ".git" not in dirlis:
    initializer = "git init"
    os.system(f"{initializer}")


statusChecker = 1
mk = 1

gitdirlis = os.listdir(".git\\refs\\")

#to check if we have newo added in gits directory.
if mk ==1:
    if "remotes" not in gitdirlis:
        repolink = str(input("Github link?\n"))
        if ".git" in repolink:
            os.system("git remote add newo {}".format(repolink)) 
        mk = 2
    else:
        print("Github link exists.")    

os.system("git branch -m main")

# Infinite loop for infinite commits to git.

while True:
    msg = input("Commit message?\n")
    print("What would you like to add?\n 1 -> All files?\n 2 -> Recent modified file?")
    n = int(input())
    if n==2:
        fileName =str(max(dirlis, key=os.path.getmtime))
        print("modified File is ",fileName)
        os.system(f"\"git add {fileName}\"")
    else:
        os.system(f"git add .")

    os.system(f"git commit -m \"{msg}\"")
    yN =input("want to push (Y/N)?")
    yN.capitalize();
    if yN =='Y':
        if statusChecker == 1:
            os.system("git push -f newo main")
            statusChecker += 1
        else:
            os.system("git push -u newo")
    else:
        continue
