from tkinter import*
from tkinter import filedialog as FileDialog
from CargarArchivo import CargarArchivo
import sys
cargarArchivo=CargarArchivo()
class GUI:
    
    def interfaz(self):
        raiz=Tk()
        raiz.title("Principal")
        #Frame
        frame=Frame()
        frame.pack()
        frame.config(width="810",height="550")
        frame.config(bg="black")

        #Agregar boton
        boton1=Button(frame,text="Cargar Archivo",command=self.abrirArchivo,width="20",height="3",activeforeground="blue",activebackground="black",borderwidth=10)
        boton1.place(x=0,y=10)
        #
        #Boton operaciones
        boton2=Button(frame,text="Operaciones",width="20",height="3",activeforeground="blue",activebackground="black",borderwidth=10)
        boton2.place(x=170,y=10)
        #Boton reportes
        boton3=Button(frame,text="Reportes",command=self.vertical,width="20",height="3",activeforeground="blue",activebackground="black",borderwidth=10)
        boton3.place(x=340,y=10)
        #Boton Ayuda
        boton4=Button(frame,text="Ayuda",command=self.suma,width="20",height="3",activeforeground="blue",activebackground="black",borderwidth=10)
        boton4.place(x=510,y=10)
        #Boton para salir
        salir=Button(frame,text="Salir",command=sys.exit,width="15",height="3",activeforeground="blue",activebackground="black",borderwidth=10)
        salir.place(x=680,y=10)
        raiz.mainloop()

    def abrirArchivo(self):
        fichero=FileDialog.askopenfilename(title="Abrir un fichero")
        fi=open(fichero,'r')
        cargarArchivo.procesar(fi)
        print(fi)

    def suma(self):
        print("hola") 

    #Prueba
    def vertical(self):
        li=[1,2,3,4,5,6,7,8]
        print(li)
        for i in range(int(len(li))-1,-1,-1):
            print(li[i])   
                  
gui=GUI()
gui.interfaz()        
