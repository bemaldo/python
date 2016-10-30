#works for windows 10 probably all windows
'''
>>> import os
>>> os.__file__
'C:\\python27\\lib\\os.pyc'
'''
import os,re

def find_drives():
	return re.findall(r"[A-Z]+:.*$",os.popen("mountvol /").read(),re.MULTILINE)

def find_users():
	drives = find_drives()
	users = []
	for drive in drives:
		if os.path.exists(drive+'Users'):
			for user in os.listdir(drive+'Users'):
				users.append((drive,user))
	return users

def cd(path):
	if os.path.exists(path):
		os.chdir(path)
	else:
		return("Directory does not exist.")
	return("Changed directory to: "+os.getcwd())

def list_directory(path='.'):
	if os.path.exists(path):
		return os.listdir(path)
	return ("Directory "+path+" does not exist.")
