import tarfile
import os

os.mkdir('outdir')
t = tarfile.open('example.tar', 'r')
t.extractall('outdir')
print os.listdir('outdir')

