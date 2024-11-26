import pandas as pd
import re

class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        if self.validar_correo(correo):
            self.correo = correo
        else:
            raise ValueError("Correo electrónico no válido")

    def validar_correo(self, correo):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, correo)

class Agenda:
    def __init__(self, archivo_csv="C:/Users/bonil/OneDrive/Documentos/programacion 2/contactos.csv"):
        self.archivo_csv = archivo_csv
        try:
            self.contactos = pd.read_csv(self.archivo_csv)
        except FileNotFoundError:
            self.contactos = pd.DataFrame(columns=['Nombre', 'Teléfono', 'Correo'])
    
    def añadir_contacto(self, nombre, telefono, correo):
        try:
            contacto = Contacto(nombre, telefono, correo)
            nuevo_contacto = {'Nombre': contacto.nombre, 'Teléfono': contacto.telefono, 'Correo': contacto.correo}
            self.contactos = self.contactos.append(nuevo_contacto, ignore_index=True)
            self.guardar()
            print(f"Contacto {nombre} añadido correctamente.")
        except ValueError as e:
            print(e)
    
    def lista_contactos(self):
        if not self.contactos.empty:
            print(self.contactos)
        else:
            print("No hay contactos guardados.")
    
    def buscar_contacto(self, nombre):
        contacto = self.contactos[self.contactos['Nombre'].str.contains(nombre, case=False, na=False)]
        if not contacto.empty:
            print(contacto)
        else:
            print(f"No se encontraron contactos con el nombre: {nombre}")
    
    def editar_contacto(self, nombre):
        indice = self.contactos[self.contactos['Nombre'].str.contains(nombre, case=False, na=False)].index
        if not indice.empty:
            print(f"Editando el contacto {nombre}. Deja vacío si no deseas cambiar.")
            nuevo_nombre = input("Nuevo nombre: ").strip() or self.contactos.at[indice[0], 'Nombre']
            nuevo_telefono = input("Nuevo teléfono: ").strip() or self.contactos.at[indice[0], 'Teléfono']
            nuevo_correo = input("Nuevo correo: ").strip()
            if nuevo_correo and not Contacto.validar_correo(None, nuevo_correo):
                print("Correo electrónico no válido.")
            else:
                self.contactos.at[indice[0], 'Nombre'] = nuevo_nombre
                self.contactos.at[indice[0], 'Teléfono'] = nuevo_telefono
                if nuevo_correo:
                    self.contactos.at[indice[0], 'Correo'] = nuevo_correo
                self.guardar()
                print(f"Contacto {nombre} actualizado correctamente.")
        else:
            print(f"No se encontraron contactos con el nombre: {nombre}")
    
    def eliminar_contacto(self, nombre):
        indice = self.contactos[self.contactos['Nombre'].str.contains(nombre, case=False, na=False)].index
        if not indice.empty:
            self.contactos = self.contactos.drop(indice)
            self.guardar()
            print(f"Contacto {nombre} eliminado correctamente.")
        else:
            print(f"No se encontraron contactos con el nombre: {nombre}")
    
    def cerrar_agenda(self):
        print("Cerrando agenda...")
    
    def guardar(self):
        self.contactos.to_csv(self.archivo_csv, index=False)

def menu():
    agenda = Agenda()
    
    while True:
        print("\n----- Menú de Agenda -----")
        print("1. Añadir contacto")
        print("2. Lista de contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Eliminar contacto")
        print("6. Cerrar agenda")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            nombre = input("Nombre: ").strip()
            telefono = input("Teléfono: ").strip()
            correo = input("Correo electrónico: ").strip()
            agenda.añadir_contacto(nombre, telefono, correo)
        elif opcion == '2':
            agenda.lista_contactos()
        elif opcion == '3':
            nombre = input("Ingrese el nombre a buscar: ").strip()
            agenda.buscar_contacto(nombre)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del contacto a editar: ").strip()
            agenda.editar_contacto(nombre)
        elif opcion == '5':
            nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
            agenda.eliminar_contacto(nombre)
        elif opcion == '6':
            agenda.cerrar_agenda()
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

menu()
