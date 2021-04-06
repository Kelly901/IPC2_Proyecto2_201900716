from NodoAh import NodoAh
from NodoEncabezadoAh import NodoEncabezadoAh
from EncabezadoAh import EncabezadoAh
class MatrizAgregaH:

    def __init__(self):

        self.encabezadoFilas= EncabezadoAh()
        self.encabezadoColumnas=EncabezadoAh()


    def insertar(self,fila,columna,valor):
        
        nuevo=NodoAh(fila,columna,valor)

        efilas=self.encabezadoFilas.getEncabezado(fila)

        if efilas==None:
            efilas=NodoEncabezadoAh(fila)
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
            eColumnas=NodoEncabezadoAh(columna)
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
                print(str(actual.columna)+"   "+actual.valor)
                actual=actual.derecha
            efila=efila.siguiente
        print(">>>>>>>>>>>>>>Fin<<<<<<<<<<<<<<<<<")   


    def retornarFila(self,fila):
        efila=self.encabezadoFilas.primero
        print(fila)
        cadena=""
        while efila!=None:
            actual=efila.acceso
            #print(efila)
            if int(actual.fila)==fila:
                print(actual.fila)
                while actual!=None:
                #print(actual.id)
                
                    #print("hola")  
                    #print(actual.fila)
                    #print(actual.columna)  
                    cadena+=actual.valor
                    
                    
                    actual=actual.derecha

                if cadena!="None":    
                    return cadena    
            efila=efila.siguiente  