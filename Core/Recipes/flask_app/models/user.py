import os
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.utils.expresiones_regulares import EMAIL_REGEX
from flask_app.utils.expresiones_regulares import CONTRASEÑA

class User:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name=data['name']
        self.last_name=data['last_name']
        self.email= data['email']
        self.password=data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users (name, last_name,email,password, created_at, updated_at) VALUES (%(name)s,%(last_name)s,%(email)s,%(password)s, NOW(), NOW() );"
        return connectToMySQL(os.getenv('BASE_DE_DATOS')).query_db( query, data )

    @classmethod 
    def get_all(cls):
        resultados_instancias = []
        query = "SELECT * FROM users;"
        resultados = connectToMySQL(os.getenv('BASE_DE_DATOS')).query_db(query)
        for resultado in resultados:
            instancia = cls(resultado)
            resultados_instancias.append(instancia)
        return resultados_instancias

    @classmethod
    def get_by_email(cls, email): 
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data = { 'email': email }
        resultados = connectToMySQL(os.getenv('BASE_DE_DATOS')).query_db( query, data ) 
        if len(resultados)< 1:
            return False
        return cls(resultados[0])
    
    @classmethod
    def get(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = { 'id': id }
        resultados = connectToMySQL(os.getenv('BASE_DE_DATOS')).query_db( query, data )
        if resultados:
            return cls(resultados[0])
        
        return None
    
    @classmethod
    def validar(cls,formulario):
        errores=[]
        if not EMAIL_REGEX.match(formulario['email']):
            errores.append("El correo que has introducido es invalido")
        if cls.get_by_email(formulario['email']): 
            errores.append("El correo que has introducido ya esta registrado, Inicia Sesion!")

        if len(formulario['name']) < 2:
            errores.append(
                "Nombre debe tener al menos 2 caracteres"
            )

        if len(formulario['last_name']) < 2:
            errores.append(
                "Apellido debe tener al menos 2 caracteres"
            )
        
        if not CONTRASEÑA.match(formulario['password']):
            errores.append("La contraseña debe tener al menos 8 caracteres, una letra, un número y un carácter especial")
    
        return errores
    
    @classmethod
    def delete(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(os.getenv('BASE_DE_DATOS')).query_db(query,data)
    