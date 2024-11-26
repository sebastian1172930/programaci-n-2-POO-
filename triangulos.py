a=float(input("porfavor ingrese un lado del triagulo "))
b=float(input("porfavor ingrese otro lado del triangulo "))
c=float(input("porfavor ingrese otro lado del triangulo "))

if (a+b>c and a+c>b and c+b>a):
    print("los datos ingresados pertenecen a un triangulo")
    if (a==b==c):
        print("triangulo equilatero")
    elif(a!=b!=c):
        print("triangulo escaleno")
    else:
        print("triangulo isoceles")
else:
    print("los datos no pertenecen a un triangulo")