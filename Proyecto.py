import tkinter as tk
from tkinter import ttk
from logicaProyecto import *
from Tienda import InterfazTiendita
from productos import productos
from Gerencia import *
from tkinter import messagebox

class Interfaz:
    def __init__(self, ventana):
    #1.Instanciamos un objeto ventana
        self.ventana=ventana
        self.ventana.title("Practica 11.3 Frames")
        self.ventana.geometry("600x400")
        self.ventana.config(bg='#A9F5BC')
        
        ventana2=ttk.Notebook(self.ventana)
        ventana2.pack(fill='both', expand=True)
        
        pestana1=ttk.Frame(ventana2)
        pestana2=ttk.Frame(ventana2)

        titulo1 = tk.Label(pestana1, text="Usuario:", font=("Helvetica",30), bg='#A9F5BC')
        titulo1.pack(padx=20,pady=5)
        self.usuario = tk.Entry(pestana1, font=("Helvetica", 30), bg='#A9F5BC')
        self.usuario.pack(padx=20,pady=10)

        titulo2 = tk.Label(pestana1, text="Contraseña:", font=("Helvetica", 30), bg='#A9F5BC')
        titulo2.pack(padx=20, pady=5)
        self.contraseña = tk.Entry(pestana1, show="*", font=("Helvetica", 30), bg='#A9F5BC')
        self.contraseña.pack(padx=20, pady=10, )

        self.Generar= tk.Button(pestana1, text="Ingresar", fg="red", bg='#A9F5BC', 
                                font=("Helvetica", 15), command=self.verificacion)
        self.Generar.pack()
        
        ventana2.add(pestana1,text='Login')
        ventana2.add(pestana2,text='Registro Rapido')
        
        #Pestaña 2 Creamos la actualizacion de todo.
        titulo2 = tk.Label(pestana2, text="Usuario:", font=("Helvetica",20)).pack(padx=20,pady=5)
        self.usuarioReg = tk.Entry(pestana2, font=("Helvetica", 20))
        self.usuarioReg.pack(padx=20,pady=10)
        
        titulo2 = tk.Label(pestana2, text="Cargo:", font=("Helvetica",20)).pack(padx=20,pady=5)
        self.correoReg = tk.StringVar()
        self.checkbutton = tk.Checkbutton(pestana2, text="Cliente", font=("Helvetica", 20), variable=self.correoReg, onvalue="Cliente", offvalue="")
        self.checkbutton.pack(padx=20,pady=10)

        titulo2 = tk.Label(pestana2, text="Contraseña:", font=("Helvetica", 20)).pack(padx=20, pady=5)
        self.contraseñaReg = tk.Entry(pestana2, show="*", font=("Helvetica", 20))
        self.contraseñaReg.pack(padx=20, pady=10, )

        self.Generar= tk.Button(pestana2, text="Ingresar", fg="white", bg='#1174B5', font=("Helvetica", 15), 
                                command=self.ejecutaInsert)
        self.Generar.pack()
        
    controlador= Resgistro()

    def ejecutaInsert(self):
        if self.correoReg.get() == "":
            messagebox.showwarning("Aguas", "Debe marcar la casilla de Cliente")
        else:
            self.controlador.guardarUsuarios(self.usuarioReg.get(), self.correoReg.get(), self.contraseñaReg.get())  
        
    def mostrar_interfaz(self, rol):
        if rol == "Gerente":
            # Mostrar la interfaz del Gerente
            Gerente=gerencia()
            pass
        elif rol == "Empleado":
            # Mostrar la interfaz del Empleado
            Empleado=productos()
            pass
        else:
            # Mostrar la interfaz del Cliente
            Cliente=InterfazTiendita()
            pass
        
    def verificacion(self):
        Usuario = self.usuario.get()
        Password = self.contraseña.get()
        if Usuario == "" or Password == "":
            mensaje = "Ingrese ambos campos"
        else:
            login = Login(Usuario, Password)
            autenticado, rol = login.login() # type: ignore
            if autenticado:
                mensaje="Bienvenido"
                # muestra el mensaje en una ventana emergente
                messagebox.showinfo(title="Resultado", message=mensaje)
                # Cierra la ventana principal
                self.ventana.destroy()
                # Mostrar la interfaz correspondiente
                self.mostrar_interfaz(rol)
            else:
                mensaje = "Revise sus datos e intente de nuevo."
                # muestra el mensaje de error en una ventana emergente
                messagebox.showerror(title="Resultado", message=mensaje)

ventana= tk.Tk()
i=Interfaz(ventana)
ventana.mainloop()