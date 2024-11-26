import pandas as pd
from datetime import datetime, timedelta
import os

# Rutas de los archivos CSV
libros_path = r"C:\Users\bonil\Downloads\Hoja de cálculo sin título - Hoja 1.csv"
usuarios_path = r"C:\Users\bonil\Downloads\usuarios.csv"
prestamos_path = r"C:\Users\bonil\Downloads\prestamos.csv"

# Función para crear un archivo CSV si no existe
def inicializar_archivo_csv(ruta, columnas):
    if not os.path.exists(ruta):
        df = pd.DataFrame(columns=columnas)
        df.to_csv(ruta, index=False)
        print(f"Archivo creado: {ruta}")

# Crear los archivos CSV con las columnas necesarias si no existen
inicializar_archivo_csv(libros_path, ["codigo", "autor", "tema", "paginas", "ejemplares", "precio"])
inicializar_archivo_csv(usuarios_path, ["nombre", "apellido", "clave"])
inicializar_archivo_csv(prestamos_path, ["usuario", "codigo_libro", "fecha_prestamo", "fecha_entrega"])

class Libro:
    def __init__(self, autor, tema, paginas, ejemplares, precio):
        self.codigo = self.generar_codigo()
        self.autor = autor
        self.tema = tema
        self.paginas = paginas
        self.ejemplares = ejemplares
        self.precio = precio

    def generar_codigo(self):
        # Genera un código alfanumérico único
        return f"{self.tema[:3].upper()}{int(datetime.now().timestamp())}"

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "autor": self.autor,
            "tema": self.tema,
            "paginas": self.paginas,
            "ejemplares": self.ejemplares,
            "precio": self.precio
        }

class Usuario:
    def __init__(self, nombre, apellido, clave):
        self.nombre = nombre
        self.apellido = apellido
        self.__clave = clave

    def reservar_libro(self, codigo_libro, libros_path, prestamos_path):
        libros_df = pd.read_csv(libros_path)
        prestamos_df = pd.read_csv(prestamos_path)
        
        libro = libros_df.loc[libros_df['codigo'] == codigo_libro]
        
        if libro.empty:
            print("Libro no encontrado.")
            return
        
        if libro.iloc[0]['ejemplares'] <= 0:
            print("No hay ejemplares disponibles.")
            return
        
        # Actualizar el número de ejemplares
        libros_df.loc[libros_df['codigo'] == codigo_libro, 'ejemplares'] -= 1
        libros_df.to_csv(libros_path, index=False)
        
        # Registrar el préstamo
        fecha_prestamo = datetime.now()
        fecha_entrega = fecha_prestamo + timedelta(days=15)
        
        nuevo_prestamo = pd.DataFrame([{
            "usuario": f"{self.nombre} {self.apellido}",
            "codigo_libro": codigo_libro,
            "fecha_prestamo": fecha_prestamo.strftime("%Y-%m-%d"),
            "fecha_entrega": fecha_entrega.strftime("%Y-%m-%d")
        }])
        prestamos_df = pd.concat([prestamos_df, nuevo_prestamo], ignore_index=True)
        prestamos_df.to_csv(prestamos_path, index=False)
        
        print(f"Libro {codigo_libro} reservado exitosamente. Fecha de entrega: {fecha_entrega.strftime('%Y-%m-%d')}")

    def ver_libros_prestados(self, prestamos_path):
        prestamos_df = pd.read_csv(prestamos_path)
        prestamos_usuario = prestamos_df[prestamos_df['usuario'] == f"{self.nombre} {self.apellido}"]
        
        if prestamos_usuario.empty:
            print("No tienes libros prestados.")
        else:
            print("Libros prestados:")
            print(prestamos_usuario[['codigo_libro', 'fecha_entrega']])

class Administrador(Usuario):
    def __init__(self, nombre, apellido, clave):
        super().__init__(nombre, apellido, clave)

    def crear_libro(self, autor, tema, paginas, ejemplares, precio, libros_path):
        libro = Libro(autor, tema, paginas, ejemplares, precio)
        
        try:
            libros_df = pd.read_csv(libros_path)
        except FileNotFoundError:
            libros_df = pd.DataFrame(columns=["codigo", "autor", "tema", "paginas", "ejemplares", "precio"])
        
        nuevo_libro_df = pd.DataFrame([libro.to_dict()])
        libros_df = pd.concat([libros_df, nuevo_libro_df], ignore_index=True)
        libros_df.to_csv(libros_path, index=False)
        
        print(f"Libro {libro.codigo} creado y guardado en CSV.")

    def crear_usuario_estudiante(self, nombre, apellido, clave, usuarios_path):
        usuario = Usuario(nombre, apellido, clave)
        
        try:
            usuarios_df = pd.read_csv(usuarios_path)
        except FileNotFoundError:
            usuarios_df = pd.DataFrame(columns=["nombre", "apellido", "clave"])
        
        nuevo_usuario_df = pd.DataFrame([{
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "clave": usuario._Usuario__clave
        }])
        usuarios_df = pd.concat([usuarios_df, nuevo_usuario_df], ignore_index=True)
        usuarios_df.to_csv(usuarios_path, index=False)
        
        print(f"Usuario {usuario.nombre} {usuario.apellido} creado y guardado en CSV.")

    def ver_usuarios_con_libros(self, prestamos_path):
        prestamos_df = pd.read_csv(prestamos_path)
        
        if prestamos_df.empty:
            print("No hay usuarios con libros prestados.")
        else:
            print("Usuarios con libros prestados:")
            for usuario, prestamos in prestamos_df.groupby("usuario"):
                print(f"Usuario: {usuario}")
                for _, prestamo in prestamos.iterrows():
                    print(f"  Libro: {prestamo['codigo_libro']}, Fecha de entrega: {prestamo['fecha_entrega']}")
                    fecha_entrega = datetime.strptime(prestamo['fecha_entrega'], "%Y-%m-%d")
                    if datetime.now() > fecha_entrega:
                        print("  - Este libro tiene una multa por retraso.")


