##class Persona():
##
##    def __init__(self):
##        self.nombre=input('ingrese su nombre ')
##        self.edad=int(input('ingrese su edad '))
##        self.ht=10
##        
##    def imprimir(self):
##        print ('su nombre es ', self.nombre, ' ', 'edad ', self.edad, ' años', self.ht, ' horas trabajadas')
##        
##class Sueldo(Persona):
##    def __init__(self):
##        super().__init__()#heredo atributos
##        self.ht=float(input('horas trabajadas'))
##
##    def pago(self):
##        sueldot=self.ht*79000
##        print(sueldot)
##        
##
##class Vida(Sueldo):
##    def __init__(self):
##        super().__init__()
##        self.actividad=input('describa que actividad fisica realiza')
##
##    def imprimir2(self):
##        print(self.actividad)
##
##        
##class Persona1():
##    def __init__(self):
##        self.nombre=input('Ingrese su nombre: ')
##        self.edad=int(input('Ingrese su edad: '))
##
##    def imprimir(self):
##        print ('su nombre es ', self.nombre, ' ', 'edad ', self.edad, ' años')
#######uis barbo uis uis barbosa barbosa uis uis sede barbosa

class UISBarbosa():
    def __init__(self):
        self.nombre_apellidos=input("ingrese su nombre")
        self.docidentidad=input("ingrese su documento de identidad")
        self.fecha=input("ingrese su fecha de nacimiento")
        self.profesion=input("ingrese su profesion")
        self.horas_trabajadas=int(input("ingrese sus horas trabajadas"))

    def mostrar(self):
        print('su nombre es ', self.nombre_apellidos, 'edad ', self.edad, ' documento de identidad', self.docidentidad, " horas trabajadas ", self.horas_trabajadas, " Profesion ", self.profesion)

class Vigilancia():
    def __init__(self):
        
















              
