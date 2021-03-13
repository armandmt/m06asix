import sys
file = sys.argv[-1] # get user input
import os
dir = os.path.dirname(file) # get directory where file is stored
filename = os.path.basename(file) # get filename
file_tar, file_tar_ext = os.path.splitext(file) # split into file.tar and .gz
file_untar, file_untar_ext = os.path.splitext(file_tar) #split into file and .tar
os.chdir(dir)
if file_tar_ext == ".gz" and file_untar_ext == ".tar": # check if file had format .tar.gz 
	import tarfile
	tar = tarfile.open(filename) 
	tar.extractall(path=dir) # untar file into same directory
	tar.close()
	os.chdir(file_untar) # This fails if file.tar.gz has different name compared to the untarred folder e.g.. file1 instead of file
