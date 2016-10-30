#file handle
import tempfile,os

def create_file(code):
	f = NamedTemporaryFile()
	file_name = f.name
	
	if os.path.exists(file_name):
		f.write(code)
		f.close()
	
	return file_name#returns path to file to be deleted

def delete_files(files):
	for file in files:
		if os.path.exists(file):
			os.unlink(file)
	error_files =[]
	for file in files:
		if os.path.exist(file)==True:
			error_files.append(file)
	if len(l)==0:
		return("Files deleted successfully.")
	else:
		return("Error deleting files: "+l)

