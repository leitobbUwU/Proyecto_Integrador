import datetime
import tkinter as tk
from tkinter import Label, ttk
from tkinter import messagebox
from tkinter import simpledialog
from logicaProyecto import productosBD


class InterfazTiendita:
    
    controlador = productosBD()
    
    def consultoria(self):
        return self.controlador.consultando()

    def __init__(self):
        # Crear una ventana principal
        self.root = tk.Tk()
        self.root.title('Interfaz de compra de productos')
        self.root.geometry("10920x1080")

        columns = ('Id', 'nom', 'desc', 'prec', 'cant')
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')

        self.tree.heading('Id', text='Id', )
        self.tree.heading('nom', text='Nombre')
        self.tree.heading('desc', text='Descripcion')
        self.tree.heading('prec', text='Precio')
        self.tree.heading('cant', text='Cantidad')

        subCons = Label(self.root, text="Productos Disponibles:", fg="blue", font=("Modern", 15)).pack()
        self.tree.pack()

        # Obtención de los datos de la función consultoria() y agregación a Treeview
        datos = self.consultoria()
        for i, row in enumerate(datos):  # type: ignore
            # Insertar datos de cada fila en el Treeview
            self.tree.insert('', 'end', text=str(i + 1), values=row)
        
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
          # Crear un Treeview para el carrito
        carrito_columns = ('Id', 'nom', 'desc', 'prec', 'cant', 'imp')
        self.carrito_tree = ttk.Treeview(self.root, columns=carrito_columns, show='headings')

        self.carrito_tree.heading('Id', text='Id', )
        self.carrito_tree.heading('nom', text='Nombre')
        self.carrito_tree.heading('desc', text='Descripcion')
        self.carrito_tree.heading('prec', text='Precio')
        self.carrito_tree.heading('cant', text='Cantidad')
        self.carrito_tree.heading('imp', text='Importe')

        subCons = Label(self.root,text="Carrito:",fg="blue",font=("Modern",15)).pack()
        self.carrito_tree.pack()

        # Crear una etiqueta para el total del carrito
        self.total_carrito_label = tk.Label(self.root,font=("Helvetica", 15), text='Total del carrito: $0.00')
        self.total_carrito_label.pack()

        # Crear un botón para agregar productos al carrito
        agregar_carrito_button = tk.Button(self.root, text='Agregar al carrito',font=("Helvetica",15), command= self.agregar_carrito)
        agregar_carrito_button.pack()

        # Crear un botón para eliminar productos del carrito
        self.eliminar_carrito_button = tk.Button(self.root, text='Eliminar del carrito', font=("Helvetica", 15), command=self.quitar_carrito)
        self.eliminar_carrito_button.pack()
        
        # Crear un botón para finalizar la compra
        self.comprar_button = tk.Button(self.root, text='Comprar', font=("Helvetica", 15), command=self.comprar)
        self.comprar_button.pack()
        
    def agregar_carrito(self):
        # Obtener el item seleccionado del Treeview
        selected = self.tree.focus()
        values = self.tree.item(selected, 'values')
        if not values:
            messagebox.showwarning('Error', 'Debe seleccionar un producto para agregar al carrito.')
            return
        
        # Obtener la cantidad deseada del producto
        cantidad = simpledialog.askinteger('Cantidad', f'¿Cuántos {values[1]} desea agregar al carrito?', minvalue=1, maxvalue=int(values[4]))
        if not cantidad:
            return
        
        # Calcular el importe
        importe = float(values[3]) * cantidad
        
        # Actualizar la cantidad del producto en el inventario
        nuevo_stock = int(values[4]) - cantidad
        self.controlador.actualizar(int(values[0]), cantidad=nuevo_stock)
        
        # Agregar el producto al carrito
        self.carrito_tree.insert('', 'end', values=(*values, cantidad, importe))
        
        # Actualizar el total del carrito
        total = sum(float(self.carrito_tree.item(i, 'values')[-1]) for i in self.carrito_tree.get_children())
        self.total_carrito_label.config(text=f'Total del carrito: ${total:.2f}')

    def quitar_carrito(self):
        # Obtener el item seleccionado del Treeview del carrito
        selected = self.carrito_tree.focus()
        values = self.carrito_tree.item(selected, 'values')
        if not values:
            messagebox.showwarning('Error', 'Debe seleccionar un producto para quitar del carrito.')
            return
        
        # Obtener la cantidad deseada del producto
        cantidad = simpledialog.askinteger('Cantidad', f'¿Cuántos {values[1]} desea quitar del carrito?', minvalue=1, maxvalue=int(values[4]))
        if not cantidad:
            return
        
        # Actualizar la cantidad del producto en el inventario
        nuevo_stock = int(values[4]) + cantidad
        self.controlador.actualizar(int(values[0]), cantidad=nuevo_stock)
        
        # Actualizar la cantidad y el importe del producto en el carrito
        nueva_cantidad = int(values[4]) - cantidad
        nuevo_importe = float(values[3]) * nueva_cantidad
        self.carrito_tree.item(selected, values=(*values[:-2], nueva_cantidad, nuevo_importe))
        
        # Actualizar el total del carrito
        total = sum(float(self.carrito_tree.item(i, 'values')[-1]) for i in self.carrito_tree.get_children())
        self.total_carrito_label.config(text=f'Total del carrito: ${total:.2f}')
    
    def comprar(self):
        # Obtener la selección actual en el Treeview del carrito
        seleccion = self.carrito_tree.selection()
        
        # Verificar que haya al menos un elemento seleccionado en el carrito
        if not seleccion:
            messagebox.showerror('Error', 'Debe seleccionar al menos un producto para realizar la compra.')
            return
        
        # Pedir confirmación al usuario para realizar la compra
        confirmacion = messagebox.askyesno('Confirmar compra', '¿Está seguro de que desea realizar la compra?')
        if not confirmacion:
            return
        
        # Iterar sobre los elementos seleccionados del carrito
        for id_carrito in seleccion:
            # Obtener los datos del producto en el carrito
            producto_carrito = self.carrito_tree.item(id_carrito)['values']
            id_producto = producto_carrito[0]
            cantidad = producto_carrito[4]
            
            # Obtener los datos del producto en la base de datos
            producto_bd = self.controlador.obtener_producto(id_producto)
            cantidad_bd = producto_bd[4]
            
            # Verificar que haya suficiente cantidad en la base de datos
            if cantidad > cantidad_bd:
                messagebox.showerror('Error', f'No hay suficiente cantidad de "{producto_bd[1]}" en el inventario.')
                return
            
            # Actualizar la cantidad en la base de datos y el Treeview correspondiente
            nueva_cantidad_bd = cantidad_bd - cantidad
            self.controlador.actualizar_producto(id_producto, {'cantidad': nueva_cantidad_bd})
            self.tree.set(id_producto, 'cant', nueva_cantidad_bd)
            
            # Eliminar el producto del carrito
            self.carrito_tree.delete(id_carrito)
        
        # Actualizar el total del carrito y mostrar un mensaje de confirmación de compra
        self.total_carrito_label.config(text='Total del carrito: $0.00')
        messagebox.showinfo('Compra realizada', 'Compra realizada con éxito.')
