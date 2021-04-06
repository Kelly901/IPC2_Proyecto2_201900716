from MatrizRectangulo import MatrizRectangulo
class NodoLRect:

    def __init__(self,id,nombre,nFila,nColumna):
        self.id=id
        self.nombre=nombre
        self.nFila=nFila
        self.nColumna=nColumna
        self.matriz=MatrizRectangulo()
        self.siguiente=None
        