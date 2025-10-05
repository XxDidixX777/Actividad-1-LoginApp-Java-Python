class Usuario:
    def __init__(self, Nombre, Apellido, Email, Username, Clave, Rol):
        self.nombre = Nombre
        self.apellido = Apellido  
        self.email = Email
        self.username = Username
        self.clave = Clave
        self.rol = Rol

    def ValidarUsuario(self, Username, Clave):
        if self.username == Username and self.clave == Clave:
            return True
        else:
            return False

    @staticmethod
    def registrarUsuarios(Nombre, Apellido, Email, Username, Clave, Rol):
        from Clases.Conector import Conector 
        con = Conector()
        sql = """INSERT INTO usuarios (Nombre, Apellido, Email, Username, Clave, Rol) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        values = (Nombre, Apellido, Email, Username, Clave, Rol)
        return con.execute_query(sql, values)
