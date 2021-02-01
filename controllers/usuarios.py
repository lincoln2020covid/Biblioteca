from models.usuario import Usuario
from models.libros import Libros
from helper.menu import Menu
from helper.helper import input_data, print_table, question
import uuid

class UsuariosController:
    def __init__(self):
        self.usuario = Usuario()
        self.libro = Libros()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ==================
                      Usuarios
                ==================
                ''')
                lista_menu = ["Listar", "Buscar", "Crear", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_usuarios()
                elif respuesta == 2:
                    self.search_usuario()
                elif respuesta == 3:
                    self.insert_usuario()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def all_usuarios(self):
        print('''
        ==========================
               Listar Usuario
        ==========================
        ''')
        usuarios = self.usuario.get_usuarios('id_usuario')
        print(print_table(usuarios, ['dni_usuario', 'id_usuario', 'nombre_usuario']))
        input('\nPresiona una tecla para continuar...')

    def search_usuario(self):
        print('''
        ========================
              Buscar Usuario
        ========================
        ''')
        try:
            dni_usuario = input_data("Ingrese el DNI del usuario >> ", "int")
            usuario = self.usuario.get_usuario({
                'dni_usuario' : dni_usuario
            })
            print(print_table(usuario, ['id_usuario', 'nombre_usuario']))

###### DESCONOCIMIENTO DE LIBRO ######
######################################

            if libro:
                if question('¿Deseas dar mantenimiento al libro?'):
                    opciones = ['Asignar Curso', 'Editar Profesor', 'Eliminar profesor', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        pass
                    elif respuesta == 2:
                        self.update_profesor(profesor_id)
                    elif respuesta == 3:
                        pass
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')

###### DESCONOCIMIENTO DE LIBRO ######
######################################

    def insert_usuario(self):
        dni_usuario = input_data('Ingrese el DNI del usuario >> ', 'int')
        id_usuario = uuid.uuid4().hex[:8]
        nombre_usuario = input_data('Ingrese el nombre del usuario >> ')
        self.usuario.insert_usuario({
            'dni_usuario': dni_usuario,
            'id_usuario': id_usuario,
            'nombre_usuario': nombre_usuario
        })
        print('''
        ==================================
               Nuevo usuario agregado
        ==================================
        ''')
        self.all_usuarios()

    def update_usuario(self, dni_usuario):
        id_usuario = input_data('Ingrese el nuevo ID asignado al usuario >> ', 'int')
        nombre_usuario = input_data('Ingrese el nombre del usuario >> ')
        self.usuario.update_libro({
            'dni_usuario': dni_usuario
        }, {
            'id_usuario': id_usuario,
            'nombre_usuario': nombre_usuario
        })
        print('''
        ==============================
              Usuario Actualizado
        ==============================
        ''')