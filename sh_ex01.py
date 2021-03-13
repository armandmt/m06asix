#/usr/bin/python
from shutil import *
import os
try:
	os.mkdir('exemple')
	print 'BEFORE:', os.listdir('exemple')
	copy('sh_ex01.py', 'exemple')
    	print 'AFTER:', os.listdir('exemple')
except IOError:
	print "Oeee, el fitxer no hieee"
except OSError:
	print "Oeee, el directori ja hieee"
