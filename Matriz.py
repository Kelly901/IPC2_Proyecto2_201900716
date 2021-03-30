from Nodo import Nodo
from NodoEncabezado import NodoEncabezado
from Encabezado import Encabezado
class Matriz:

    def __init__(self):

        self.encabezadoFilas= Encabezado()
        self.encabezadoColumnas=Encabezado()


    def insertar(self,fila,columna,valor,cont):
        
        nuevo=Nodo(fila,columna,valor,cont)

        efilas=self.encabezadoFilas.getEncabezado(fila)

        if efilas==None:
            efilas=NodoEncabezado(fila)
            efilas.acceso=nuevo
            self.encabezadoFilas.setEncabezado(efilas)    
        else:
            if nuevo.columna< efilas.acceso.columna:
                nuevo.derecha=efilas.acceso
                efilas.acceso.izquierda=nuevo
                efilas.acceso=nuevo
            else:
                actual=efilas.acceso
                while actual.derecha!=None:
                    if nuevo.columna<actual.derecha.columna:
                        nuevo.derecha=actual.derecha
                        actual.derecha.izquierda=nuevo
                        nuevo.izquierda=actual
                        actual.derecha=nuevo
                        break
                    actual=actual.derecha

                if actual.derecha==None:
                    actual.derecha=nuevo
                    nuevo.izquierda=actual
        #Insercion encabezado por columna
        eColumnas=self.encabezadoColumnas.getEncabezado(columna)
        if eColumnas==None:
            eColumnas=NodoEncabezado(columna)
            eColumnas.acceso=nuevo
            self.encabezadoColumnas.setEncabezado(eColumnas)
        else:
            if nuevo.fila< eColumnas.acceso.fila:
                nuevo.abajo=eColumnas.acceso
                eColumnas.acceso.arriba=nuevo
                eColumnas.acceso=nuevo
            else:
                actual=eColumnas.acceso
                while actual.abajo!=None:
                    if nuevo.fila< actual.abajo.fila:
                        nuevo.abajo=actual.abajo
                        actual.abajo.arriba=nuevo
                        nuevo.arriba=actual
                        actual.abajo=nuevo
                        break
                    actual=actual.abajo
                if actual.abajo==None:
                    actual.abajo=nuevo    #se inserta al final de la lista
                    nuevo.arriba=actual
                    

    def recorrerFilas(self):
        efila=self.encabezadoFilas.primero
        print(">>>>>>>Recorrer por fila<<<<<<<<<<<")
        
        while efila!=None:
            actual=efila.acceso
            print("\nFila  "+str(actual.fila))
            print("Columna valor")
            while actual!=None:
                print(str(actual.columna)+"   id:"+str(actual.id)+actual.valor)
                actual=actual.derecha
            efila=efila.siguiente
        print(">>>>>>>>>>>>>>Fin<<<<<<<<<<<<<<<<<")   


    def retornar(self,id):
        efila=self.encabezadoFilas.primero

        while efila!=None:
            actual=efila.acceso
            print(efila)
            while actual!=None:
                if actual.id==id:
                    print(actual.valor)     
                    actual=actual.derecha
            efila=efila.siguiente            
'''m=Matriz()
m.insertar(1,0,"hola")
m.insertar(0,0,"adios")
m.recorrerFilas()'''