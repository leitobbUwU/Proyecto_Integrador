import sqlite3
from tkinter import messagebox

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
            conexion=sqlite3.connect("C:/Users/LeitobbUwU/Desktop/FPOO/Proyecto/TiendaQueveDoes.db")
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
            conexion = sqlite3.connect("C:/Users/LeitobbUwU/Desktop/FPOO/Proyecto/TiendaQueveDoes.db")
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
                cursor = conx.cursor()# type: ignore
                datos = (nombre, desc, precio, cantidad)
                qrInsert = "insert into TBProductos(Nombre, Descripcion, Precio, Cantidad) values(?,?,?,?)"

                # 4. ejecutar insert y cerramos conexion
                cursor.execute(qrInsert, datos)
                conx.commit()# type: ignore
                conx.close()# type: ignore
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
            conx.close()# type: ignore
        else:
            try:
                # 3. preparar el cursor y el query
                cursor = conx.cursor()# type: ignore
                selectQry = "select * from TBProductos where Id=" + id

                # 4. ejecutar y guardar la consulta
                cursor.execute(selectQry)
                rsProducto = cursor.fetchall()
                conx.close()# type: ignore
                return rsProducto

            except sqlite3.OperationalError:
                print("error consulta")
                
    # método para buscar 1 producto
    def ConsultarNombre(self, nom):
        # 1. preparar una conexion
        conx = self.conexionBD()

        # 2.verificar si id contiene algo
        if nom == "":
            messagebox.showwarning("cuidado", "nombre vacio escribe algo valido")
            conx.close()# type: ignore
        else:
            try:
                # 3. preparar el cursor y el query
                cursor = conx.cursor()# type: ignore
                select = f"select * from TBProductos where Nombre='{nom}'"

                # 4. ejecutar y guardar la consulta
                cursor.execute(select)
                NombreProducto = cursor.fetchall()
                conx.close()# type: ignore
                return NombreProducto

            except sqlite3.OperationalError:
                print("error consulta")
                
    #Consulta de todos los articulos en la bd            
    def consultando(self):
        #1. Preparar una condición
        conx= self.conexionBD()
        #3. Preparar el cursor y el qwery
        cursor=conx.cursor() # type: ignore
        try:
            selectQry= "select Id, Nombre, Descripcion, Precio, Cantidad from TBProductos"
                    
            #4. ejecutar y guardar la consulta
            cursor.execute(selectQry)
            rsUsuario=cursor.fetchall()
            conx.close() # type: ignore
            
            #tomamos los datos guardados en la consulta y los agregamos 
            # como una lista en datos
            datos = []
            for row in rsUsuario:
                datos.append(list(row))

            #Regresamos la lista
            return datos
        except sqlite3.OperationalError:
            print("Error de consulta a la BD")

    # método para consultar a todos los productos de la base de datos
    def importarProductos(self):
        # 1. Preparar una conexión
        conx = self.conexionBD()

        try:
            # 2. Preparar el cursor y la consulta
            cursor = conx.cursor()# type: ignore
            selectQry = "select * from TBProductos"

            # 3. Ejecutar y guardar la consulta
            cursor.execute(selectQry)
            rsProductos = cursor.fetchall()
            conx.close()# type: ignore

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
                cursor = conx.cursor()# type: ignore
                datos = (nom, desc, precio,cantidad,  id)
                qrUpdate = "update TBProductos set Nombre=?, Descripcion=?, Precio=?, Cantidad=? where Id=?"

                # 4. Ejecutar update y cerrar conexión
                cursor.execute(qrUpdate, datos)
                conx.commit()# type: ignore
                conx.close()# type: ignore
                messagebox.showinfo("Exito", "Producto Actualizado")

            except sqlite3.OperationalError:
                print("error al actualizar producto")

    # método para eliminar un producto
    def eliminarProducto(self, nom):
        # 1. preparar una conexión
        conx = self.conexionBD()

        # 2. verificar si id contiene algo
         # 2. Checar que el id exista
        if not nom:
            messagebox.showwarning("Aguas", "Nombre vacío")
            return
        usuario = self.ConsultarNombre(nom)
        if not usuario:
            messagebox.showwarning("Aguas", "Nombre no existe en la BD")
            return

        # 3. Ventana emergente de confirmación
        respuesta = messagebox.askquestion("Confirmación", "¿Estás seguro que deseas eliminar "+nom+"?")
        if respuesta == 'no':
            return
        else:
            try:
                # 3. preparar el cursor y el query
                cursor = conx.cursor()# type: ignore
                deleteQry = f"delete from TBProductos where Nombre='{nom}'"

                # 4. ejecutar y confirmar la eliminación
                cursor.execute(deleteQry)
                conx.commit()# type: ignore
                conx.close()# type: ignore
                messagebox.showinfo("Exito", "Producto Eliminado")

            except sqlite3.OperationalError:
                print("error al eliminar producto")


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
class UsuariosBD:

    def __init__(self):
        pass

    # método para crear conexiones
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/LeitobbUwU/Desktop/FPOO/Proyecto/TiendaQueveDoes.db")
            print("conectado a la BD")
            return conexion
        except sqlite3.OperationalError:
            print("no se pudo conectar a la BD")

    # métodos para guardar productos
    def guardarUs(self, id, NombreUsu, Contra, Puesto):
        # 1. usamos una conexión
        conx = self.conexionBD()

        # 2. validar parámetros vacíos
        if id == "" or NombreUsu == "" or Contra == "" or Puesto == "":
            messagebox.showwarning("cuidado", "formulario incompleto")
        else:
            try:
                # 3. preparamos cursor, datos, query sql
                cursor = conx.cursor()# type: ignore
                datos = (id, NombreUsu, Contra, Puesto)
                qrInsert = "insert into Usuarios(id, NombreUsu, Contraseña, Puesto) values(?,?,?,?)"

                # 4. ejecutar insert y cerramos conexion
                cursor.execute(qrInsert, datos)
                conx.commit()# type: ignore
                conx.close()# type: ignore
                messagebox.showinfo("Exito", "Producto Guardado")

            except sqlite3.OperationalError:
                print("error al guardar producto")

    # método para buscar 1 producto
    def consultarUsuario(self, id):
        # 1. preparar una conexion
        conx = self.conexionBD()

        # 2.verificar si id contiene algo
        if id == "":
            messagebox.showwarning("cuidado", "id vacio escribe algo valido")
            conx.close()# type: ignore
        else:
            try:
                # 3. preparar el cursor y el query
                cursor = conx.cursor()# type: ignore
                selectQry = "select * from Usuario where NombreUsu=" + id

                # 4. ejecutar y guardar la consulta
                cursor.execute(selectQry)
                rsProducto = cursor.fetchall()
                conx.close()# type: ignore
                return rsProducto

            except sqlite3.OperationalError:
                print("error consulta")
                
    # método para buscar 1 producto
    def ConsultarID(self, nom):
        # 1. preparar una conexion
        conx = self.conexionBD()

        # 2.verificar si id contiene algo
        if nom == "":
            messagebox.showwarning("cuidado", "nombre vacio escribe algo valido")
            conx.close()# type: ignore
        else:
            try:
                # 3. preparar el cursor y el query
                cursor = conx.cursor()# type: ignore
                select = f"select * from Usuarios where id='{nom}'"

                # 4. ejecutar y guardar la consulta
                cursor.execute(select)
                NombreProducto = cursor.fetchall()
                conx.close()# type: ignore
                return NombreProducto

            except sqlite3.OperationalError:
                print("error consulta")
    
    # método para buscar 1 producto
    def ConsultarNombreUsu(self, nom):
        # 1. preparar una conexion
        conx = self.conexionBD()

        # 2.verificar si id contiene algo
        if nom == "":
            messagebox.showwarning("cuidado", "nombre vacio escribe algo valido")
            conx.close()# type: ignore
        else:
            try:
                # 3. preparar el cursor y el query
                cursor = conx.cursor()# type: ignore
                select = f"select * from Usuarios where NombreUsu='{nom}'"

                # 4. ejecutar y guardar la consulta
                cursor.execute(select)
                NombreProducto = cursor.fetchall()
                conx.close()# type: ignore
                return NombreProducto

            except sqlite3.OperationalError:
                print("error consulta")
                
    #Consulta de todos los articulos en la bd            
    def consultando(self):
        #1. Preparar una condición
        conx= self.conexionBD()
        #3. Preparar el cursor y el qwery
        cursor=conx.cursor() # type: ignore
        try:
            selectQry= "select id, NombreUsu, Contraseña, Puesto from Usuarios"
                    
            #4. ejecutar y guardar la consulta
            cursor.execute(selectQry)
            rsUsuario=cursor.fetchall()
            conx.close() # type: ignore
            
            #tomamos los datos guardados en la consulta y los agregamos 
            # como una lista en datos
            datos = []
            for row in rsUsuario:
                datos.append(list(row))

            #Regresamos la lista
            return datos
        except sqlite3.OperationalError:
            print("Error de consulta a la BD")

    # método para consultar a todos los productos de la base de datos
    def importarProductos(self):
        # 1. Preparar una conexión
        conx = self.conexionBD()

        try:
            # 2. Preparar el cursor y la consulta
            cursor = conx.cursor()# type: ignore
            selectQry = "select * from Usuarios"

            # 3. Ejecutar y guardar la consulta
            cursor.execute(selectQry)
            rsProductos = cursor.fetchall()
            conx.close()# type: ignore

            return rsProductos

        except sqlite3.OperationalError:
            print("error consulta")

    # método para actualizar un producto
    def actualizarUsuario(self, id, nom, contra, pues):
        # 1. Preparar una conexión
        conx = self.conexionBD()

        # 2. Checar que el id exista y el entry contenga algo
        if not id:
            messagebox.showwarning("Aguas", "ID vacío")
            return
        if not nom or not contra or not pues:
            messagebox.showwarning("Aguas", "Formulario incompleto")
            return
        usuario = self.ConsultarID(id)
        if not usuario:
            messagebox.showwarning("Aguas", "ID no existe en la BD")
            return
        else:
            try:
                # 3. Preparar el cursor, datos y query SQL
                cursor = conx.cursor()# type: ignore
                datos = (nom, contra, pues, id)
                qrUpdate = "update Usuarios set NombreUsu=?, Contraseña=?, Puesto=? where id=?"

                # 4. Ejecutar update y cerrar conexión
                cursor.execute(qrUpdate, datos)
                conx.commit()# type: ignore
                conx.close()# type: ignore
                messagebox.showinfo("Exito", "Usuario Actualizado")

            except sqlite3.OperationalError:
                print("error al actualizar producto")

    # método para eliminar un producto
    def eliminarUsuario(self, nom):
        # 1. preparar una conexión
        conx = self.conexionBD()

        # 2. verificar si id contiene algo
         # 2. Checar que el id exista
        if not nom:
            messagebox.showwarning("Aguas", "Nombre vacío")
            return
        usuario = self.ConsultarNombreUsu(nom)
        if not usuario:
            messagebox.showwarning("Aguas", "Nombre no existe en la BD")
            return

        # 3. Ventana emergente de confirmación
        respuesta = messagebox.askquestion("Confirmación", "¿Estás seguro que deseas eliminar "+nom+"?")
        if respuesta == 'no':
            return
        else:
            try:
                # 3. preparar el cursor y el query
                cursor = conx.cursor()# type: ignore
                deleteQry = f"delete from Usuarios where NombreUsu='{nom}'"

                # 4. ejecutar y confirmar la eliminación
                cursor.execute(deleteQry)
                conx.commit()# type: ignore
                conx.close()# type: ignore
                messagebox.showinfo("Exito", "Usuario Eliminado")

            except sqlite3.OperationalError:
                print("error al eliminar usuario")
