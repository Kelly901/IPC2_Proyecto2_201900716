from MatrizHorizontal import MatrizHorizontal
class NodoLh:

    def __init__(self,id,nombre,nFila,nColumna):
        self.id=id
        self.nombre=nombre
        self.nFila=nFila
        self.nColumna=nColumna
        self.matriz=MatrizHorizontal()
        self.siguiente=None
        