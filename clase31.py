##def hoy():
##    print("bienvenudo a la clase")
    
##def Sumar(num1,num2):
##    global resultado
##    resultado = num1 + num2
##    print(resultado)
##    return resultado #debe tener donde almacenar el return"sebas"
##a=float(input("ingrese un numero"))
##b=float(input("ingrese un numero"))
##sebas = Sumar(a,b)
##print(sebas)
##

##def perimetro_triangulo ( cateto1 : float ,cateto2:float)->float:
##
##    hipotenusa=calcular_hip(cateto1,cateto2)
##
##    return cateto1+cateto2+hipotenusa
##
##
##
##def calcular_hip(cateto1:float,cateto2:float)->float:
##
##    suma_cuadrados=(cateto1**2)+(cateto2**2)
##
##    hipotenusa=pow(suma_cuadrados,0.5)
##
##    return hipotenusa
##
##
##
##cadena_cat_1=input("Indique la longitud del primer cateto: ")
##
##cadena_cat_2=input("Indique la longitud del segundo cateto: ")
##
##cat_1=float(cadena_cat_1)
##
##cat_2=float(cadena_cat_2)
##
##perimetro=perimetro_triangulo(cat_1,cat_2)
##
##print("El perímetro de un triángulo rectángulo que tenga catetos de longitud",cat_1,"y",cat_2,"es",perimetro)
##

##def area_perimtero_rectangulo(base, altura) :
##    perimetro = 2*base + 2*altura
##    area = base*altura
##    return perimetro,area
##bas = float(input("ingrese la base del rectangulo"))
##alt = float(input("ingrese la altura del rectangulo"))
##perimetro, area = area_perimtero_rectangulo(bas,alt)
##print("perimetro: ", perimetro, " area: ", area)



def suma():
    a = float(input("numero "))
    b = float(input("numero "))
    print(a+b)
    menu()
def resta():
    a = float(input("numero "))
    b = float(input("numero "))
    print(a-b)
    menu()
def multiplicacion():
    a = float(input("numero "))
    b = float(input("numero "))
    print(a*b)
    menu()
def cociente():
    a = float(input("numero "))
    b = float(input("numero "))
    print(a/b)
    menu()
def menu():
    print(""" Seleccione: 1:suma
                          2:resta
                          3:multiplicacion
                          4:cociente
                          5:salir""")
    op=int(input("opcion deseada "))
    while op>=1 and op<=5:
        if op == 1:
            suma()
        elif op == 2:
            resta()
        elif op == 3:
            multiplicacion()
        elif op == 4:
            cociente()
        elif op == 5:
            exit()
        else:
            print("error")
menu()
            



