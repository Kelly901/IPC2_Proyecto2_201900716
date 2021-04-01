from MatrizAgregaH import MatrizAgregaH
class NodoLAH:

    def __init__(self,id,nombre,nFila,nColumna):
        self.id=id
        self.nombre=nombre
        self.nFila=nFila
        self.nColumna=nColumna
        self.matriz=MatrizAgregaH()
        self.siguiente=None
        