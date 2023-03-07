import tkinter as tk
from tkinter import ttk

class tienda:
    def __init__(self, master):
        self.master = master
        master.title("Tienda")
        self.master.geometry("800x600")

        # Etiqueta de bienvenida
        self.label = tk.Label(master, text="Bienvenido a la tienda!")
        self.label.pack(fill=tk.X, padx=20,pady=5)

        # Botones para las opciones de la tienda
        boton_productos = ttk.Combobox(master, width=17)
        boton_productos.pack()
        productos = ["Coca","Galletas","Pan", "Leche","Papas","Queso"]
        boton_productos ['values'] = productos

        self.boton_comprar = tk.Button(master, text="Comprar")
        self.boton_comprar.pack(padx=20,pady=10)

        self.boton_salir = tk.Button(master, text="Salir", command=master.quit)
        self.boton_salir.pack(padx=20,pady=10)

root = tk.Tk()
tienda_gui = tienda(root)
root.mainloop()