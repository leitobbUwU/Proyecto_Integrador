import tkinter as tk
from logicaProyecto import Login
from Tienda import InterfazTiendita
from tkinter import messagebox

class Interfaz:
    
    def __init__(self, ventana):
#1.Instanciamos un objeto ventana
        self.ventana=ventana
        self.ventana.title("Practica 11.3 Frames")
        self.ventana.geometry("600x400")
        self.ventana.config(bg='#A9F5BC')

        titulo1 = tk.Label(ventana, text="Usuario:", font=("Helvetica",30), bg='#A9F5BC')
        titulo1.pack(padx=20,pady=5)
        self.usuario = tk.Entry(ventana, font=("Helvetica", 30), bg='#A9F5BC')
        self.usuario.pack(padx=20,pady=10)

        titulo2 = tk.Label(ventana, text="Contraseña:", font=("Helvetica", 30), bg='#A9F5BC')
        titulo2.pack(padx=20, pady=5)
        self.contraseña = tk.Entry(ventana, show="*", font=("Helvetica", 30), bg='#A9F5BC')
        self.contraseña.pack(padx=20, pady=10, )

        self.Generar= tk.Button(ventana, text="Ingresar", fg="red", bg='#A9F5BC', font=("Helvetica", 15), command=self.verificar)
        self.Generar.pack()
        
    def verificar(self):
        Usuario = self.usuario.get()
        Password = self.contraseña.get()
        if Usuario == "" or Password == "":
            mensaje = "Ingrese ambos campos"
        else:
            login = Login(Usuario, Password)
            if login.login():
                mensaje="Bienvenido"
                # muestra el mensaje en una ventana emergente
                messagebox.showinfo(title="Resultado", message=mensaje)
                # Cierra la ventana principal
                self.ventana.destroy()
                # Crea una instancia de InterfazTiendita
                tiendita = InterfazTiendita()
                # Llama al método mainloop de la ventana
                tiendita.ventana.mainloop()
            else:
                mensaje = "Revise sus datos e intente de nuevo."
                # muestra el mensaje de error en una ventana emergente
                messagebox.showerror(title="Resultado", message=mensaje)

ventana= tk.Tk()
interfaz_login=Interfaz(ventana)
ventana.mainloop()