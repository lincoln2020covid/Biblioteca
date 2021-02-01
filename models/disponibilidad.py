from connection.conn import Connection

class Disponibilidad:
    def __init__(self):
        self.model = Connection('disponibilidad')

    def get_disponibilidades(self, order):
        return self.model.get_all(order)

    def get_disponibilidad(self, id_object):
        return self.model.get_by_id(id_object)

# NO SE REQUIERE "INSERTAR" DISPONIBILIDAD
# PUESTO QUE TODOS SE MODIFICARÁN CON LOS COMANDOS DE LOS OTROS DOS ARCHIVO
    # def insert_libros(self, libros):
    #     return self.model.insert(libros)

    def update_disponibilidad(self, id_object, data):
        return self.model.update(id_object, data)
    
# NO SE ELIMINA DISPONIBILIDAD
    # def delete_libros(self, id_object):
    #     return self.model.delete(id_object)

# NO SE BUSCAN DISPONIBILIDADES
    # def search_libro(self,data):
    #     return self.model.get_columns(data)
    
