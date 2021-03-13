import tarfile
import os

os.mkdir('outdir')
t = tarfile.open('example.tar', 'r')
t.extractall('outdir', members=[t.getmember('README.txt')])
print os.listdir('outdir')
