#!/usr/bin/python
import os

tempus=os.walk("/var/log")

for root, dir, files in tempus:
	if "history*" in files: print os.path.join(root,".placeholder")


#for root, dir, files in os.walk("/tmp"):
#	for file in files:
#		fullpath = os.path.join(root,file)

