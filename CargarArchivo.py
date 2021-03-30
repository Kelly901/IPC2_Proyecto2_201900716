import xml.etree.ElementTree as ET
from ListaSimple import ListaSimple
from Matriz import Matriz


class CargarArchivo:
    lista=ListaSimple()
    def procesar(self,ruta1):
        ruta=ruta1
        tree=ET.parse(ruta)
        
        root=tree.getroot()
        cont=0
        cont2=0
        fila=0
        columna=0
        cadena=""
        cont3=0
        nombre=""

        #Fors
        for element in root:
            #print(element)
            matriz=Matriz()
            if element.iter('matriz'):
                #Obtener el nombre
                for i in element.iter('nombre'):
                    nombre=i.text
                #Obtener el numero de filas    
                for i in element.iter('filas'):
                    fila=i.text
                #Obtener el numero de columnas    
                for i in element.iter('columnas'):
                    columna=i.text
                #Obtener los datos que esta en el nodo con nombre Imagen    
                for i in element.iter('imagen'):
                    #print(">"+i.text+"<")
                    for r in i.text:
                    
                        if r=="\n":
                            cont+=1

                        if r=="*" or r=="-":
                            #cont2+=1
                            cadena+=r
                            #print(r)
                    #print(fila)
                    #print(columna)

                    #Distibruir los datos de la imagen en la matriz ortogonal
                    for i in range(int(fila)):
                        
                        for j in range(int(columna)):
                            
                            #print("fila "+str(i)+" columna "+str(j)+" valor "+cadena[cont3])
                            matriz.insertar(i,j,cadena[cont3],cont3)
                            cont3+=1
                    #Guardar las matrices
                    self.lista.insertar_final(nombre,fila,columna,matriz)         
                    #print("_______________")
                    #self.matriz.recorrerFilas()
                    cadena=""
                    cont3=0
                    #print(cadena)
        self.lista.mostrar() 
        print("_______________________")
        self.lista.vertical()          
               