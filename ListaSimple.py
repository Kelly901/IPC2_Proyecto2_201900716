from NodoL import NodoL
from ListaSimpleH import ListaSimpleH
from MatrizHorizontal import MatrizHorizontal
from ListaSimpleV import ListaSimpleV
from MatrizVertical import MatrizVertical
from ListaSimpleLimpiar import ListaSimpleLimpiar
from MatrizLimpiar import MatrizLimpiar
from ListaSimpleAgregarH import ListaSimpleAgregarH
from MatrizAgregaH import MatrizAgregaH
from ListaSimpleTransp import ListaSimpleTransp
from MatrizTransp import MatrizTransp
from ListaSimpleAgV import ListaSimpleAgV
from MatrizAgregarV import MatrizAgregaV
from ListaSimpleRectangulo import ListaSimpleRectangulo
from MatrizRectangulo import MatrizRectangulo
from Matriz import Matriz



class ListaSimple:
    # Lista en donde se almacena la matriz que se giro de forma horizontal
    listaH = ListaSimpleH() 
    # Lista en donde se alamacena la matriz que se giro de forma vertical
    listaV = ListaSimpleV()
    # Lista para almacenar las matrices cuando se limpiar un area
    listaLimpiar = ListaSimpleLimpiar()
    #Lista para almacenar un matriz agregando una linea horizontal.
    listaAgregaH=ListaSimpleAgregarH()
    #Lista para alamcenar una matriz transpuesta
    listaTranspuesta=ListaSimpleTransp()
    #Lista para almacena una matriz agregando una linea vertical
    listaVertical=ListaSimpleAgV()
    #Lista para agregar un rectangulo
    listaRectangulo=ListaSimpleRectangulo()
    def __init__(self):
        self.cabeza = None

    # Metodo para insertar
    def insertar_final(self, id, nombre, nFila, nColumna, matriz):
        nuevo = NodoL(id, nombre, nFila, nColumna)
        nuevo.matriz = matriz

        # Lista
        if self.cabeza == None:
            self.cabeza = nuevo
        else:
            auxiliar = self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar = auxiliar.siguiente
            auxiliar.siguiente = nuevo

    # Metodo para mostrar en consola
    def mostrar(self):
        temp = self.cabeza

        while temp is not None:
            print(str(temp.id)+' nombre: '+temp.nombre+' no.Fila: ' +
                  str(temp.nFila)+' no.Columna: '+str(temp.nColumna))
            temp.matriz.recorrerFilas()

            temp = temp.siguiente

    # Girar matriz de forma Horizontal

    def horizontal(self, id):
        # Matriz
        matriz = MatrizHorizontal()
        #

        temp = self.cabeza
        cont = 0
        cadena = ""
        fila = 0
        columna = 0
        nombre = ""
        while temp is not None:
            if temp.id == id:

                nombre = temp.nombre
                total = int(temp.nFila)*int(temp.nColumna)
                fila = int(temp.nFila)
                columna = int(temp.nColumna)
                for i in range(fila-1, -1, -1):
                    # print("hoed")
                    # print(i)
                    print("valor ")
                    print(temp.matriz.retornarFila(i))
                    cadena += str(temp.matriz.retornarFila(i))

            temp = temp.siguiente
        print(cadena)
        c = 0
        for i in range(fila):
            for j in range(columna):

                matriz.insertar(i, j, cadena[c])
                print("\t", cadena[c], end=" ")
                c += 1
            print()
        self.listaH.insertar_final(id, nombre, fila, columna, matriz)
        print("________________")
        print(self.listaH.mostrar())
    # Girar matriz de forma vertical

    def vertical(self, id):
        # Lista de la matriz ortogonal
        matriz = MatrizVertical()
        #
        temp = self.cabeza
        cont = 0
        cadena = ""
        fila = 0
        columna = 0
        nombre = ""
        while temp is not None:
            if temp.id == id:

                total = int(temp.nFila)*int(temp.nColumna)
                fila = int(temp.nFila)
                nombre = temp.nombre
                columna = int(temp.nColumna)
                for i in range(columna-1, -1, -1):
                    # print("hoed")
                    # print(i)
                    print("valor ")
                    print(temp.matriz.retornarColumna(i))
                    cadena += str(temp.matriz.retornarColumna(i))

            temp = temp.siguiente
        print(cadena)
        c = 0
        for i in range(columna):
            for j in range(fila):

                matriz.insertar(j, i, cadena[c])
                # print("\t",cadena[c],end=" ")
                c += 1
            # print()
        self.listaV.insertar_final(id, nombre, fila, columna, matriz)
        print("_____________-")
        self.listaV.mostrar()

    # Transpuesta de la matriz
    def transpuesta(self, id):
        matriz=MatrizTransp()
        # matriz=MatrizVertical()
        #
        temp = self.cabeza
        cont = 0
        cadena = ""
        fila = 0
        columna = 0
        nombre = ""
        while temp is not None:
            if temp.id == id:

                total = int(temp.nFila)*int(temp.nColumna)
                fila = int(temp.nFila)
                nombre = temp.nombre
                columna = int(temp.nColumna)
                for i in range(columna):
                    # print("hoed")
                    # print(i)
                    print("valor ")
                    print(temp.matriz.retornarTranspuesta(i))
                    cadena += str(temp.matriz.retornarTranspuesta(i))

            temp = temp.siguiente
        print(cadena)
        c = 0
        print("   Transpuesta")
        for i in range(columna):
            for j in range(fila):

                # matriz.insertar(j, i, cadena[c])
                print("\t", cadena[c], end=" ")
                matriz.insertar(i,j,cadena[c])
                
                c += 1
            print()
        # self.listaV.insertar_final(id,nombre,fila,columna,matriz)
        print("_____________-")
        # self.listaV.mostrar()
        self.listaTranspuesta.insertar_final(id,nombre,columna,fila,matriz)
    # Metodo para limpiar

    def limpiarArea(self, id, f1, c1, f2, c2):
        # (1,1)(2,2)

        temp = self.cabeza
        cont = 0
        cadena = ""
        cadena2 = ""
        fila = 0
        columna = 0
        nombre = ""
        matriz1=Matriz()
        matriz = MatrizLimpiar()
        numeros = ""
        while temp is not None:
            if temp.id == id:

                nombre = temp.nombre
                total = int(temp.nFila)*int(temp.nColumna)
                fila = int(temp.nFila)
                columna = int(temp.nColumna)
                for i in range(fila):
                    cadena += temp.matriz.retornarFila(i)

                '''for i in range(f1,f2+1):
                    # print("hoed")
                    # print(i)
                    for j in range(c1,c2+1):
                        print("valor ")
                        # print(temp.matriz.retornaLimpiarA(i,j))
                        print("(",i,j,")")


                        # matriz.insertar(i,j,"-")
                        cadena+="-"
                        # str(temp.matriz.retornaLimpiarA(i,j))
                        # matriz.insertar(i,j,"-")
                        numeros+=str(i)
                        numeros+=str(j)'''

            temp = temp.siguiente
        # -----------
        c = 0
        for i in range(fila):
            for j in range(columna):
                matriz1.insertar(i,j,cadena[c],c)
                c += 1

        matriz1.recorrerFilas() 
        
        efila=matriz1.encabezadoFilas.primero
        for i in range(f1,f2+1):
            for j in range(c1,c2+1):
                print(i,j)
                matriz1.retornaLimpiarA(i,j)
        #
        efila=matriz1.encabezadoFilas.primero
        while efila !=None:
            actual=efila.acceso
            while actual!=None:
                matriz.insertar(actual.fila,actual.columna,actual.valor)

                actual=actual.derecha
            efila=efila.siguiente    
        
        matriz1.recorrerFilas()
        matriz.recorrerFilas()
        self.listaLimpiar.insertar_final(id,nombre,fila,columna,matriz)
  
        print("________________")
        self.listaLimpiar.mostrar()

    #Agrega linea horizontal
    def agregar_linea_horizontal(self,id,f1,c1,c2):
        temp = self.cabeza
    
        cadena = ""
    
        fila = 0
        columna = 0
        nombre = ""
        matriz1=Matriz()
        matriz=MatrizAgregaH()
      
  
        while temp is not None:
            if temp.id == id:

                nombre = temp.nombre
                total = int(temp.nFila)*int(temp.nColumna)
                fila = int(temp.nFila)
                columna = int(temp.nColumna)
                for i in range(fila):
                    cadena += temp.matriz.retornarFila(i)


            temp = temp.siguiente
        # -----------
        c = 0
        for i in range(fila):
            for j in range(columna):
                matriz1.insertar(i,j,cadena[c],c)
                c += 1

        matriz1.recorrerFilas() 
        
        efila=matriz1.encabezadoFilas.primero
        #_____________________________ 
        for i in range(f1):
            for j in range(c1,c2+1):
                #print(i,j)
                matriz1.fila_agregada(f1,j)
        #----------------------------

        matriz1.recorrerFilas()
        #____________________________
        efila=matriz1.encabezadoFilas.primero
        while efila !=None:
            actual=efila.acceso
            while actual!=None:
                matriz.insertar(actual.fila,actual.columna,actual.valor)

                actual=actual.derecha
            efila=efila.siguiente    
        
        #matriz1.recorrerFilas()
        #matriz.recorrerFilas()
        self.listaAgregaH.insertar_final(id,nombre,fila,columna,matriz)
        print("________________")
        self.listaAgregaH.mostrar()

    #Metodo para agergar un linea horizontal

    def agregar_linea_vertical(self,id,f1,f2,col):
        temp = self.cabeza
    
        cadena = ""
    
        fila = 0
        columna = 0
        nombre = ""
        matriz1=Matriz()
        matriz=MatrizAgregaV()
      
  
        while temp is not None:
            if temp.id == id:

                nombre = temp.nombre
                total = int(temp.nFila)*int(temp.nColumna)
                fila = int(temp.nFila)
                columna = int(temp.nColumna)
                for i in range(fila):
                    cadena += temp.matriz.retornarFila(i)


            temp = temp.siguiente
        # -----------
        c = 0
        for i in range(fila):
            for j in range(columna):
                matriz1.insertar(i,j,cadena[c],c)
                c += 1

        matriz1.recorrerFilas() 
        
        efila=matriz1.encabezadoFilas.primero
        #_____________________________ 
        for i in range(f1,f2+1):
            for j in range(col):
                #print(i,j)
                matriz1.columna_agregada(i,col)
        #----------------------------
        matriz1.recorrerFilas()
        #_________________
        efila=matriz1.encabezadoFilas.primero
        #_____________________________ 

        
        #____________________________
        efila=matriz1.encabezadoFilas.primero
        while efila !=None:
            actual=efila.acceso
            while actual!=None:
                matriz.insertar(actual.fila,actual.columna,actual.valor)

                actual=actual.derecha
            efila=efila.siguiente    
        
        self.listaVertical.insertar_final(id,nombre,fila,columna,matriz)
    
    #Agregar un rectangulo

    def agrega_un_rectangulo(self,id,x,y,filas,columnas):
        temp = self.cabeza
        cont = 0
        cadena = ""
        cadena2 = ""
        fila = 0
        columna = 0
        nombre = ""
        matriz1=Matriz()
        matriz=MatrizRectangulo()
        #matriz = MatrizLimpiar()
        numeros = ""
        while temp is not None:
            if temp.id == id:

                nombre = temp.nombre
                total = int(temp.nFila)*int(temp.nColumna)
                fila = int(temp.nFila)
                columna = int(temp.nColumna)
                for i in range(fila):
                    cadena += temp.matriz.retornarFila(i)

            temp = temp.siguiente
        # -----------
        c = 0
        for i in range(fila):
            for j in range(columna):
                matriz1.insertar(i,j,cadena[c],c)
                c += 1

        matriz1.recorrerFilas() 
        
        efila=matriz1.encabezadoFilas.primero
        for i in range(x,x+filas):
            for j in range(y,y+columnas):
                print(i,j)
                matriz1.agregarRectangulo(i,j)
        
        matriz1.recorrerFilas()

        #______
        efila=matriz1.encabezadoFilas.primero
        while efila !=None:
            actual=efila.acceso
            while actual!=None:
                matriz.insertar(actual.fila,actual.columna,actual.valor)

                actual=actual.derecha
            efila=efila.siguiente    
        
        self.listaRectangulo.insertar_final(id,nombre,fila,columna,matriz)
        
        
