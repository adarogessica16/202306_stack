import os
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.utils.expresiones_regulares import EMAIL_REGEX

class User:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.email= data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW() );"
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
    
    @staticmethod
    def validar(formulario):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        resultado = connectToMySQL(os.getenv('BASE_DE_DATOS')).query_db(query,formulario)
        if len(resultado) >= 1:
            flash("Ya existe","info")
            is_valid=False
        if not EMAIL_REGEX.match(formulario['email']):
            flash("Invalido", "error")
            is_valid=False
        return is_valid
    
    @classmethod
    def delete(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(os.getenv('BASE_DE_DATOS')).query_db(query,data)
    