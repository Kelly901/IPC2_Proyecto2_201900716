from graphviz import Digraph
from graphviz import Graph
from CargarArchivo import CargarArchivo


class Imagen:

    def crear_imagen_original(self,id):
        
        cadena=""
        cuerpo=""
        temp=CargarArchivo.lista.cabeza
        fila=0
        columna=0
        etiqueta=""
        nombre=""
        encabezado=[]
        
        while temp is not None:
            if temp.id==id:
                fila = int(temp.nFila)
                columna = int(temp.nColumna) 
                nombre=temp.nombre   
                for i in range(fila):
                    cadena+=temp.matriz.retornarFila(i)
                   
            temp = temp.siguiente    
        #------------------------
        #------------------------
        c=0
        #Colocar el nombre de la etiqueta
        etiqueta="<tr><td>"+nombre+"</td>"
         #Colocar el encabezado de la columna
        for i in range(1,columna+1):
            etiqueta+="<td>"+str(i)+"</td>"
        etiqueta+="</tr>"    
        #Colocar el encabezado de la fila
        
            
        #Colocar el valor en cada celda
        for i in range(1,fila+1):
            etiqueta+="<tr>"
            etiqueta+="<td>"+str(i)+"</td>"

            for j in range(columna):

                if cadena[c]=="-":
                    etiqueta+="<td> </td>"
                else:
                    etiqueta+="<td>"+cadena[c]+"</td>"
                c+=1
            etiqueta+="</tr>"


        g=Digraph('G',format='png')
        g.attr(label='Matriz Original')
        cuerpo='''<<table >
                '''+etiqueta+'''   
                </table>>'''   
        g.node('S',label=cuerpo,shape='none',color='blue')

        g.render('imagen')
    
    def crear_imagen_rotacionH(self,id):
        cadena=""
        cuerpo=""
        temp=CargarArchivo.lista.listaH.cabeza
        fila=0
        columna=0
        etiqueta=""
        nombre=""
        encabezado=[]
        
        while temp is not None:
            if temp.id==id:
                fila = int(temp.nFila)
                columna = int(temp.nColumna) 
                nombre=temp.nombre   
                for i in range(fila):
                    cadena+=temp.matriz.retornarFila(i)
                   
            temp = temp.siguiente    
        #------------------------
        #------------------------
        c=0
        #Colocar el nombre de la etiqueta
        etiqueta="<tr><td>"+nombre+"</td>"
         #Colocar el encabezado de la columna
        for i in range(1,columna+1):
            etiqueta+="<td>"+str(i)+"</td>"
        etiqueta+="</tr>"    
        #Colocar el encabezado de la fila
        
            
        #Colocar el valor en cada celda
        for i in range(1,fila+1):
            etiqueta+="<tr>"
            etiqueta+="<td>"+str(i)+"</td>"

            for j in range(columna):
                
                if cadena[c]=="-":
                    etiqueta+="<td> </td>"
                else:
                    etiqueta+="<td>"+cadena[c]+"</td>"
                c+=1
            etiqueta+="</tr>"


        g=Digraph('G',format='png')
        g.attr(label='Rotación Horizontal')
        cuerpo='''<<table >
                '''+etiqueta+'''   
                </table>>'''   
        g.node('S',label=cuerpo,shape='none',color='blue')

        g.render('imagenHorizontal')
    
    #Generar imagen de rotación vertical
    def crear_imagen_rotacionV(self,id):
        cadena=""
        cuerpo=""
        temp=CargarArchivo.lista.listaV.cabeza
        fila=0
        columna=0
        etiqueta=""
        nombre=""
        encabezado=[]
        
        while temp is not None:
            if temp.id==id:
                fila = int(temp.nFila)
                columna = int(temp.nColumna) 
                nombre=temp.nombre   
                for i in range(fila):
                    cadena+=temp.matriz.retornarFila(i)
                   
            temp = temp.siguiente    
        #------------------------
        #------------------------
        c=0
        #Colocar el nombre de la etiqueta
        etiqueta="<tr><td>"+nombre+"</td>"
         #Colocar el encabezado de la columna
        for i in range(1,columna+1):
            etiqueta+="<td>"+str(i)+"</td>"
        etiqueta+="</tr>"    
        #Colocar el encabezado de la fila
        
            
        #Colocar el valor en cada celda
        for i in range(1,fila+1):
            etiqueta+="<tr>"
            etiqueta+="<td>"+str(i)+"</td>"

            for j in range(columna):
                
                if cadena[c]=="-":
                    etiqueta+="<td> </td>"
                else:
                    etiqueta+="<td>"+cadena[c]+"</td>"
                c+=1
            etiqueta+="</tr>"


        g=Digraph('G',format='png')
        g.attr(label='Rotación Vertical')
        cuerpo='''<<table >
                '''+etiqueta+'''   
                </table>>'''   
        g.node('S',label=cuerpo,shape='none',color='blue')

        g.render('imagenVertical')
                    
    #Generar imagen de rotación vertical
    def crear_imagen_transpuesta(self,id):
        cadena=""
        cuerpo=""
        temp=CargarArchivo.lista.listaTranspuesta.cabeza
        fila=0
        columna=0
        etiqueta=""
        nombre=""
        encabezado=[]
        
        while temp is not None:
            if temp.id==id:
                fila = int(temp.nFila)
                columna = int(temp.nColumna) 
                nombre=temp.nombre   
                for i in range(fila):
                    cadena+=temp.matriz.retornarFila(i)
                   
            temp = temp.siguiente    
        #------------------------
        #------------------------
        c=0
        #Colocar el nombre de la etiqueta
        etiqueta="<tr><td>"+nombre+"</td>"
         #Colocar el encabezado de la columna
        for i in range(1,columna+1):
            etiqueta+="<td>"+str(i)+"</td>"
        etiqueta+="</tr>"    
        #Colocar el encabezado de la fila
        
            
        #Colocar el valor en cada celda
        for i in range(1,fila+1):
            etiqueta+="<tr>"
            etiqueta+="<td>"+str(i)+"</td>"

            for j in range(columna):
                
                if cadena[c]=="-":
                    etiqueta+="<td> </td>"
                else:
                    etiqueta+="<td>"+cadena[c]+"</td>"
                c+=1
            etiqueta+="</tr>"


        g=Digraph('G',format='png')
        g.attr(label='Transpuesta')
        cuerpo='''<<table >
                '''+etiqueta+'''   
                </table>>'''   
        g.node('S',label=cuerpo,shape='none',color='blue')

        g.render('imagenTranspuesta')

    #Crear imagen con la zona limpia
    def crear_imagen_LimpiarZona(self,id):
        cadena=""
        cuerpo=""
        temp=CargarArchivo.lista.listaLimpiar.cabeza
        fila=0
        columna=0
        etiqueta=""
        nombre=""
        encabezado=[]
        
        while temp is not None:
            if temp.id==id:
                fila = int(temp.nFila)
                columna = int(temp.nColumna) 
                nombre=temp.nombre   
                for i in range(fila):
                    cadena+=temp.matriz.retornarFila(i)
                   
            temp = temp.siguiente    
        #------------------------
        #------------------------
        c=0
        #Colocar el nombre de la etiqueta
        etiqueta="<tr><td>"+nombre+"</td>"
         #Colocar el encabezado de la columna
        for i in range(1,columna+1):
            etiqueta+="<td>"+str(i)+"</td>"
        etiqueta+="</tr>"    
        #Colocar el encabezado de la fila
        
            
        #Colocar el valor en cada celda
        for i in range(1,fila+1):
            etiqueta+="<tr>"
            etiqueta+="<td>"+str(i)+"</td>"

            for j in range(columna):
                
                if cadena[c]=="-":
                    etiqueta+="<td> </td>"
                else:
                    etiqueta+="<td>"+cadena[c]+"</td>"
                c+=1
            etiqueta+="</tr>"


        g=Digraph('G',format='png')
        g.attr(label='Limpiar zona')
        cuerpo='''<<table >
                '''+etiqueta+'''   
                </table>>'''   
        g.node('S',label=cuerpo,shape='none',color='blue')

        g.render('imagenLimpiarZona')  

    #Crear imagen agregar linea horizontal
    def crear_imagen_agregaH(self,id):
        cadena=""
        cuerpo=""
        temp=CargarArchivo.lista.listaAgregaH.cabeza
        fila=0
        columna=0
        etiqueta=""
        nombre=""
        encabezado=[]
        
        while temp is not None:
            if temp.id==id:
                fila = int(temp.nFila)
                columna = int(temp.nColumna) 
                nombre=temp.nombre   
                for i in range(fila):
                    cadena+=temp.matriz.retornarFila(i)
                   
            temp = temp.siguiente    
        #------------------------
        #------------------------
        c=0
        #Colocar el nombre de la etiqueta
        etiqueta="<tr><td>"+nombre+"</td>"
         #Colocar el encabezado de la columna
        for i in range(1,columna+1):
            etiqueta+="<td>"+str(i)+"</td>"
        etiqueta+="</tr>"    
        #Colocar el encabezado de la fila
        
            
        #Colocar el valor en cada celda
        for i in range(1,fila+1):
            etiqueta+="<tr>"
            etiqueta+="<td>"+str(i)+"</td>"

            for j in range(columna):
                
                if cadena[c]=="-":
                    etiqueta+="<td> </td>"
                else:
                    etiqueta+="<td>"+cadena[c]+"</td>"
                c+=1
            etiqueta+="</tr>"


        g=Digraph('G',format='png')
        g.attr(label='Agregar Linea horizontal')
        cuerpo='''<<table >
                '''+etiqueta+'''   
                </table>>'''   
        g.node('S',label=cuerpo,shape='none',color='blue')

        g.render('imagenAgregarH')    

    #Imagen agregando una linea verticl
    def crear_imagen_agregaV(self,id):
        cadena=""
        cuerpo=""
        temp=CargarArchivo.lista.listaVertical.cabeza
        fila=0
        columna=0
        etiqueta=""
        nombre=""
        encabezado=[]
        
        while temp is not None:
            if temp.id==id:
                fila = int(temp.nFila)
                columna = int(temp.nColumna) 
                nombre=temp.nombre   
                for i in range(fila):
                    cadena+=temp.matriz.retornarFila(i)
                   
            temp = temp.siguiente    
        #------------------------
        #------------------------
        c=0
        #Colocar el nombre de la etiqueta
        etiqueta="<tr><td>"+nombre+"</td>"
         #Colocar el encabezado de la columna
        for i in range(1,columna+1):
            etiqueta+="<td>"+str(i)+"</td>"
        etiqueta+="</tr>"    
        #Colocar el encabezado de la fila
        
            
        #Colocar el valor en cada celda
        for i in range(1,fila+1):
            etiqueta+="<tr>"
            etiqueta+="<td>"+str(i)+"</td>"

            for j in range(columna):
                
                if cadena[c]=="-":
                    etiqueta+="<td> </td>"
                else:
                    etiqueta+="<td>"+cadena[c]+"</td>"
                c+=1
            etiqueta+="</tr>"


        g=Digraph('G',format='png')
        g.attr(label='Agregar Linea Vertical')
        cuerpo='''<<table >
                '''+etiqueta+'''   
                </table>>'''   
        g.node('S',label=cuerpo,shape='none',color='blue')

        g.render('imagenAgregarV')          

    #Agregar rectangulo
    def crear_imagen_agregaRec(self,id):
        cadena=""
        cuerpo=""
        temp=CargarArchivo.lista.listaRectangulo.cabeza
        fila=0
        columna=0
        etiqueta=""
        nombre=""
        encabezado=[]
        
        while temp is not None:
            if temp.id==id:
                fila = int(temp.nFila)
                columna = int(temp.nColumna) 
                nombre=temp.nombre   
                for i in range(fila):
                    cadena+=temp.matriz.retornarFila(i)
                   
            temp = temp.siguiente    
        #------------------------
        #------------------------
        c=0
        #Colocar el nombre de la etiqueta
        etiqueta="<tr><td>"+nombre+"</td>"
         #Colocar el encabezado de la columna
        for i in range(1,columna+1):
            etiqueta+="<td>"+str(i)+"</td>"
        etiqueta+="</tr>"    
        #Colocar el encabezado de la fila
        
            
        #Colocar el valor en cada celda
        for i in range(1,fila+1):
            etiqueta+="<tr>"
            etiqueta+="<td>"+str(i)+"</td>"

            for j in range(columna):
                
                if cadena[c]=="-":
                    etiqueta+="<td> </td>"
                else:
                    etiqueta+="<td>"+cadena[c]+"</td>"
                c+=1
            etiqueta+="</tr>"


        g=Digraph('G',format='png')
        g.attr(label='Agregar Rectangulo')
        cuerpo='''<<table >
                '''+etiqueta+'''   
                </table>>'''   
        g.node('S',label=cuerpo,shape='none',color='blue')

        g.render('imagenAgregarRec')          
