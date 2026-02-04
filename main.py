import os
import random

files = []
directory = r"\\arcadia\Multimedia\Films"
import_dir = os.listdir(directory)


for file in import_dir:
	files.append(file)

suggest_nb = random.randint(0, len(files))
for item in files:
	print(item)

print(len(files))
print("================================")
print(f"Je te propose de regarder: {files[suggest_nb]}")
print("================================")
