from tkinter import *
from tkinter import messagebox
import sqlite3

import bcrypt

class Login:
    
    def __init__(self, usuario, contraseña):
            self.usuario = usuario
            self.contraseña = contraseña

    def login(self):
        try:
            conx = sqlite3.connect("C:/Users/LeitobbUwU/Desktop/FPOO/Proyecto/TiendaQueveDoes.db")
            cursor = conx.cursor()
            qrSelect = "SELECT * FROM Usuarios WHERE NombreUsu=? AND Contraseña=?"
            cursor.execute(qrSelect, (self.usuario, self.contraseña))
            resultado = cursor.fetchone()
            conx.close()

            if resultado:
                return True
            else:
                return False

        except sqlite3.OperationalError:
            print("Error de conexion a la BD")
            return False

class Resgistro:
    
    def __init__(self):
        pass
    
    # Metodo para intentar una conexión a la BD
    def conexionBD(self):
        try:
            conexion=sqlite3.connect("D:/documentos/GitHub/Proyecto_Integrador/TiendaQueveDoes.db")
            print("Conexion exitosa")
            return conexion            
        except sqlite3.OperationalError:
            print("Error de conexion a la BD")
        
    # Metodo para capturar datos del entry
    def guardarUsuarios(self, nom, cor, con):
        
        #1. usamos una conexión para registrar
        conx= self.conexionBD()
        
        #2. Checar que el entry contenga algo
        if(nom== " " or cor == "" or con == ""):
            messagebox.showwarning("Aguas", "Formulario incompleto")
        else:
            #3. Preparamos Cursor, Datos, QuerySQL
            cursor = conx.cursor()
            # Se manda a encriptar la contraseña y se agrega en el paquete de datos enviados a la BD
            datos=(nom, cor, con)
            qrInsert= "insert into Usuarios(NombreUsu, Puesto, Contraseña) values(?,?,?)"
            
            #4. Ejecutar Insert y cerramos conexion
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", "Usuario Guardado")