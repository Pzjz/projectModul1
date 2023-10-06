from tkinter import*
from tkinter import ttk
from conector import *

class Ventana(Frame):

    def __init__(self,master=None):
        super().__init__(master,width=1200,height=500,bg="#C7D1F4")
        self.master = master
        self.pack()
        self.create_widgets()

    def fNuevo(self):
        pass

    def fModificar(self):
        pass

    def fEliminar(self):
        pass

    def fGuardar(self):
        pass

    def fCancelar(self):
        pass

    def create_widgets(self):
        contenedorUno = Frame(self,bg="#C7D1F4",height=50,width=200)
        contenedorUno.place(x=0,y=0,width=93,height=259)

        self.botonAgregar = Button(contenedorUno,text="Agregar",command=self.fNuevo,bg="Blue",fg="#ACBEFA")
        self.botonAgregar.place(x=5,y=50,width=80,height=30)
        self.botonModificar = Button(contenedorUno,text="Modificar",command=self.fModificar,bg="Blue",fg="#ACBEFA")
        self.botonModificar.place(x=5,y=90,width=80,height=30)
        self.botonEliminar = Button(contenedorUno,text="Eliminar",command=self.fEliminar,bg="Blue",fg="#ACBEFA")
        self.botonEliminar.place(x=5,y=130,width=80,height=30)

        contenedorDos = Frame(self,bg="#C7D1F4")
        contenedorDos.place(x=95,y=0,width=150,height=490)

        tituloUno = Label(contenedorDos,text="Nombre")
        tituloUno.place(x=3,y=15)
        self.txtUno = Entry(contenedorDos)
        self.txtUno.place(x=3,y=40,width=120,height=20)
        
        tituloDos = Label(contenedorDos,text="Apellidos")
        tituloDos.place(x=3,y=65)
        self.txtDos = Entry(contenedorDos)
        self.txtDos.place(x=3,y=90,width=120,height=20)

        tituloTres = Label(contenedorDos,text="Cedula")
        tituloTres.place(x=3,y=115)
        self.txtTres = Entry(contenedorDos)
        self.txtTres.place(x=3,y=140,width=120,height=20)

        tituloCuatro = Label(contenedorDos,text="Residencia")
        tituloCuatro.place(x=3,y=165)
        self.txtCuatro = Entry(contenedorDos)
        self.txtCuatro.place(x=3,y=190,width=120,height=20)

        tituloCinco = Label(contenedorDos,text="Numero telefono")
        tituloCinco.place(x=3,y=215)
        self.txtCinco = Entry(contenedorDos)
        self.txtCinco.place(x=3,y=240,width=120,height=20)

        tituloSeis = Label(contenedorDos,text="Enfermedad")
        tituloSeis.place(x=3,y=265)
        self.txtSeis = Entry(contenedorDos)
        self.txtSeis.place(x=3,y=290,width=140,height=20)

        tituloSiete = Label(contenedorDos,text="Fecha consulta")
        tituloSiete.place(x=3,y=315)
        self.txtSiete = Entry(contenedorDos)
        self.txtSiete.place(x=3,y=340,width=120,height=20)

        tituloOcho = Label(contenedorDos,text="Registro medico")
        tituloOcho.place(x=3,y=365)
        self.txtOcho = Entry(contenedorDos)
        self.txtOcho.place(x=3,y=390,width=120,height=20)

        self.botonGuardar = Button(contenedorDos,text="Guardar",command=self.fGuardar,bg="#ACBEFA",fg="Black")
        self.botonGuardar.place(x=10,y=440,width=60,height=30)

        self.botonCancelar = Button(contenedorDos,text="Cancelar",command=self.fCancelar,bg="#ACBEFA",fg="Black")
        self.botonCancelar.place(x=80,y=440,width=60,height=30)

        self.grid = ttk.Treeview(self,columns=("col1","col2","col3","col4","col5","col6","col7"))

        self.grid.column("#0",width=50)
        self.grid.column("col1",width=50,anchor="center")
        self.grid.column("col2",width=50,anchor="center")
        self.grid.column("col3",width=90,anchor="center")
        self.grid.column("col4",width=70,anchor="center")
        self.grid.column("col5",width=90,anchor="center")
        self.grid.column("col6",width=50,anchor="center")
        self.grid.column("col7",width=90,anchor="center")

        self.grid.heading("#0",text="nombre",anchor="center")
        self.grid.heading("col1",text="Apellidos",anchor="center")
        self.grid.heading("col2",text="Cedula",anchor="center")
        self.grid.heading("col3",text="Residencia",anchor="center")
        self.grid.heading("col4",text="Numero telefono",anchor="center")
        self.grid.heading("col5",text="Enfermedad",anchor="center")
        self.grid.heading("col6",text="Fecha consulta",anchor="center")
        self.grid.heading("col7",text="Registro medico",anchor="center")

        self.grid.place(x=247,y=0,width=900,height=490)