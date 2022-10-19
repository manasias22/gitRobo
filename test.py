import os

lis = os.listdir()
fileName =str(max(lis, key=os.path.getmtime))
print("modified File is ",fileName)
os.system(f"\"git add {fileName}\"")