#/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

try:

       llista = os.listdir("/etc")
       print llista

       os.chdir("/tmp")
       print os.getcwd()
       os.chdir("/home/armand")
       print os.getcwd()

       os.mkdir ("prova") # crea un directori
       os.chdir("prova")
       os.system("touch fitxerin") # executa una ordre del shell
       dir(os.getcwd()) # imprimeix el directori prova sense emprar el mbdul os
       os.chdir("..")
       #os.rmdir("prova") # ha de donar error
       # os.removedirs("prova")
       os.mkdir("provados")
       os.rename("provados","provatres")
       os.removedirs("prova")

except OSError as e:
       # InformaciO prbpia del mbdul OS, que tambe pot donar error
       #print "Opps. Hi ha hagut algun error: " + str(e.errno) 
       #print e.strerror + "--" + e.filename
       print " #Error error error error error ########"
       print sys.exc_info() # Aquesta es la informacio generica

