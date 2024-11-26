##class Alumno:
##     def _int_(self):
##        self.nombre=nombre
##        self.nota=nota
##     def imprimir(self):
##         print("Nombre: ",self.nombre)
##         print("Nota: ",self.nota)
##     def resultado(self):
##         if self.nota < 5:
##             print("El alumno ha suspendido")
##         else:
##             print("El alumno ha aprobado")
##alumno1=Alumno()
##alumno2=Alumno()
##alumno1.inicializar("ivan",8)
##alumno2.inicializar("juan",4)
##alumno1.imprimir()
##alumno1.resultado()
##alumno2.imprimir()
##alumno2.resultado()
##class Persona:
##    def inicializar(self,nombre,edad):
##        self.nombre=nombre
##        self.edad=edad
##    def imprimir(self):
##        print("Nombre: ",self.nombre)
##        print("Edad: ",self.edad)
##    def mayor_edad(self):
##        if self.edad >= 18:
##             print("Es mayor de edad")
##        else:
##             print("No es mayor de edad")
##persona1=Persona()
##persona1.inicializar("Ivan",23)
##persona2=Persona()
##persona2.inicializar("Carlos",17)
##persona1.imprimir()
##persona1.mayor_edad()
##persona2.imprimir()
##persona2.mayor_edad()
##class Triangulo:
##    def inicializar(self):
##        self.lado1=int(input("Ingrese el valor del primer lado: "))
##        self.lado2=int(input("Ingrese el valor del segundo lado: "))
##        self.lado3=int(input("Ingrese el valor del tercer lado: "))
##    def imprimir(self):
##        print("Los lados del triángulo tienen el valor de")
##        print("Lado 1: ",self.lado1)
##        print("Lado 2: ",self.lado2)
##        print("Lado 3: ",self.lado3)
##    def mayor(self):
##        print("El lado mayor es")
##        if self.lado1>self.lado2 and self.lado1>self.lado3:
##            print("Lado 1: ",self.lado1)
##        elif self.lado2>self.lado3:
##            print("Lado 2: ",self.lado2)
##        else:
##            print("Lado 3: ",self.lado3)
##    def tipo(self):
##        if self.lado1==self.lado2 and self.lado1==self.lado3:
##            print("Es un triángulo equilátero")
##        elif self.lado1!=self.lado2 and self.lado1!=self.lado3:
##            print("Es un triángulo escaleno")
##        else:
##            print("Es un triángulo isósceles")
##figura=Triangulo()
##figura.inicializar()
##figura.imprimir()
##figura.mayor()
##figura.tipo()
##class Calculadora:
##    def __init__(self):
##        self.valor1=int(input("Ingrese el primer valor: "))
##        self.valor2=int(input("Ingrese el segundo valor: "))
##        self.menu()
##    def suma(self):
##        suma=self.valor1+self.valor2
##        print("El resultado de la suma de los valores es: ",suma)
##        self.menu()
##    def resta(self):
##        resta=self.valor1-self.valor2
##        print("El resultado de la resta de los valores es: ",resta)
##        self.menu()
##    def multiplicacion(self):
##        pro=self.valor1*self.valor2
##        print("El resultado de la multiplicación de los valores es: ",pro)
##        self.menu()
##    def division(self):
##        div=self.valor1/self.valor2
##        print("El resultado de la división de los valores es: ",div)
##        self.menu()
##    def imprimir(self):
##        print("Los valores son: ")
##        print("Valor 1: ",self.valor1)
##        print("Valor 2: ",self.valor2)
##        self.menu()
##    def menu(self):
##        opcion = input(("ingrese 1:suma,2:resta,3:producto,4:divison,5:mostrar,6:exit"))
##        if opcion == "1":
##            self.suma()
##        elif opcion == "2":
##            self.resta()
##        elif opcion == "3":
##            self.multiplicacion()
##        elif opcion == "4":
##            self.division()
##        elif opcion == "5":
##            self.imprimir()
##        elif opcion == "6":
##            exit()
##        else:
##            print("error")
##            self.menu()
##calcular=Calculadora()
##class Persona():
##    nombre="sebastian"
##    apellido = "bonilla"
##    trabajo = "inutil"
##    
##    def mostrar(self):
##        print(f"su nombre es {self.nombre}, con apellido {self.apellido} y su trabajo es {self.trabajo}")
##    def si(self):
##        print("vida")
##              
class Alumno():
    def __init__(self):
        self.nombre=input("ingrese su nombre")
        self.apellido=input("ingrese su apellido")
        self.codigo=int(input("ingrese su codigo"))
        self.nota=float(input("ingrese su nota"))
    def imprimir(self):
        print("nombre: ", self.nombre)
        print("apellido:", self.apellido)
        print("codigo:", self.codigo)
        print("nota:", self.nota)
    def resultado(self):
        if self.nota < 5:
            print("El alumno ha suspendido")
        else:
            print("El alumno ha aprobado")
alumno=Alumno()
alumno.imprimir()
alumno.resultado()        





















