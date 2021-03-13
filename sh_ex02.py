#!/usr/bin/python

from shutil import *
import os
import time

def show_file_info(filename):
   stat_info = os.stat(filename)
   print '\tMode:    ', stat_info.st_mode
   print '\tCreated: ', time.ctime(stat_info.st_ctime)
   print '\tAccessed:', time.ctime(stat_info.st_atime)
   print '\tModified:', time.ctime(stat_info.st_mtime)

os.mkdir('exemple')
print 'SOURCE:'
show_file_info('sh_ex02.py')
copy2('sh_ex02.py', 'exemple')
print 'DEST:'
show_file_info('exemple/sh_ex02.py')
