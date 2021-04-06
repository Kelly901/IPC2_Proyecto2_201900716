class NodoEncabezadoAv:
    def __init__(self,id):
        self.id=id
        self.siguiente=None
        self.anterior=None
        #Acceso al nodo interno de la matriz
        self.acceso=None