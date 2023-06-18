import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL SERVER}; SERVER=LEITOBBUWU\SQLEXPRESS; DATABASE=TiendaQueveDoes; UID=LeoPI; PWD=1234')
    print("Conexion exitosa")
except Exception as ex:
    print(ex)

# # Configurar los detalles de conexión
# server = 'LEITOBBUWU/SQLEXPRESS'
# database = 'TiendaQueveDoes'
# username = 'LeitobbUwU'
# password = '4424873950'

# # Crear la cadena de conexión
# conn_str = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

# try:
#     # Intentar establecer la conexión
#     conn = pyodbc.connect(conn_str)
#     print("Conexión exitosa")
    
#     # Realizar operaciones en la base de datos si es necesario
    
#     # Cerrar la conexión
#     conn.close()
    
# except pyodbc.Error as e:
#     # Capturar errores de conexión
#     print("Error de conexión:", e)
