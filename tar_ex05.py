import tarfile

t = tarfile.open('example.tar', 'r')
for filename in [ 'README.txt', 'notthere.txt' ]:
    try:
        f = t.extractfile(filename)
    except KeyError:
        print ('ERROR: Did not find %s in tar archive' % filename)
    else:
        print (filename, ':', f.read())
