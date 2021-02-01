from helper.menu import Menu
from controllers.libros import LibrosController
from controllers.usuarios import UsuariosController

def app():
    try:
        print('''
        ============================
            Sistema de Biblioteca
        ============================
        ''')
        menu_principal = ["Libros", "Usuarios", "Disponibilidad"]
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            libros = LibrosController()
            libros.menu()
            if libros.salir:
                app()
        elif respuesta == 2:
            usuarios = UsuariosController()
            usuarios.menu()
            if usuarios.salir:
                app()
        elif respuesta == 3:
            pass

        print("\n Gracias por utilizar el sistema \n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

app()