import tarfile
import os

os.mkdir('outdir')
t = tarfile.open('example.tar', 'r')
t.extract('README.txt', 'outdir')
print os.listdir('outdir')

