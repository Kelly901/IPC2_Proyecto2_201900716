from MatrizAgregarV import MatrizAgregaV
class NodoLav:

    def __init__(self,id,nombre,nFila,nColumna):
        self.id=id
        self.nombre=nombre
        self.nFila=nFila
        self.nColumna=nColumna
        self.matriz=MatrizAgregaV()
        self.siguiente=None
        