#!/usr/bin/python
import tarfile
tar = tarfile.open("temp.tar.gz", "w|gz")
import os
for root, dir, files in os.walk("/tmp"):
	for file in files:
		fullpath = os.path.join(root,file)
		tar.add(fullpath)

tar.close()
