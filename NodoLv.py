from MatrizVertical import MatrizVertical
class NodoLv:

    def __init__(self,id,nombre,nFila,nColumna):
        self.id=id
        self.nombre=nombre
        self.nFila=nFila
        self.nColumna=nColumna
        self.matriz=MatrizVertical()
        self.siguiente=None
        