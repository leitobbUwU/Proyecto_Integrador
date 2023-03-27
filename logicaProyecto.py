from tkinter import *
from tkinter import messagebox
import sqlite3
import bcrypt

class Login:
    def __init__(self, usuario, contraseña):
            self.usuario = usuario
            self.contraseña = contraseña

    def login(self):
        if self.usuario == "Usuario" and self.contraseña == "Admin":
            return True
        else:
            return False
        
        
class consulta:
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion=sqlite3.connect("D:/documentos/GitHub/Proyecto_Integrador/TiendaQueveDoes.db")
            print("Conexion exitosa")
            return conexion            
        except sqlite3.OperationalError:
            print("Error de conexion a la BD")
    
    def login(self, nom, con):
        
        conx= self.conexionBD()
        cursor = conx.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE NombreUsu = ? AND Contraseña = ?", (nom, con))
        resultado = cursor.fetchone()
        if resultado is None:
            return False
        else:
            return True


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
            conH= self.encriptarCon(con)
            datos=(nom, cor, conH)
            qrInsert= "insert into Usuarios(NombreUsu, Puesto, Contraseña) values(?,?,?)"
            
            #4. Ejecutar Insert y cerramos conexion
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", "Usuario Guardado")
            
    # Metodo para encriptar la contraseña
    def encriptarCon(self, con):
        conPlana= con
        # Se convierte con a bytes
        conPlana= conPlana.encode()
        # Le hecha la sal a la contraseña
        sal= bcrypt.gensalt()
        
        # Encriptamos la contraseña
        conHa= bcrypt.hashpw(conPlana, sal)
        print(conHa)
        
        # Envia la contraseña
        return conHa