from dojos_flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        print(f"data: {data}")
        self.id = data['id']
        self.name= data['name']
        self.created_at = data['created_at']
        # TODO cambiar el nombre de la columna en la BDD
        self.updated_at = data['update_at']

    @classmethod
    def created(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result= connectToMySQL ('esquemas_dojos_y_ninjas').query_db(query, data)
        return result

    #Lectura(read)
    @classmethod
    def all_dojos(cls):
        query="SELECT * FROM dojos;"
        result= connectToMySQL('esquemas_dojos_y_ninjas').query_db(query)
        dojos = []
        for dict in result:
            dojos.append(cls(dict))
        return dojos

    @classmethod
    def get_dojo(cls, data):
        print(f"get_dojo. data: {data}")
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result= connectToMySQL('esquemas_dojos_y_ninjas').query_db(query, data)
        print(f"get_dojo. result: {result}")
        return cls(result[0])

    @classmethod
    def get_ninjas_in_dojo(cls, data):
        consulta = """SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"""
        result = connectToMySQL('esquemas_dojos_y_ninjas').query_db(consulta, data)
        return result
