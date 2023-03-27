class Login:
    def __init__(self, usuario, contraseña):
            self.usuario = usuario
            self.contraseña = contraseña

    def login(self):
        if self.usuario == "Usuario" and self.contraseña == "Admin":
            return True
        else:
            return False
        