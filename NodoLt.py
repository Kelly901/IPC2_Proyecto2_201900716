from MatrizTransp import MatrizTransp
class NodoLt:

    def __init__(self,id,nombre,nFila,nColumna):
        self.id=id
        self.nombre=nombre
        self.nFila=nFila
        self.nColumna=nColumna
        self.matriz=MatrizTransp()
        self.siguiente=None
        