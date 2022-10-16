
# from multiprocessing.connection import wait
import os
initializer ="git init"
add ="git add ."
msg = input("COmmit message?\n") 
cmt = f"git commit -m {msg}"
os.system(f"{initializer}")
os.system(f"{add}") 
# wait(10)
os.system(f"{cmt}")