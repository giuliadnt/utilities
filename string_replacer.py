__author__ = "Giulia Dnt"

import os

def replace_substring():
	original = raw_input("Enter the substring you want to modify: ")
	new = raw_input("Enter the new substring: ")
	ext = raw_input("Enter the file extension (include the '.'): ")
	path = raw_input("Enter the absolute path of the file folder: ")
	for file in os.listdir(path):
		if file.endswith(ext):
			os.rename(path + "/" + file, path + "/" + file.replace(original, new))

def append_substring():
	pref=raw_input("Enter the substring you want to add as prefix to the filename: ")
	ext = raw_input("Enter the file extension (include the '.'): ")
	path = raw_input("Enter the absolute path of the file folder : ")
	for file in os.listdir(path):
		if file.endswith(ext):
			os.rename(path + "/" + file, path + "/" + pref + file)

def main():

	print("Please input your decision: " + "\n" +
		  "write replace if you want to modify a substring in the filename, " + "\n" +
		  "write append if you want to add a substring to the filename")
	#attempts = 0
	#while True:
	#try:
	decision = raw_input("Append or Replace? ").lower().strip()
	#except ValueError:
	#print("Please submit a valid answer")
	#continue
	if decision == "replace":
		replace_substring()
	elif decision == "append":
		append_substring()
	else:
		print("This is not a valid option")
		main()

	

if __name__ == "__main__":
	main()
	

