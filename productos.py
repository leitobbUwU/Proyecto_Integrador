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

        self.botonGuardar = tk.Button(pestana1, text="Guardar producto", fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.GuardarProducto)
        self.botonGuardar.pack()

        # Pestaña 2: búsqueda de productos
        titulo3 = Label(pestana2, text="Consultar productos", fg="green",font=("Modern", 18)).pack()

        columns = ('Id', 'nom', 'desc', 'prec', 'cant')
        self.tree = ttk.Treeview(pestana2, columns=columns, show='headings')
        
        self.tree.heading('Id', text='Id', )
        self.tree.column('Id', width=50)
        self.tree.heading('nom', text='Nombre')
        self.tree.column('nom', width=100)
        self.tree.heading('desc', text='Descripcion')
        self.tree.column('desc', width=100)
        self.tree.heading('prec', text='Precio')
        self.tree.column('prec', width=50)
        self.tree.heading('cant', text='Cantidad')
        self.tree.column('cant', width=50)

        subCons = Label(pestana2,text="productos encontrados:",fg="blue",font=("Modern",15)).pack()
        self.tree.pack()
        
        # Obtención de los datos de la función consultoria() y agregación a Treeview
        datos=self.consultoria()
        for i, row in enumerate(datos): # type: ignore
            # Insertar datos de cada fila en el Treeview
            self.tree.insert('', 'end', text=str(i+1), values=row)

        #Toma de datos para consultar si estan en la BD
        self.varBus=tk.StringVar()
        iblid = Label(pestana2, text="Identificar producto especifico: ", font=("Modern",18)).pack(fill=tk.X, padx=20,pady=5)
        self.txtid = Entry(pestana2, textvariable=self.varBus, font=("Helvetica", 18))
        self.txtid.pack( padx=20,pady=10)

        botonAct= tk.Button(pestana2, text="Actualizar Tabla", fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.actualizar_tabla)
        botonAct.pack()
        #Boton de consulta especifica para un id
        botonBus= tk.Button(pestana2, text="Buscar Producto", fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.ejecutaSelectU)
        botonBus.pack()
        #Boton para borrar el id dentro del entry
        self.botonBorrar= tk.Button(pestana2, text="Borrar Producto", fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.eliminar)
        self.botonBorrar.pack()

        #pestaña3: actualizar productos
        titulo4 = Label(pestana3, text="Actualizar Producto", font=("Modern",18)).pack(fill=tk. X, padx=20, pady=10)

        #Campo para ingresar el ID del producto a actualizar
        self.varID = tk. StringVar()
        lblID = Label(pestana3, text="ID del producto:", font=("Modern", 15)).pack(padx=20, pady=5)
        txtID = Entry(pestana3, textvariable=self.varID, font=("Helvetica", 15))
        txtID.pack(padx=20, pady=5)

        #Campos para ingresar los nuevos datos del producto
        self.varNomAct = tk.StringVar()
        lblNomAct = Label(pestana3, text="Nuevo Nombre", font=("Modern", 15)).pack(padx=20, pady=5)
        txtNomAct = Entry(pestana3, textvariable=self.varNomAct, font=("Helvetica", 15))
        txtNomAct.pack(padx=20, pady=5)

        self.varDesAct = tk. StringVar()
        lblDesAct = Label(pestana3, text="Nueva Descripcion", font=("Modern", 15)).pack(padx=20, pady=5)
        txtDesAct = Entry(pestana3, textvariable=self.varDesAct, font=("Helvetica", 15))
        txtDesAct.pack(padx=20, pady=5)

        self.varPreAct = tk. StringVar()
        lblPreAct = Label(pestana3, text="Nuevo precio:", font=("Modern", 15)).pack(padx=20, pady=5)
        txtPreAct = Entry(pestana3, textvariable=self.varPreAct, font=("Helvetica", 15))
        txtPreAct.pack(padx=20, pady=5)

        self.varCanAct = tk. StringVar()
        lblPreAct = Label(pestana3, text="Nueva cantidad:", font=("Modern", 15)).pack(padx=20, pady=5)
        txtCanAct = Entry(pestana3, textvariable=self.varCanAct, font=("Helvetica", 15))
        txtCanAct.pack(padx=20, pady=5)

        #Botón para actualizar el producto
        self.botonAct = tk. Button(pestana3, text="Actualizar producto", 
                                   fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.ejecutarActualizarP )
        self.botonAct.pack()

        panel.add(pestana1, text='Formulario productos')
        panel.add(pestana2, text='Buscar productos y eliminarlos')
        panel.add(pestana3, text='Actualizar Productos')
        panel.add(pestana4, text='Registrar Empleados')
        
        #Pestaña 4 donde se registraran Clientes y Empleados
        titulo2 = tk.Label(pestana4, text="Usuario:", font=("Helvetica",20)).pack(padx=20,pady=5)
        self.usuarioReg = tk.Entry(pestana4, font=("Helvetica", 20))
        self.usuarioReg.pack(padx=20,pady=10)
        
        titulo2 = tk.Label(pestana4, text="Cargo:", font=("Helvetica",20)).pack(padx=20,pady=5)
        self.opciones = [("Cliente", "Cliente"), ("Empleado", "Empleado")]
        self.opcionVar = StringVar()
        for opcion, valor in self.opciones:
            ttk.Radiobutton(pestana4, text=opcion, variable=self.opcionVar, value=valor).pack()
        
        titulo2 = tk.Label(pestana4, text="Contraseña:", font=("Helvetica", 20)).pack(padx=20, pady=5)
        self.contraseñaReg = tk.Entry(pestana4, show="*", font=("Helvetica", 20))
        self.contraseñaReg.pack(padx=20, pady=10, )

        self.Generar= tk.Button(pestana4, text="Registrar", fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.ejecutaInsert)
        self.Generar.pack()    
    
    controlado= Resgistro()
    
    #Eliminar Usuarios
    def eliminar(self):
        self.controlador.eliminarProducto(self.txtid.get())
    
    def ejecutaInsert(self):
        opcion=self.opcionVar.get()
        print("Opción seleccionada:", opcion)
        self.controlado.guardarUsuarios(self.usuarioReg.get(), opcion, self.contraseñaReg.get())

    # Creamos un objeto de la clase controladorBD
    controlador = productosBD()
    
     # Función para dar de alta un nuevo producto
    def GuardarProducto(self):
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

    #Actualizar campos de un id
    def ejecutarActualizarP(self):
        self.controlador.actualizarProducto(self.varID.get(),self.varNomAct.get(), self.varDesAct.get(), self.varPreAct.get(), self.varCanAct.get())

    # Función para dar de baja un producto por su ID
    def ejecutarEliminarP(self):
        self.controlador.eliminarProducto(self.txtid.get())
        self.actualizar_tabla()

    #2. Consultar registro de Productos por nombre
    def ejecutaSelectU(self):
        #Limpiar la tabla
        self.tree.delete(*self.tree.get_children())
        usuario=self.controlador.ConsultarNombre(self.varBus.get())
            
        if(usuario):
            for usu in usuario:
                self.tree.insert('', 'end', values=(usu[0], usu[1], usu[2], usu[3], usu[4]))
        else:
            messagebox.showinfo("No encontrado", "Ese usuario no existe en la BD")

    #Importamos la lista de la BD
    def consultoria(self):
        return self.controlador.consultando()

    #Actualizamos la parte grafica mandando a borrar y mostrar la nueva BD
    def actualizar(self):
        # Borrar los registros actuales en la tabla después de 100ms
        for record in self.tree.get_children():
            self.tree.delete(record)

        # Obtener los nuevos registros de la base de datos después de 200ms
        datos = self.consultoria()
        for i, row in enumerate(datos): # type: ignore
            self.tree.insert('', 'end', text=str(i+1), values=row)

    #Creamos una funcion para que la tabla se actualice al dar clic en el boton 
    def actualizar_tabla(self):
        self.actualizar()

        # t = threading.Thread(target=self.actualizar)
        # t.start()
