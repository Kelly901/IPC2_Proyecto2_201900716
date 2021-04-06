from NodoLRect import NodoLRect
class ListaSimpleRectangulo:

    def __init__(self):
        self.cabeza=None


    #Metodo para insertar
    def insertar_final(self,id,nombre,nFila,nColumna,matriz):
        nuevo=NodoLRect(id,nombre,nFila,nColumna)
        nuevo.matriz=matriz

        #Lista
        if self.cabeza==None:
            self.cabeza=nuevo
        else:
            auxiliar=self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar=auxiliar.siguiente
            auxiliar.siguiente=nuevo

    #Metodo para mostrar en consola
    def mostrar(self):
        temp=self.cabeza
       
        while temp is not None:
            print(str(temp.id)+' nombre: '+temp.nombre+' no.Fila: '+str(temp.nFila)+' no.Columna: '+str(temp.nColumna))
            temp.matriz.recorrerFilas()
         
            temp=temp.siguiente


  



