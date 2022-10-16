import os
initializer ="git init"
add ="git add ."
msg = input("COmmit message?\n") 
cmt = f"git commit -m {msg}"
os.system(f"{initializer}")
os.system(f"{add}")
# os.system(f"git commit -m {msg}") 
os.system(f"{cmt}")
repolink = str(input("What link?\n"))
os.system(f"git remote add origin {repolink}")
os.system("git push origin")