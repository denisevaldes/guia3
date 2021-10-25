
archivo = open("ejemplo.txt")
lineas = archivo.readline()
#print(lineas)
#quit()

while lineas != "":
    lineas = archivo.readline()
    print(lineas, end = "")

#for linea in lineas:
#    print(linea)

#estamos diciendo antes de cerrar el archivo, conservalo 
#de forma segura 
archivo.close()



