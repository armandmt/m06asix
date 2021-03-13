#!/usr/bin/python

from shutil import *
from commands import *

print 'BEFORE:'
print getoutput('ls -rlast /tmp/example') 
copytree('exemple', '/tmp/example')
print 'AFTER:'
print getoutput('ls -rlast /tmp/example')
