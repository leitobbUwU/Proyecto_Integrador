import tkinter as tk
from tkinter import Label, Entry, messagebox
from logicaProyecto import Tiendita

class InterfazTiendita:
    def __init__(self):
        self.tiendita = Tiendita()

        self.root = tk.Tk()
        self.root.title("Bienvenido a la tiendita")
        self.root.geometry("800x500")

        # Creamos un cuadro de lista para mostrar los productos
        self.listbox = tk.Listbox(self.root)
        for producto in self.tiendita.productos:
            self.listbox.insert(tk.END, producto)
        self.listbox.pack()

        # Creamos un botón para agregar productos al carrito
        agregar_button = tk.Button(self.root, text="Agregar al carrito", command=self.agregar_producto)
        agregar_button.pack()

        # Creamos un botón para eliminar productos al carrito
        eliminar_button = tk.Button(self.root, text="Eliminar producto del carrito", command=self.eliminar_producto)
        eliminar_button.pack()

        # Creamos una etiqueta para mostrar el total a pagar
        self.total_label = tk.Label(self.root, text="Total: $0")
        self.total_label.pack()

        # Creamos un botón para finalizar compra
        self.comprar_button = tk.Button(self.root, text="Comprar", command=lambda: self.comprar(self.ubicacion.get()), state=tk.DISABLED)
        self.comprar_button.pack()

        self.label = Label(self.root, text="Agregue su ubicación de favor:", fg="black")
        self.label.pack()
        self.ubicacion = Entry(self.root)
        self.ubicacion.pack()

        # Ejecutamos el bucle principal de la ventana
        self.root.mainloop()

    # Función para agregar un producto al carrito
    def agregar_producto(self):
        producto = self.listbox.get(tk.ACTIVE)
        self.tiendita.agregar_producto(producto)
        self.actualizar_total()
        self.comprar_button.config(state=tk.NORMAL)

    # Función para eliminar un producto al car
    def eliminar_producto(self):
        producto = self.listbox.get(tk.ACTIVE)
        self.tiendita.eliminar_producto(producto)
        self.actualizar_total()
        if not self.tiendita.carrito:
            self.comprar_button.config(state=tk.DISABLED)
            
    def comprar(self):
        ubicacion = self.ubicacion.get()
        if not ubicacion:
            messagebox.showerror("Error", "Debe ingresar una dirección para la entrega.")
        else:
            self.tiendita.comprar(ubicacion)
            messagebox.showinfo("Compra realizada", f"Compra realizada con éxito. Total a pagar: ${self.tiendita.total}. La entrega se realizará en la dirección: {ubicacion}.")
            self.root.quit()
        for producto in self.carrito:
            del self.productos[producto]


    # Función para actualizar el total a pagar
    def actualizar_total(self):
        self.total_label.config(text="Total: $" + str(self.tiendita.total))
        self.listbox.destroy()
        self.listbox = tk.Listbox(self.root)
        for producto in self.tiendita.productos:
            self.listbox.insert(tk.END, producto)
        self.listbox.pack()
