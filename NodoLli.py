from MatrizLimpiar import MatrizLimpiar
class NodoLli:

    def __init__(self,id,nombre,nFila,nColumna):
        self.id=id
        self.nombre=nombre
        self.nFila=nFila
        self.nColumna=nColumna
        self.matriz=MatrizLimpiar()
        self.siguiente=None
        