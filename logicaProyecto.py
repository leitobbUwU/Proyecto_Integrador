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
            conx = sqlite3.connect("D:/documentos/GitHub/Proyecto_Integrador/TiendaQueveDoes.db")
            cursor = conx.cursor()
            qrSelect = "SELECT * FROM Usuarios WHERE NombreUsu=? AND Contraseña=?"
            cursor.execute(qrSelect, (self.usuario, self.contraseña))
            resultado = cursor.fetchone()
            conx.close()

            if resultado:
                # Obtener el rol del usuario
                rol = resultado[3]
                if rol == "Gerente":
                    return (True, "Gerente")
                elif rol == "Empleado":
                    return (True, "Empleado")
                else:
                    return (True, "Cliente")
            else:
                return (False, None)

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
        if(nom== "" or cor == "" or con == ""):
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
            
#/////////////////////////////////////////Gerente/////////////////////////////////////////////////////////////
class productosBD:

    def __init__(self):
        pass

    # método para crear conexiones
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("D:/documentos/GitHub/Proyecto_Integrador/TiendaQueveDoes.db")
            print("conectado a la BD")
            return conexion
        except sqlite3.OperationalError:
            print("no se pudo conectar a la BD")

    # métodos para guardar productos
    def guardarProducto(self, nombre, desc, precio, cantidad):
        # 1. usamos una conexión
        conx = self.conexionBD()

        # 2. validar parámetros vacíos
        if nombre == "" or desc == "" or precio == "" or cantidad == "":
            messagebox.showwarning("cuidado", "formulario incompleto")
        else:
            try:
                # 3. preparamos cursor, datos, query sql
                cursor = conx.cursor()
                datos = (nombre, desc, precio, cantidad)
                qrInsert = "insert into TBProductos(Nombre, Descripcion, Precio, Cantidad) values(?,?,?,?)"

                # 4. ejecutar insert y cerramos conexion
                cursor.execute(qrInsert, datos)
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito", "Producto Guardado")

            except sqlite3.OperationalError:
                print("error al guardar producto")


    # método para buscar 1 producto
    def consultarProducto(self, id):
        # 1. preparar una conexion
        conx = self.conexionBD()

        # 2.verificar si id contiene algo
        if id == "":
            messagebox.showwarning("cuidado", "id vacio escribe algo valido")
            conx.close()
        else:
            try:
                # 3. preparar el cursor y el query
                cursor = conx.cursor()
                selectQry = "select * from TBProductos where Id=" + id

                # 4. ejecutar y guardar la consulta
                cursor.execute(selectQry)
                rsProducto = cursor.fetchall()
                conx.close()
                return rsProducto

            except sqlite3.OperationalError:
                print("error consulta")

    # método para consultar a todos los productos de la base de datos
    def importarProductos(self):
        # 1. Preparar una conexión
        conx = self.conexionBD()

        try:
            # 2. Preparar el cursor y la consulta
            cursor = conx.cursor()
            selectQry = "select * from TBProductos"

            # 3. Ejecutar y guardar la consulta
            cursor.execute(selectQry)
            rsProductos = cursor.fetchall()
            conx.close()

            return rsProductos

        except sqlite3.OperationalError:
            print("error consulta")

    # método para actualizar un producto
    def actualizarProducto(self, id, nom, desc, precio, cantidad):
        # 1. Preparar una conexión
        conx = self.conexionBD()

        # 2. Checar que el id exista y el entry contenga algo
        if not id:
            messagebox.showwarning("Aguas", "ID vacío")
            return
        if not nom or not desc or not precio or not cantidad:
            messagebox.showwarning("Aguas", "Formulario incompleto")
            return
        usuario = self.consultarProducto(id)
        if not usuario:
            messagebox.showwarning("Aguas", "ID no existe en la BD")
            return
        else:
            try:
                # 3. Preparar el cursor, datos y query SQL
                cursor = conx.cursor()
                datos = (nom, desc, precio,cantidad,  id)
                qrUpdate = "update TBProductos set Nombre=?, Descripcion=?, Precio=?, Cantidad=? where Id=?"

                # 4. Ejecutar update y cerrar conexión
                cursor.execute(qrUpdate, datos)
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito", "Producto Actualizado")

            except sqlite3.OperationalError:
                print("error al actualizar producto")

    # método para eliminar un producto
    def eliminarProducto(self, id):
        # 1. preparar una conexión
        conx = self.conexionBD()

        # 2. verificar si id contiene algo
         # 2. Checar que el id exista
        if not id:
            messagebox.showwarning("Aguas", "ID vacío")
            return
        usuario = self.consultarProducto(id)
        if not usuario:
            messagebox.showwarning("Aguas", "ID no existe en la BD")
            return

        # 3. Ventana emergente de confirmación
        respuesta = messagebox.askquestion("Confirmación", "¿Estás seguro que deseas eliminar al usuario con ID "+id+"?")
        if respuesta == 'no':
            return
        else:
            try:
                # 3. preparar el cursor y el query
                cursor = conx.cursor()
                deleteQry = "delete from TBProductos where Id=" + id

                # 4. ejecutar y confirmar la eliminación
                cursor.execute(deleteQry)
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito", "Producto Eliminado")

            except sqlite3.OperationalError:
                print("error al eliminar producto")
