from tkinter import*
from tkinter import filedialog as FileDialog
from tkinter import ttk
from CargarArchivo import CargarArchivo
import sys
from Imagen import Imagen
cargarArchivo=CargarArchivo()
imagen=Imagen()
class GUI:
    raiz=Tk()
    frame=Frame()
    #
    frameP=Frame()
    id=0
    #Posicion en x
    pos_x=0
    #Poscion en y
    pos_y=0
    #fila
    f=0
    #Columna
    co=0

    #
    caja1=ttk.Entry(frame)
    #
    caja2=ttk.Entry(frame)
    #
    caja3=ttk.Entry(frame)
    #
    caja4=ttk.Entry(frame)
    #
    lista_opciones=ttk.Combobox(frame,width=17)
    #Lista de las matrices individuaes
    lista_matrices=ttk.Combobox(frame,width=17)
    #Lista de las operaciones
    lista_operaciones=ttk.Combobox(frame,width=17)
    #widget original
    widget=Label()
    #widget horizontal
    widgetH=Label()
    #Widget vertical
    widgetV=Label()
    #Widget Transpuesta
    widgetT=Label()
    #widget limpiar zona
    widgetLimpiar=Label()
    #widget agregar fila horizontal
    widgetAg=Label()
    #widget agregar fila vertical
    widgetAv=Label()
    #Widget agregar Rectangulo
    widgetRec=Label()

    def interfaz(self):
        
        self.raiz.title("Principal")
        self.raiz.geometry("810x690")
        #Frame
       
        self.frameP.place(x=0,y=0)
        self.frameP.config(width="810",height="90")
        self.frameP.config(bg="black")
        self.frame.place(x=0,y=90)
        self.frame.config(width="810",height="500")
        self.frame.config(bg="black")

        #Agregar boton
        boton1=Button(self.frameP,text="Cargar Archivo",command=self.abrirArchivo,width="20",height="3",activeforeground="blue",activebackground="black",borderwidth=10)
        boton1.place(x=0,y=10)
        #
        #Boton operaciones
        boton2=Button(self.frameP,text="Operaciones",command=self.lista_de_opciones,width="20",height="3",activeforeground="blue",activebackground="black",borderwidth=10)

        boton2.place(x=170,y=10)
        #Boton reportes
        boton3=Button(self.frameP,text="Reportes",command=self.vertical,width="20",height="3",activeforeground="blue",activebackground="black",borderwidth=10)
        boton3.place(x=340,y=10)
        #Boton Ayuda
        boton4=Button(self.frameP,text="Ayuda",command=self.ayuda,width="20",height="3",activeforeground="blue",activebackground="black",borderwidth=10)
        boton4.place(x=510,y=10)
        #Boton para salir
        salir=Button(self.frameP,text="Salir",command=sys.exit,width="15",height="3",activeforeground="blue",activebackground="black",borderwidth=10)
        salir.place(x=680,y=10)
        #
        
        #
        self.raiz.mainloop()

        #


    def abrirArchivo(self):
        fichero=FileDialog.askopenfilename(title="Abrir un fichero")
        fi=open(fichero,'r')
        cargarArchivo.procesar(fi)
        print(fi)

    def suma(self):
        print("hola") 

    #Prueba
    def vertical(self):
        print("")

    #Escoger la cantidad de matrices
   

    def lista_de_opciones(self):
       
        
        self.lista_matrices.place(x=10,y=25)   
        temp=CargarArchivo.lista.cabeza
        ids=[]
        opciones=[]
        label=Label(self.frame,text="matricez",fg="blue")
        label.place(x=10,y=0)
        #___________________________
        while temp is not None:
            opciones.append(temp.nombre)
            ids.append(id)
            temp=temp.siguiente
        #_______________________________
        
        self.lista_matrices['values']=opciones
      
        #__________Boton______________
        aceptar=Button(self.frame,text="Aceptar",command=self.obtener_numero2,width="8",height="2",activeforeground="blue",activebackground="black",borderwidth=10)
        aceptar.place(x=150,y=10)
        print("adios")

    #Obtener el numero 2
    def obtener_numero2(self):
        self.id=int(self.lista_matrices.current())+1
        
        print(self.id) 
        self.operaciones_de_una()   
        
    # Escoger operación de una matriz
    def operaciones_de_una(self):  
        label=Label(self.frame,text="Operaciones",fg="blue")
        label.place(x=255,y=0)
        self.lista_operaciones.place(x=255,y=25)   
        temp=CargarArchivo.lista.cabeza
        ids=[]
        operaciones=['Rotación Horizontal','Rotación Vertical','Transpuesta','Limpiar zona','Agregar línea horizontal','Agregar línea vertical','Agregar rectángulo','Agregar triangulo Rectangulo','Unión A,B', 'Intersección A,B','Diferencia','Diferencia Simétrica']
        
        #_______________________________
        
        self.lista_operaciones['values']=operaciones
        aceptar=Button(self.frame,text="Aceptar",command=self.obtener_numero3,width="8",height="2",activeforeground="blue",activebackground="black",borderwidth=10)
        aceptar.place(x=385,y=10)
        #Posicion en x
        Label(self.frame,text="Posición en X",fg="blue").place(x=495,y=0)
        
        self.caja1.place(x=495,y=25)
        
        #Posicion en y
        Label(self.frame,text="Posición en Y",fg="blue").place(x=635,y=0)
        
        self.caja2.place(x=625,y=25)
        
        #Numero de filas
        Label(self.frame,text="Número de fila",fg="blue").place(x=495,y=55)
        
        self.caja3.place(x=495,y=85)
        
        #Numero de columna
        Label(self.frame,text="Número de columna",fg="blue").place(x=635,y=55)
        
        self.caja4.place(x=625,y=85)
        
        #Boton para limipar
      

    #Escoger las operaciones
    def obtener_numero3(self):
        if self.widget!=None:
            self.widget.destroy()
        if self.widgetH!=None:
            self.widgetH.destroy()
        if self.widgetV!=None:
            self.widgetV.destroy()
        if self.widgetT!=None:
            self.widgetT.destroy()    
        if self.widgetLimpiar!=None:
            self.widgetLimpiar.destroy()    
        if self.widgetAg!=None:
            self.widgetAg.destroy()
        if self.widgetAv!=None:
            self.widgetAv.destroy()   
        if self.widgetRec!=None:
            self.widgetRec.destroy()     
        #
        print(self.caja1.get())
        self.pos_x=int(self.caja1.get())-1
        #
        self.pos_y=int(self.caja2.get())-1
        #
        self.f=int(self.caja3.get())-1
        #
        self.co=int(self.caja4.get())-1
        #ifs par las operaciones    
        #
        numero=int(self.lista_operaciones.current())+1
        if numero==1:
            print("rotacion Horizonal")
            #Imagen original
            CargarArchivo.lista.horizontal(self.id)
            imagen.crear_imagen_original(self.id)
            
            imagen_original=PhotoImage(file="imagen.png")
            self.widget=Label(self.frame,image=imagen_original)
            self.widget.place(x=10,y=90)
            #Imagen horizonatl
            imagen.crear_imagen_rotacionH(self.id)
            imagen_horizontal=PhotoImage(file="imagenHorizontal.png")
            self.widgetH=Label(self.frame,image=imagen_horizontal)
            self.widgetH.place(x=420,y=90)

            self.raiz.mainloop()
        elif numero==2:
            #Imagen original
            CargarArchivo.lista.vertical(self.id)
            imagen.crear_imagen_original(self.id)
            
            imagen_original=PhotoImage(file="imagen.png")
            self.widget=Label(self.frame,image=imagen_original)
            self.widget.place(x=10,y=90)
            #Imagen vertical
            imagen.crear_imagen_rotacionV(self.id)
            imagen_vertical=PhotoImage(file="imagenVertical.png")
            self.widgetV=Label(self.frame,image=imagen_vertical)
            self.widgetV.place(x=420,y=90)
            self.raiz.mainloop()
            print("rotacion Vertical")
        elif numero==3:
            CargarArchivo.lista.transpuesta(self.id)
            imagen.crear_imagen_original(self.id)
            
            imagen_original=PhotoImage(file="imagen.png")
            self.widget=Label(self.frame,image=imagen_original)
            self.widget.place(x=10,y=90)
            #Imagen Transpuesta
            imagen.crear_imagen_transpuesta(self.id)
            imagen_transpuesta=PhotoImage(file="imagenTranspuesta.png")
            self.widgetT=Label(self.frame,image=imagen_transpuesta)
            self.widgetT.place(x=420,y=90)
            self.raiz.mainloop()
            print("Transpuesta")
        elif numero==4:
            
            imagen.crear_imagen_original(self.id)
            CargarArchivo.lista.limpiarArea(self.id,self.pos_x,self.pos_y,self.f,self.co)
            imagen_original=PhotoImage(file="imagen.png")
            self.widget=Label(self.frame,image=imagen_original)
            self.widget.place(x=10,y=90)
            #Imagen Limpiar zona
            imagen.crear_imagen_LimpiarZona(self.id)
            imagen_Limpiar=PhotoImage(file="imagenLimpiarZona.png")
            self.widgetLimpiar=Label(self.frame,image=imagen_Limpiar)
            self.widgetLimpiar.place(x=420,y=90)
            self.raiz.mainloop()
            print("Limpiar zona")

        elif numero==5:

            imagen.crear_imagen_original(self.id)
            CargarArchivo.lista.agregar_linea_horizontal(self.id,self.pos_x,self.pos_y,self.co+1)
            imagen_original=PhotoImage(file="imagen.png")
            self.widget=Label(self.frame,image=imagen_original)
            self.widget.place(x=10,y=90)
            #Imagen Agregar fila horizontal
            imagen.crear_imagen_agregaH(self.id)
            imagen_agregarH=PhotoImage(file="imagenAgregarH.png")
            self.widgetAg=Label(self.frame,image=imagen_agregarH)
            self.widgetAg.place(x=420,y=120)
            self.raiz.mainloop()
            print("Agregar linea horizontal")   

        elif numero==6:
            imagen.crear_imagen_original(self.id)
            CargarArchivo.lista.agregar_linea_vertical(self.id,self.pos_x,self.f+1,self.co)
            imagen_original=PhotoImage(file="imagen.png")
            self.widget=Label(self.frame,image=imagen_original)
            self.widget.place(x=10,y=90)
            #Imagen Agregar fila horizontal
            imagen.crear_imagen_agregaV(self.id)
            imagen_agregarH=PhotoImage(file="imagenAgregarV.png")
            self.widgetAv=Label(self.frame,image=imagen_agregarH)
            self.widgetAv.place(x=420,y=90)
            self.raiz.mainloop()


            print("Agregar linea vertical")
        elif numero==7:

            imagen.crear_imagen_original(self.id)
            
            CargarArchivo.lista.agrega_un_rectangulo(self.id,self.pos_x,self.pos_y,self.f+1,self.co+1)
            imagen_original=PhotoImage(file="imagen.png")
            self.widget=Label(self.frame,image=imagen_original)
            self.widget.place(x=10,y=90)
            #Imagen Agregar fila horizontal
            imagen.crear_imagen_agregaRec(self.id)
            imagen_agregarH=PhotoImage(file="imagenAgregarRec.png")
            self.widgetRec=Label(self.frame,image=imagen_agregarH)
            self.widgetRec.place(x=420,y=120)
            self.raiz.mainloop()
            print("Agregar rectangulo")   
        elif numero==2:
            print("Agregar triangulo rectangulo") 
    #Metodo para limpiar
    def limpiar(self):
        
           
        print("limpiados")  
    def ayuda(self):
        raiz2=Tk()
        frame2=Frame()  
        frame2.place(x=0,y=0)
        frame2.config(width="100",height="90")
        frame2.config(bg="black")     
        
        raiz2.mainloop()      

gui=GUI()
gui.interfaz()        
