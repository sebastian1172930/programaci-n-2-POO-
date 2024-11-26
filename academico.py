import csv

admin = {"admin":1234}
profes = {}
estudiantes = {}
asignaturas = []
def Academico():
    print("academico")
    crear = int(input("masque 1:Profesores , 2:Estudiantes , 3:Asignaturas , 4:salir"))
    if crear == 1:
        usu = input("ingrese el nuevo ususario")
        contra = input("ingrese la contraseña para el nuevo ususario")
        profes[usu]=contra
        print("usuario almacenado")
        Academico()
    elif crear == 4:
        print("los ususarios fueron agregados")

def Convivencia():
    print("convivencia")

def Biblioteca():
    print("biblioteca")

def votaciones():
    print("votaciones")

def Acceso():
    print("bienvenido al menu de acceso: !Administrativo , 2:profesor , 3:estudiante")
    opcion = int(input())
    if opcion==1:
        print("bienvenido administrador")
        usu = input("ingrese su usuario")
        cont = int(input("ingrese su contraseña"))
        if usu in admin and cont == admin[usu]:
            print("ok")
            modulo = int(input("a que modulo quiere ir 1:Academico , 2:convivencia , 3:votaciones , 4:biblioteca"))
            if modulo==1:
                Academico()
            elif modulo==2:
                Convivencia()
            elif modulo==3:
                Votaciones()
            elif modulo==4:
                Biblioteca()
            else:
                print("dato erroneo")
        else:
            print("dato erroneo")
Acceso()
        
        
    
