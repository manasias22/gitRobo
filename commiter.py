
# This is a bot to make any directory a git repo.
# you just need to run this code using python 3.10 + interpreter in your directory
# and input commit message and repo link. And that's it.
# Make changes and then just run this file.

import os
initializer = "git init"
add ="git add ."
msg = str(input("Commit message?\n"))
cmt = f"git commit -m {msg}"
os.system(f"{initializer}")
os.system(f"{add}")
os.system(f"{cmt}")
repolink = str(input("What link?\n"))
os.system("git remote add newo {}".format(repolink))
yN = input("want to push?")

if yN =='Y' or yN =='y':
    os.system("git push -u newo main")
else:
    pass
