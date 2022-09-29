from unittest import result
from dojos_flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name= data['first_name']
        self.last_name= data['last_name']
        self.age= data['age']
        self.dojo_id=data['dojo_id']
        self.created_at= data['created_at']
        self.update_at=data['update_at']

#metodo de creacion (CREATE)
    @classmethod
    def created_ninja(cls, data):
        query = """INSERT INTO ninjas (first_name, last_name, age, dojo_id)
        VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW()"""
        result= connectToMySQL ('shema_dojos_ninjas').query_db(query, data)
        return result

    @classmethod
    def get_ninja(cls, data):
        query= "SELECT *FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL ('shema_dojos_ninjas').query_db(query, data)
        return result


