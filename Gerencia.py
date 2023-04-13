from tkinter import *
import tkinter as tk
from productos import *

class gerencia:
    def __init__(self):
        # Creamos la ventana principal
        self.ventana = Tk()
        self.ventana.title("Acciones del gerente")
        self.ventana.geometry("600x400")
        
        titulo3 = Label(self.ventana, text="Productos", font=("Modern", 18)).pack(fill=tk.X, padx=20, pady=5)

        self.botonGuardar = tk.Button(self.ventana, text="Manejar Productos", fg="Black", bg="#00ccff", font=("Modern", 15), command=self.verProductos)
        self.botonGuardar.pack()
        
        titulo3 = Label(self.ventana, text="Usuarios", font=("Modern", 18)).pack(fill=tk.X, padx=20, pady=5)

        self.botonGuardar = tk.Button(self.ventana, text="Manejar Usuarios", fg="Black", bg="#00ccff", font=("Modern", 15))
        self.botonGuardar.pack()
        
    def verProductos(self):
        producto=productos()
        self.ventana.destroy()