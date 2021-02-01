from models.libros import Libros
from models.usuario import Usuario
from helper.menu import Menu
from helper.helper import input_data, print_table, question


class LibrosController:
    def __init__(self):
        self.libros = Libros()
        self.usuario = Usuario()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ==================
                      Libros
                ==================
                ''')
                lista_menu = ["Listar", "Buscar", "Crear", "Actualizar", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_libros()
                elif respuesta == 2:
                    self.search_libro()
                elif respuesta == 3:
                    self.insert_libro()
                elif respuesta == 4:
                    self.update_libro()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def all_libros(self):
        print('''
        ==========================
               Listar Libros
        ==========================
        ''')
        libros = self.libros.get_libros('id_libro')
        print(print_table(libros, ['id_libro', 'nombre_libro', 'editorial', 'disponibilidad']))
        input('\nPresiona una tecla para continuar...')

    def search_libro(self):
        print('''
        ========================
              Buscar Libro
        ========================
        ''')
        try:
            id_libro = input_data("Ingrese el ID del libro >> ", "int")
            libro = self.libros.get_libro({
                'id_libro': id_libro
            })
            print(print_table(libro, ['id_libro', 'nombre_libro', 'editorial', 'disponibilidad']))

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

    def insert_libro(self):
        nombre_libro = input_data('Ingrese el nombre del libro >> ')
        editorial = input_data('Ingrese la editorial del libro >> ')
        disponibilidad = input_data('Ingrese la disponibilidad del libro >> ', 'int')
        self.libros.insert_libro({
            'nombre_libro': nombre_libro,
            'editorial': editorial,
            'disponibilidad': disponibilidad
        })
        print('''
        ==================================
               Nuevo libro agregado
        ==================================
        ''')
        self.all_libros()

    def update_libro(self, id_libro):
        nombre_libro = input_data('Ingrese el nuevo nombre del libro >> ')
        editorial = input_data('Ingrese la nueva editorial del libro >> ')
        disponibilidad = input_data('Ingrese la disponibilidad del libro >> ', 'int')
        self.libro.update_libro({
            'id_libro': id_libro
        }, {
            'nombre_libro': nombre_libro,
            'editorial': editorial,
            'disponibilidad': disponibilidad
        })
        print('''
        ==============================
              Libro Actualizado
        ==============================
        ''')