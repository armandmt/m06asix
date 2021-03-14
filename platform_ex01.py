import platform

print(platform.platform())
print("Processador: " + platform.processor())
print("Màquina: " + platform.machine())
print("Sistema: " + platform.system())
print("Versió SO: " + platform.version())
print("Release (Versió kernel): " + platform.release())
print("Node (Nom de xarxa) : " + platform.node())

maquina = platform.uname()
print("Tot: maquina  ")
print(maquina)
print("Indexant amb [] obtenim els valors individuals: " + maquina[0])

# Decidim en un funció del tipus de SO
so = platform.system();
if so == "Darwin":
    print ("Això és un MAC")
    print (platform.mac_ver() )
elif so == "Linux":
    print ("Això és un Linux")
    print (platform.libc_ver() )
elif so == "Windows":
    print ("Això és un Windows")
    print (platform.win32_ver() )
else:
    print ("No se que soc ...")

