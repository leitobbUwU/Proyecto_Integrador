import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from logicaProyecto import *

class InterfazTiendita:
    def __init__(self):
        # Crear una lista de productos con su precio
        self.productos = {
            "Coca-cola 600ML ": 16,
            "Sabritas ": 20,
            "Garrafon de Agua ": 50,
            "Pan Bimbo ": 45,
            "Tortillas ": 22,
            "Fabuloso ": 30,
            "Cloro ": 20,
            "Cepillo de dientes ": 17,
            "Leche ": 26,
            "Mazapan ": 7
        }
        # Crear una ventana principal
        self.root = tk.Tk()
        self.root.title('Interfaz de compra de productos')
        self.root.geometry("500x400")
        
        ventana2=ttk.Notebook(self.root)
        ventana2.pack(fill='both', expand=True)
        
        pestana1=ttk.Frame(ventana2)
        pestana2=ttk.Frame(ventana2)
        pestana3=ttk.Frame(ventana2)
        pestana4=ttk.Frame(ventana2)

        # Crear una variable de control para el total
        self.total = tk.DoubleVar()
        self.total.set(0.0)

        # Crear una etiqueta para el total
        self.total_label = tk.Label(pestana1,font=("Helvetica", 15), text=f'Total: {self.total.get()}')
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
        self.productos_listbox = tk.Listbox(pestana1)

        for producto, precio in self.productos.items():
            self.productos_listbox.insert(tk.END, f'{producto} - ${precio}')

        self.productos_listbox.pack()

        # Crear un botón para sumar productos
        self.sumar_button = tk.Button(pestana1, text='Sumar',font=("Helvetica",15), command=sumar_productos)
        self.sumar_button.pack()

        # Crear un botón para restar productos
        self.restar_button = tk.Button(pestana1, text='Restar',font=("Helvetica",15), command=restar_productos)
        self.restar_button.pack()
        
        # Crear una entrada para la dirección
        direccion_label = tk.Label(pestana1,font=("Helvetica", 15), text='Dirección:')
        direccion_label.pack()

        self.direccion_entry = tk.Entry(pestana1)
        self.direccion_entry.pack()

        # Crear un botón para finalizar la compra
        self.comprar_button = tk.Button(pestana1, text='Comprar',font=("Helvetica",15), command=self.finalizar_compra)
        self.comprar_button.pack()
        
        ventana2.add(pestana1,text='Compra Productos')
        ventana2.add(pestana2,text='')
        ventana2.add(pestana3,text=' ')
        ventana2.add(pestana4,text=' ')        

    def finalizar_compra(self):
        # Obtener la dirección del cliente
        direccion = self.direccion_entry.get()

        # Verificar que se haya ingresado una dirección
        if direccion == '':
            messagebox.showerror('Error', 'Debe ingresar una dirección para finalizar la compra.')
        else:
            # Mostrar un mensaje con el total y la dirección
            messagebox.showinfo('Compra realizada', f'Se ha realizado una compra por un total de ${self.total.get()} a la dirección {direccion}.')