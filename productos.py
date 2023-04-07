from tkinter import *
from tkinter import ttk
from logicaProyecto import *

import tkinter as tk
class productos:
    def __init__(self):
        # Creamos la ventana principal
        self.ventana = Tk()
        self.ventana.title("ABM de productos")
        self.ventana.geometry("800x600")

        # Creamos las pestañas del panel
        panel = ttk.Notebook(self.ventana)
        panel.pack(fill='both', expand=True)
        pestana1 = ttk.Frame(panel)
        pestana2 = ttk.Frame(panel)
        pestana3 = ttk.Frame(panel)
        pestana4= ttk.Frame(panel)
        pestaña5= ttk.Frame(panel)
        pestaña6= ttk.Frame(panel)

        # Pestaña 1: alta de productos
        self.varNom = tk.StringVar()
        titulo1 = Label(pestana1, text="Nombre:", font=("Modern",18)).pack(fill=tk.X, padx=20, pady=5)
        self.nombre = Entry(pestana1, textvariable=self.varNom, font=("Helvetica", 18))
        self.nombre.pack( padx=20, pady=10)

        self.varDes= tk.StringVar()
        titulo2 = Label(pestana1, text="descripcion:", font=("Modern",18)).pack(fill=tk.X, padx=20, pady=5)
        self.descripcion = Entry(pestana1, textvariable=self.varDes, font=("Helvetica", 18))
        self.descripcion.pack( padx=20, pady=10)

        self.varPrecio = tk.StringVar()
        titulo3 = Label(pestana1, text="Precio:", font=("Modern", 18)).pack(fill=tk.X, padx=20, pady=5)
        self.precio = Entry(pestana1,textvariable=self.varPrecio, font=("Helvetica", 18))
        self.precio.pack( padx=20, pady=10, )

        self.varCantidad = tk.StringVar()
        titulo3 = Label(pestana1, text="Cantidad:", font=("Modern", 18)).pack(fill=tk.X, padx=20, pady=5)
        self.cantidad = Entry(pestana1,textvariable=self.varCantidad, font=("Helvetica", 18))
        self.cantidad.pack( padx=20, pady=10, )

        self.botonGuardar = tk.Button(pestana1, text="Guardar producto", fg="Black", bg="#00ccff", font=("Modern", 15), command=self.ejecutaInsert)
        self.botonGuardar.pack()

        # Pestaña 2: búsqueda de productos
        titulo2 = Label(pestana2, text="Buscar producto", fg="green",font=("Modern", 18)).pack()

        self.varBus = tk.StringVar()
        lblid = Label(pestana2,text="identificador producto: ").pack()
        self.txtid = Entry(pestana2,textvariable=self.varBus)
        self.txtid.pack()
        self.btnBus = Button(pestana2,text="Buscar",command=self.ejecutaSelectP).pack()

        subBus = Label(pestana2,text="encontrado:",fg="blue",font=("Modern",15)).pack()
        self.textEnc = tk.Text(pestana2,height=5,width=52)
        self.textEnc.pack()

        titulo3 = Label(pestana3, text="Consultar productos", fg="green",font=("Modern", 18)).pack()

        self.varCons = tk.StringVar()
        self.botonCons = Button(pestana3,text="Buscar",command=self.ejecutarConsultarP).pack()

        self.treeview = ttk.Treeview(pestana3, columns=(1, 2, 3, 4), show="headings", height="5")
        self.treeview.heading(1, text="ID")
        self.treeview.column(1, width=50)
        self.treeview.heading(2, text="Nombre")
        self.treeview.column(2, width=150)
        self.treeview.heading(3, text="Descripcion")
        self.treeview.column(3, width=200)
        self.treeview.heading(4, text="Precio")
        self.treeview.column(4, width=100)

        subCons = Label(pestana3,text="productos encontrados:",fg="blue",font=("Modern",15)).pack()
        self.treeview.pack()

        #pestaña4: actualizar productos
        titulo4 = Label(pestana4, text="Actualizar Producto", font=("Modern",18)).pack(fill=tk. X, padx=20, pady=10)

        #Campo para ingresar el ID del producto a actualizar
        self.varID = tk. StringVar()
        lblID = Label(pestana4, text="ID del producto:", font=("Modern", 15)).pack(padx=20, pady=5)
        txtID = Entry(pestana4, textvariable=self.varID, font=("Helvetica", 15))
        txtID.pack(padx=20, pady=5)

        #Campos para ingresar los nuevos datos del producto
        self.varNomAct = tk.StringVar()
        lblNomAct = Label(pestana4, text="Nuevo Nombre", font=("Modern", 15)).pack(padx=20, pady=5)
        txtNomAct = Entry(pestana4, textvariable=self.varNomAct, font=("Helvetica", 15))
        txtNomAct.pack(padx=20, pady=5)

        self.varDesAct = tk. StringVar()
        lblDesAct = Label(pestana4, text="Nueva Descripcion", font=("Modern", 15)).pack(padx=20, pady=5)
        txtDesAct = Entry(pestana4, textvariable=self.varDesAct, font=("Helvetica", 15))
        txtDesAct.pack(padx=20, pady=5)

        self.varPreAct = tk. StringVar()
        lblPreAct = Label(pestana4, text="Nuevo precio:", font=("Modern", 15)).pack(padx=20, pady=5)
        txtPreAct = Entry(pestana4, textvariable=self.varPreAct, font=("Helvetica", 15))
        txtPreAct.pack(padx=20, pady=5)

        self.varCanAct = tk. StringVar()
        lblPreAct = Label(pestana4, text="Nueva cantidad:", font=("Modern", 15)).pack(padx=20, pady=5)
        txtCanAct = Entry(pestana4, textvariable=self.varCanAct, font=("Helvetica", 15))
        txtCanAct.pack(padx=20, pady=5)

        #Botón para actualizar el producto
        self.botonAct = tk. Button(pestana4, text="Actualizar producto", fg="Black", bg="#00ccff", font=("Modern", 15), command=self.ejecutarActualizarP )
        self.botonAct.pack()

        #pestaña5: eliminar producto
        titulo5 = Label(pestaña5, text="Eliminar Producto", font=("Modern",18)).pack(fill=tk. X, padx=20, pady=10)

        #Campo para ingresar el ID del producto a eliminar
        self.varIDs = tk. StringVar()
        lblIDs = Label(pestaña5, text="ID del producto:", font=("Modern", 15)).pack(padx=20, pady=5)
        txtIDs = Entry(pestaña5, textvariable=self.varIDs, font=("Helvetica", 15))
        txtIDs.pack(padx=20, pady=5)

        #Botón para eliminar el producto
        botonElm = tk. Button(pestaña5, text="Eliminar producto", fg="Black", bg="#00ccff", font=("Modern", 15), command=self.ejecutarEliminarP)
        botonElm.pack()

        panel.add(pestana1, text='Formulario productos')
        panel.add(pestana2, text='Buscar productos')
        panel.add(pestana3, text='Consultar productos')
        panel.add(pestana4, text='Actualizar productos')
        panel.add(pestaña5, text='Eliminar productos')
        panel.add(pestaña6, text='Registrar usuarios')
        
    #Creamos la cuarta pestaña donde se registraran usuarios y empleados
        titulo2 = tk.Label(pestaña6, text="Usuario:", font=("Helvetica",20)).pack(padx=20,pady=5)
        self.usuarioReg = tk.Entry(pestaña6, font=("Helvetica", 20))
        self.usuarioReg.pack(padx=20,pady=10)
        
        titulo2 = tk.Label(pestaña6, text="Cargo:", font=("Helvetica",20)).pack(padx=20,pady=5)
        self.correoReg = tk.Entry(pestaña6, font=("Helvetica", 20))
        self.correoReg.pack(padx=20,pady=10)

        titulo2 = tk.Label(pestaña6, text="Contraseña:", font=("Helvetica", 20)).pack(padx=20, pady=5)
        self.contraseñaReg = tk.Entry(pestaña6, show="*", font=("Helvetica", 20))
        self.contraseñaReg.pack(padx=20, pady=10, )

        self.Generar= tk.Button(pestaña6, text="Ingresar", fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.ejecutaInsert)
        self.Generar.pack()
        
    controlado= Resgistro()

    def ejecutaInsert(self):
        self.controlado.guardarUsuarios(self.usuarioReg.get(), self.correoReg.get(), self.contraseñaReg.get())
    
    # Creamos un objeto de la clase controladorBD
    controlador = productosBD()
    
     # Función para dar de alta un nuevo producto
    def ejecutaInsert(self):
        self.controlador.guardarProducto(self.varNom.get(), self.varDes.get(), self.varPrecio.get(), self.varCantidad.get())

    # Función para buscar un producto por su ID
    def ejecutaSelectP(self):
        producto = self.controlador.consultarProducto(self.varBus.get())
        if producto:
            cadena = str(producto[0][0]) + " " + producto[0][1] + " " + str(producto[0][2])
            self.textEnc.delete(1.0, END)
            self.textEnc.insert(END, cadena)
        else:
            messagebox.showinfo("Producto no encontrado", "El producto no existe en la BD")

    def ejecutarActualizarP(self):
        self.controlador.actualizarProducto(self.varID.get(),self.varNomAct.get(), self.varDesAct.get(), self.varPreAct.get(), self.varCanAct.get())

    # Función para dar de baja un producto por su ID
    def ejecutarEliminarP(self):
        self.controlador.eliminarProducto(self.varIDs.get())

    # Función para consultar todos los productos de la base de datos
    def ejecutarConsultarP(self):
        productos = self.controlador.importarProductos()
        self.treeview.delete(*self.treeview.get_children())
        if productos:
            for producto in productos:
                self.treeview.insert("", "end", values=(producto[0], producto[1], producto[2], producto[3]))
        else:
            messagebox.showinfo("No hay productos", "No hay productos en la BD")
