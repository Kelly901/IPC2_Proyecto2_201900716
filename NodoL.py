from Matriz import Matriz
class NodoL:

    def __init__(self,nombre,nFila,nColumna):
        self.nombre=nombre
        self.nFila=nFila
        self.nColumna=nColumna
        self.matriz=Matriz()
        self.siguiente=None
        