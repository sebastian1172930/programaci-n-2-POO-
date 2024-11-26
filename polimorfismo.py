class UISbarbosa:
    def __init__(self, nombre_apellido, doc_identidad, fecha_nacimiento, profesion, horas_trabajadas):
        self.nombre_apellido = nombre_apellido
        self.doc_identidad = doc_identidad
        self.fecha_nacimiento = fecha_nacimiento
        self.profesion = profesion
        self.horas_trabajadas = horas_trabajadas

    def mostrar(self):
        print(f"Nombre y Apellido: {self.nombre_apellido}")
        print(f"Documento de Identidad: {self.doc_identidad}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento}")
        print(f"Profesión: {self.profesion}")
        print(f"Horas Trabajadas: {self.horas_trabajadas}")


class Vigilancia(UISbarbosa):
    def __init__(self, nombre_apellido, doc_identidad, fecha_nacimiento, profesion, horas_trabajadas, turno, lugar):
        super().__init__(nombre_apellido, doc_identidad, fecha_nacimiento, profesion, horas_trabajadas)
        self.turno = turno
        self.lugar = lugar

    def sueldo(self):
        return self.horas_trabajadas * 10  # Ejemplo de cálculo: $10 por hora trabajada

    def mostrar(self):
        super().mostrar()
        print(f"Turno: {self.turno}")
        print(f"Lugar: {self.lugar}")


class Auxiliares(Vigilancia):
    def funciones(self):
        print("Funciones: Apoyo en vigilancia y tareas administrativas básicas.")


class Administrativos(UISbarbosa):
    def __init__(self, nombre_apellido, doc_identidad, fecha_nacimiento, profesion, horas_trabajadas, dependencia):
        super().__init__(nombre_apellido, doc_identidad, fecha_nacimiento, profesion, horas_trabajadas)
        self.dependencia = dependencia

    def sueldo(self):
        return self.horas_trabajadas * 12  # Ejemplo de cálculo: $12 por hora trabajada

    def funciones(self):
        print("Funciones: Gestión de documentos, organización de personal y tareas administrativas en su dependencia.")

    def mostrar(self):
        super().mostrar()
        print(f"Dependencia: {self.dependencia}")


# Ejemplos de uso:
vigilante = Vigilancia("Juan Pérez", "123456789", "1990-01-01", "Vigilante", 40, "Nocturno", "Edificio A")
vigilante.mostrar()
print(f"Sueldo: ${vigilante.sueldo()}")

auxiliar = Auxiliares("Ana Gómez", "987654321", "1995-05-05", "Auxiliar de Vigilancia", 35, "Diurno", "Entrada Principal")
auxiliar.mostrar()
auxiliar.funciones()

admin = Administrativos("Carlos López", "456789123", "1985-10-10", "Administrativo", 30, "Recursos Humanos")
admin.mostrar()
print(f"Sueldo: ${admin.sueldo()}")
admin.funciones()
