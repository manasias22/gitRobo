import os
list_of_files = os.listdir()
latest_file = max(list_of_files, key=os.path.getmtime)
print(latest_file)