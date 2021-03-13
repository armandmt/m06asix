#!/usr/bin/python

from shutil import *
from commands import *
import os

f = open('file_to_change.txt', 'wt')
f.write('content')
f.close()
os.chmod('file_to_change.txt', 0444)

print 'BEFORE:', getstatus('file_to_change.txt')
copymode('sh_ex03.py', 'file_to_change.txt')
print 'AFTER :' , getstatus('file_to_change.txt')
