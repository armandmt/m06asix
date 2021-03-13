import platform

print(platform.platform())
print("Processador: " + platform.processor())
print("Màquina: " + platform.machine())
print("Sistema: " + platform.system())
print("Versió SO: " + platform.version())
print("Release (Versió kernel): " + platform.release())
print("Node (Nom de xarxa) : " + platform.node())

print ("Això és un MAC? ")
print (platform.mac_ver() )

maquina = platform.uname()
print("Tot: maquina  ")
print(maquina)
print("Indexant amb [] obtenim els valors individuals: " + maquina[0])
