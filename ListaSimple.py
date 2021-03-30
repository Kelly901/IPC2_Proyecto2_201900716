from NodoL import NodoL
class ListaSimple:

    def __init__(self):
        self.cabeza=None


    #Metodo para insertar
    def insertar_final(self,nombre,nFila,nColumna,matriz):
        nuevo=NodoL(nombre,nFila,nColumna)
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
        cont=1
        while temp is not None:
            print(str(cont)+' nombre: '+temp.nombre+' no.Fila: '+str(temp.nFila)+' no.Columna: '+str(temp.nColumna))
            temp.matriz.recorrerFilas()
            cont+=1
            temp=temp.siguiente


    #Girar matriz de forma vertical

    def vertical(self):
        temp=self.cabeza
        cont=0
        while temp is not None:

           
            total=int(temp.nFila)*int(temp.nColumna)
            for i in range(total-1,-1,-1):
                print("hoed")
                print(i)
                temp.matriz.retornar(i)
                      
                           
            temp=temp.siguiente        
            