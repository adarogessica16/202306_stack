import os
from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User


class Recipe:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name=data['name']
        self.description=data['description']
        self.instruction= data['instruction']
        self.time_preparation= data['time_preparation']
        self.made= data['made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user= None
        
    
    @classmethod
    def get_all(cls):
        resultados_instancias = []
        query = """
    SELECT recipes.*, users.name AS creator_name
    FROM recipes
    JOIN users ON recipes.user_id = users.id;
    """
        resultados = connectToMySQL(os.getenv('BASE_DE_DATOS')).query_db(query)
        for resultado in resultados:
            resultados_instancias.append(resultado)
        return resultados_instancias


    @classmethod
    def add_recipe(cls, data):
        query = """
        INSERT INTO recipes (name, description, instruction,time_preparation,made, user_id, created_at, updated_at)
        VALUES (%(name)s,%(description)s,%(instruction)s,%(time_preparation)s,%(made)s, %(user_id)s, NOW(), NOW())"""
        data_user = {
            **data,
            'user_id': session['user']['id'],
        }

        return connectToMySQL(os.getenv('BASE_DE_DATOS')).query_db( query, data_user )
    
    @classmethod
    def get_recipe(cls, id):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        data = { 'id': id }
        resultados = connectToMySQL(os.getenv('BASE_DE_DATOS')).query_db( query, data )
        if resultados:
            return cls(resultados[0])
        return None
    
    
    #Validar formulario 
    @classmethod
    def validar_Recipe(cls,formulario):
        errores=[]

        if len(formulario['name']) < 3:
            errores.append(
                "The name must have at least 3 characters."
            )

        if len(formulario['description']) < 3:
            errores.append(
                "The description must have at least 3 characters."
            )
        if len(formulario['instruction']) < 3:
            errores.append(
                "The instruction must have at least 3 characters."
            )
        #Validar todos los campos
        for llave, valor in formulario.items():
            if len(valor) == 0:
                errores.append(
                    f"{llave} All fields are required"
                )
        return errores
    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s,instruction=%(instruction)s,time_preparation= %(time_preparation)s,made=%(made)s,updated_at=NOW() WHERE id = %(id)s;"
        data = {
            "id": int(data['id']),
            "name": data['name'],
            "description": data['description'],
            "instruction": data['instruction'],
            "time_preparation": data['time_preparation'],  
            "made":data['made']          
        } 
        return connectToMySQL(os.getenv('BASE_DE_DATOS')).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query  = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(os.getenv('BASE_DE_DATOS')).query_db(query,data)