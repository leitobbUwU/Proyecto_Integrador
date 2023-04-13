from tkinter import *
import tkinter as tk
from productos import *
from Usuarios import *

class gerencia:
    def __init__(self):
        # Creamos la ventana principal
        self.ventana = Tk()
        self.ventana.title("Acciones del gerente")
        self.ventana.geometry("400x200")
        
        titulo3 = Label(self.ventana, text="Productos", font=("Modern", 18)).pack(fill=tk.X, padx=20, pady=5)

        self.botonProductos = tk.Button(self.ventana, text="Manejar Productos",
                                        fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.verProductos)
        self.botonProductos.pack()
        
        titulo3 = Label(self.ventana, text="Usuarios", font=("Modern", 18)).pack(fill=tk.X, padx=20, pady=5)

        self.botonUsuarios = tk.Button(self.ventana, text="Manejar Usuarios",
                                       fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.verUsuarios)
        self.botonUsuarios.pack()
        
    def verProductos(self):
        self.ventana.destroy()
        productos()
        
    def verUsuarios(self):
        self.ventana.destroy()
        usuarios()