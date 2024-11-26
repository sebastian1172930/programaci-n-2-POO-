import math
ingresar="si"
while ingresar=="si":
    print("""perimetros y areas de figuras geometricas
      marque 1:cuadrado
             2:triangulo
             3:circunferencia
             4:rombo""")

    figurA=input("ingrese la opcion ")
    if figurA=="1":
        lado=float(input("ingrese el lado "))
        peri=lado*4
        area=lado*lado
        print("perimetro = ",peri," area = ",area)
    elif figurA=="2":
        a=float(input("porfavor ingrese el lado de un triangulo "))
        b=float(input("porfavor ingrese otro lado del triangulo "))
        c=float(input("porfavor ingrese otro lado del triangulo "))
        semi=(a+b+c)/2
        area=math.sqrt(semi*(semi-a)*(semi-b)*(semi-c))
        perit=a+b+c
        print("el area = ",area," el perimetro = ",round(perit,2))
    elif figurA=="3":
        radio=float(input("porfavor ingrese el radio del circulo "))
        peric=2*math.pi*radio
        area=math.pi*radio**2
        print("el radio = ",peric," el area = ",area)
    elif figurA=="4":
        D=float(input("ingrese el ancho del rombo "))
        d=float(input("ingrese el largo del rombo "))
        a=float(input("porfavor ingrese el lado del rombo "))
        perir=(D*d)/2
        area=a+a+a+a
        print("el perimetro = ",perir," el area = ",area)
    ingresar=input("desea ingresar de nuevo si , no ")
print("programa terminado")





    


