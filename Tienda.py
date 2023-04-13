import tkinter as tk
from tkinter import Label, ttk
from tkinter import messagebox
from logicaProyecto import *

class InterfazTiendita:
    
    # Creamos un objeto de la clase controladorBD
    controlador = productosBD()
    
    def consultoria(self):
        return self.controlador.consultando()
    
    def __init__(self):
        # Crear una ventana principal
        self.root = tk.Tk()
        self.root.title('Interfaz de compra de productos')
        self.root.geometry("500x400")
        
        columns = ('Id', 'nom', 'desc', 'prec', 'cant')
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')
        
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

        subCons = Label(self.root,text="Productos Disponibles:",fg="blue",font=("Modern",15)).pack()
        self.tree.pack()
        
        # Obtención de los datos de la función consultoria() y agregación a Treeview
        datos=self.consultoria()
        for i, row in enumerate(datos): # type: ignore
            # Insertar datos de cada fila en el Treeview
            self.tree.insert('', 'end', text=str(i+1), values=row)
        
        # Crear una variable de control para el total
        self.total = tk.DoubleVar()
        self.total.set(0.0)

        # Crear una etiqueta para el total
        self.total_label = tk.Label(self.root,font=("Helvetica", 15), text=f'Total: {self.total.get()}')
        self.total_label.pack()
        

        # Crear una función para sumar los productos seleccionados
        def sumar_productos():
            # Obtener el nombre del producto seleccionado
            producto_seleccionado = self.productos_listbox.get(tk.ACTIVE)

            # Dividir el nombre del producto y el precio en una lista
            producto_seleccionado_lista = producto_seleccionado.split(' - ')

            # Obtener el precio del producto seleccionado
            precio = self.productos[producto_seleccionado_lista[0]]

            # Sumar el precio al total
            self.total.set(self.total.get() + precio)

            # Actualizar la etiqueta del total
            self.total_label.config(text=f'Total: {self.total.get()}')

        # Crear una función para restar los productos seleccionados
        def restar_productos():
            # Obtener el nombre del producto seleccionado
            producto_seleccionado = self.productos_listbox.get(tk.ACTIVE)

            # Dividir el nombre del producto y el precio en una lista
            producto_seleccionado_lista = producto_seleccionado.split(' - ')

            # Obtener el nombre del producto
            producto = producto_seleccionado_lista[0]

            if producto in self.productos:
                # Obtener el precio del producto seleccionado
                precio = self.productos[producto]

                # Verificar que el total no sea menor que cero después de restar el precio del producto
                if self.total.get() - precio < 0:
                    messagebox.showerror('Error', 'No tiene suficientes fondos para realizar esta compra.')
                else:
                    # Restar el precio al total
                    self.total.set(self.total.get() - precio)

                    # Actualizar la etiqueta del total
                    self.total_label.config(text=f'Total: {self.total.get()}')

        # Crear una lista de productos con su precio
        self.productos_listbox = tk.Listbox(self.root)

        for producto, precio in self.productos.items():
            self.productos_listbox.insert(tk.END, f'{producto} - ${precio}')

        self.productos_listbox.pack()

        # Crear un botón para sumar productos
        self.sumar_button = tk.Button(self.root, text='Sumar',font=("Helvetica",15), command=sumar_productos)
        self.sumar_button.pack()

        # Crear un botón para restar productos
        self.restar_button = tk.Button(self.root, text='Restar',font=("Helvetica",15), command=restar_productos)
        self.restar_button.pack()
        
        # Crear una entrada para la dirección
        direccion_label = tk.Label(self.root,font=("Helvetica", 15), text='Dirección:')
        direccion_label.pack()

        self.direccion_entry = tk.Entry(self.root)
        self.direccion_entry.pack()

        # Crear un botón para finalizar la compra
        self.comprar_button = tk.Button(self.root, text='Comprar',font=("Helvetica",15), command=self.finalizar_compra)
        self.comprar_button.pack()       

    def finalizar_compra(self):
        # Obtener la dirección del cliente
        direccion = self.direccion_entry.get()

        # Verificar que se haya ingresado una dirección
        if direccion == '':
            messagebox.showerror('Error', 'Debe ingresar una dirección para finalizar la compra.')
        else:
            # Mostrar un mensaje con el total y la dirección
            messagebox.showinfo('Compra realizada', f'Se ha realizado una compra por un total de ${self.total.get()} a la dirección {direccion}.')
