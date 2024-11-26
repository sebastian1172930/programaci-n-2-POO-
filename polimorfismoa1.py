from datetime import datetime

class UISbarbosa:
    def __init__(self, nombre_apellido, doc_identidad, fecha_nacimiento, profesion, horas_trabajadas):
        self.nombre_apellido = nombre_apellido
        self.doc_identidad = doc_identidad
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') 
        self.profesion = profesion
        self.horas_trabajadas = horas_trabajadas

    def calcular_edad(self):
        today = datetime.today()
        age = today.year - self.fecha_nacimiento.year - (
            (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return age

    def mostrar(self):
        print("\nDatos del funcionario:")
        print(f"Nombre y Apellido: {self.nombre_apellido}")
        print(f"Documento de Identidad: {self.doc_identidad}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento.strftime('%Y-%m-%d')}")
        print(f"Edad: {self.calcular_edad()} años")
        print(f"Profesión: {self.profesion}")
        print(f"Horas Trabajadas: {self.horas_trabajadas}")


class Vigilancia(UISbarbosa):
    def __init__(self, nombre_apellido, doc_identidad, fecha_nacimiento, profesion, horas_trabajadas, turno, lugar):
        super().__init__(nombre_apellido, doc_identidad, fecha_nacimiento, profesion, horas_trabajadas)
        self.turno = turno
        self.lugar = lugar

    def sueldo(self):
        if self.turno.lower() == 'diurno':
            return self.horas_trabajadas * 6042
        elif self.turno.lower() == 'nocturno':
            return self.horas_trabajadas * 9478
        return 0

    def mostrar(self):
        super().mostrar()
        print(f"Turno: {self.turno}")
        print(f"Lugar: {self.lugar}")
        print(f"Sueldo: ${self.sueldo()}")


class Auxiliares(Vigilancia):
    def funciones(self):
        print("Funciones: Apoyo en vigilancia y tareas administrativas básicas.")

    def sueldo(self):
        # Sueldo igual al de Vigilancia
        return super().sueldo()


class Administrativos(UISbarbosa):
    def __init__(self, nombre_apellido, doc_identidad, fecha_nacimiento, profesion, horas_trabajadas, dependencia):
        super().__init__(nombre_apellido, doc_identidad, fecha_nacimiento, profesion, horas_trabajadas)
        self.dependencia = dependencia

    def sueldo(self):
        return self.horas_trabajadas * 20000 

    def funciones(self):
        print("Funciones: Gestión de documentos, organización de personal y tareas administrativas en su dependencia.")

    def mostrar(self):
        super().mostrar()
        print(f"Dependencia: {self.dependencia}")
        print(f"Sueldo: ${self.sueldo()}")

# Solicitud de datos
funcionario = input("Ingrese el tipo de funcionario (Vigilancia, Auxiliares, Administrativos): ").strip().capitalize()

nombre_apellido = input("Ingrese su nombre y apellido: ")
doc_identidad = input("Ingrese su documento de identidad: ")
fecha_nacimiento = input("Ingrese su fecha de nacimiento (año-mes-dia): ")
profesion = input("Ingrese su profesión: ")
horas_trabajadas = int(input("Ingrese las horas trabajadas: "))

if funcionario == "Vigilancia":
    turno = input("Ingrese el turno de trabajo (Diurno/Nocturno): ")
    lugar = input("Ingrese el lugar de trabajo: ")
    empleado = Vigilancia(nombre_apellido, doc_identidad, fecha_nacimiento, profesion, horas_trabajadas, turno, lugar)
    empleado.mostrar()

elif funcionario == "Auxiliares":
    turno = input("Ingrese el turno de trabajo (Diurno/Nocturno): ")
    lugar = input("Ingrese el lugar de trabajo: ")
    empleado = Auxiliares(nombre_apellido, doc_identidad, fecha_nacimiento, profesion, horas_trabajadas, turno, lugar)
    empleado.mostrar()
    empleado.funciones()

elif funcionario == "Administrativos":
    dependencia = input("Ingrese el área a la que pertenece: ")
    empleado = Administrativos(nombre_apellido, doc_identidad, fecha_nacimiento, profesion, horas_trabajadas, dependencia)
    empleado.mostrar()
    empleado.funciones()

else:
    print("Tipo de funcionario no reconocido.")


