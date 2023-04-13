import threading
from tkinter import *
from tkinter import ttk
from logicaProyecto import *
import tkinter as tk

class usuarios:
    def __init__(self):
        # Creamos la ventana principal
        self.ventana = Tk()
        self.ventana.title("Usuarios")
        self.ventana.geometry("800x600")

        # Creamos las pestañas del panel
        panel = ttk.Notebook(self.ventana)
        panel.pack(fill='both', expand=True)
        pes1 = ttk.Frame(panel)
        pes2 = ttk.Frame(panel)
        pes3 = ttk.Frame(panel)
        pes4= ttk.Frame(panel)

        # Pestaña 2: búsqueda de productos
        titulo3 = Label(pes1, text="Consultar usuario", fg="green",font=("Modern", 18)).pack()

        columns = ('Id', 'nom', 'desc', 'prec', 'cant')
        self.tree = ttk.Treeview(pes1, columns=columns, show='headings')

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

        subCons = Label(pes1,text="Usuarios encontrados:",fg="blue",font=("Modern",15)).pack()
        self.tree.pack()

        # Obtención de los datos de la función consultoria() y agregación a Treeview
        datos=self.consultoria()
        for i, row in enumerate(datos): # type: ignore
            # Insertar datos de cada fila en el Treeview
            self.tree.insert('', 'end', text=str(i+1), values=row)

        #Toma de datos para consultar si estan en la BD
        self.varBus=tk.StringVar()
        iblid = Label(pes1, text="Identificar usuario especifico: ", font=("Modern",18)).pack(fill=tk.X, padx=20,pady=5)
        self.txtid = Entry(pes1, textvariable=self.varBus, font=("Helvetica", 18))
        self.txtid.pack( padx=20,pady=10)

        botonAct= tk.Button(pes1, text="Actualizar Tabla", fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.actualizar_tabla)
        botonAct.pack()
        #Boton de consulta especifica para un id
        botonBus= tk.Button(pes1, text="Buscar Usuario", fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.ejecutaSelectU)
        botonBus.pack()
        #Boton para borrar el id dentro del entry
        self.botonBorrar= tk.Button(pes1, text="Borrar Usuario", fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.eliminar)
        self.botonBorrar.pack()

        #pestaña3: actualizar productos
        titulo4 = Label(pes2, text="Actualizar usuario", font=("Modern",18)).pack(fill=tk. X, padx=20, pady=10)

        #Campo para ingresar el ID del producto a actualizar
        self.varID = tk. StringVar()
        lblID = Label(pes2, text="ID del usuario:", font=("Modern", 15)).pack(padx=20, pady=5)
        txtID = Entry(pes2, textvariable=self.varID, font=("Helvetica", 15))
        txtID.pack(padx=20, pady=5)

        #Campos para ingresar los nuevos datos del producto
        self.varNomAct = tk.StringVar()
        lblNomAct = Label(pes2, text="Nuevo nombre", font=("Modern", 15)).pack(padx=20, pady=5)
        txtNomAct = Entry(pes2, textvariable=self.varNomAct, font=("Helvetica", 15))
        txtNomAct.pack(padx=20, pady=5)

        self.varDesAct = tk. StringVar()
        lblDesAct = Label(pes2, text="Nueva contraseña", font=("Modern", 15)).pack(padx=20, pady=5)
        txtDesAct = Entry(pes2, textvariable=self.varDesAct,show="*", font=("Helvetica", 15))
        txtDesAct.pack(padx=20, pady=5)

        lblPreAct = Label(pes2, text="Nuevo puesto:", font=("Modern", 15)).pack(padx=20, pady=5)
        self.opciones2 = [("Cliente", "Cliente"), ("Empleado", "Empleado"), ("Gerente", "Gerente")]
        self.opcionVar2 = StringVar()
        for opcion2, valor2 in self.opciones2:
            ttk.Radiobutton(pes2, text=opcion2, variable=self.opcionVar2, value=valor2).pack()

        #Botón para actualizar el producto
        self.botonAct = tk. Button(pes2, text="Actualizar Usuario", fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.ActualizarU )
        self.botonAct.pack()

        panel.add(pes1, text='Buscar y eliminar usuarios')
        panel.add(pes2, text='Actualizar Usuraio')
        panel.add(pes3, text='Registrar Gerentes')

        #Pestaña 4 donde se registraran Clientes y Empleados
        titulo2 = tk.Label(pes3, text="Usuario:", font=("Helvetica",20)).pack(padx=20,pady=5)
        self.usuarioReg = tk.Entry(pes3, font=("Helvetica", 20))
        self.usuarioReg.pack(padx=20,pady=10)

        titulo2 = tk.Label(pes3, text="Cargo:", font=("Helvetica",20)).pack(padx=20,pady=5)
        self.opciones = [("Cliente", "Cliente"), ("Empleado", "Empleado"), ("Gerente", "Gerente")]
        self.opcionVar = StringVar()
        for opcion, valor in self.opciones:
            ttk.Radiobutton(pes3, text=opcion, variable=self.opcionVar, value=valor).pack()

        titulo2 = tk.Label(pes3, text="Contraseña:", font=("Helvetica", 20)).pack(padx=20, pady=5)
        self.contraseñaReg = tk.Entry(pes3, show="*", font=("Helvetica", 20))
        self.contraseñaReg.pack(padx=20, pady=10, )

        self.Generar= tk.Button(pes3, text="Registrar", fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.ejecutaInsert)
        self.Generar.pack()

    control1= Resgistro()

    def ejecutaInsert(self):
        opcion=self.opcionVar.get()
        print("Opción seleccionada:", opcion)
        self.control1.guardarUsuarios(self.usuarioReg.get(), opcion, self.contraseñaReg.get())

    # Creamos un objeto de la clase controladorBD
    control2 = UsuariosBD()

    #Eliminar Usuarios
    def eliminar(self):
        self.control2.eliminarUsuario(self.txtid.get())
        self.actualizar_tabla()

    # Función para buscar un producto por su ID
    def ejecutaSelectP(self):
        producto = self.control2.consultarUsuario(self.varBus.get())
        if producto:
            cadena = str(producto[0][0]) + " " + producto[0][1] + " " + str(producto[0][2])
            # self.textEnc.delete(1.0, END)
            # self.textEnc.insert(END, cadena)
        else:
            messagebox.showinfo("Usuario no encontrado", "El usuario no existe en la BD")

    #Actualizar campos de un id
    def ActualizarU(self):
        opcion2=self.opcionVar2.get()
        print("Opción seleccionada:", opcion2)
        self.control2.actualizarUsuario(self.varID.get(), self.varNomAct.get(), self.varDesAct.get(), opcion2)

    #2. Consultar registro de Productos por nombre
    def ejecutaSelectU(self):
        #Limpiar la tabla
        self.tree.delete(*self.tree.get_children())
        usuario=self.control2.ConsultarNombreUsu(self.varBus.get())

        if(usuario):
            for usu in usuario:
                self.tree.insert('', 'end', values=(usu[0], usu[1], usu[2], usu[3]))
        else:
            messagebox.showinfo("No encontrado", "Ese usuario no existe en la BD")

    #Importamos la lista de la BD
    def consultoria(self):
        return self.control2.consultando()

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
