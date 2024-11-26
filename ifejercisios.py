########1#########
##nombre=input("porfavor ingrese su nombre")
##apellido=input("porfavor ingrese su apellido")
##documento=input("porfavor ingrese su documento de identidad")
##sueldo=float(input("porfavor ingrese su salario"))
##
##mini=1300000
##print(nombre)
##print(apellido)
##print(documento)
##print("el minimo es de $",mini, "pesos colombianos ")
##if(sueldo>mini):
##    print(nombre, "gana mas de el minimo ")
##elif(sueldo==mini):
##    print(nombre, "gana lo mismo que el minimo ")
##
##########2#########
##import math
##a=float(input("ingrese el valor a de la raiz "))
##b=float(input("ingrese el valor b de la raiz "))
##c=float(input("ingrese el valor c de la raiz "))
##dic = b**2 - 4*a*c
##if (dic>0):
##
##        raiz1 = (-b + math.sqrt(dic))/(2*a)
##        raiz1 = (-b - math.sqrt(dic))/(2*a)
##
##        print("las raices son reales y distintas", raiz1 ,raiz2)
##elif (dic==0):
##        raiz = -b/(2*a)
##        print("las raices reales son iguales ",raiz)
##else:
##        real = -b /(2*a)
##        imaginaria = math.sqrt(-dic)/(2*a)
##        print("las raices son complejas " ,real+imaginaria,"i" ,"Y" , real-imaginaria,"i")
##########3#########

##while True: 
##    letra=input("porfavor ingrese una letra ")
##
##    if len(letra)==1:
##        letra=input("porfavor ingrese una letra ")
##
##        vocal= "a" , "e" , "i" , "o" , "u"
##
##        if letra == vocal:
##             print("la letra ingresada es una vocal")
##        else:
##             print("la letra ingresada no es una vocal")
##        break
##    else:
##        print("fuera de porfavor introducir solo una letra")

##########5#########

##cantidad=float(input("ingrese la cantidad que desea convertir "))
##print(""" Seleccione la opcion en la que va a ingrear la cantidad:1:Metro
##                                                                2:Kilometro
##                                                                3:Centimetros
##                                                                4:Millas
##                                                                5:Yardas
##                                                                6:Pulgadas
##                                                                7:salir""")
##op=int(input("opcion deseada "))
##while op>=1 and op<=7:
##    print(""" Seleccione la opcion a la que va a convertir la cantidad:1:Metro
##                                                                2:Kilometro
##                                                                3:Centimetros
##                                                                4:Millas
##                                                                5:Yardas
##                                                                6:Pulgadas
##                                                                7:salir""")
##    op2=int(input("opcion deseada "))
##    while op2>=1 and op<=7:
##        if op==1 and op2==1:
##            print("la opcion a convertir es la misma intentelo otra vez")
##        elif op==2 and op2==2:
##            print("la opcion a convertir es la misma intentelo otra vez")
##        elif op==3 and op2==3:
##            print("la opcion a convertir es la misma intentelo otra vez")
##        elif op==4 and op2==4:
##            print("la opcion a convertir es la misma intentelo otra vez")
##        elif op==5 and op2==5:
##            print("la opcion a convertir es la misma intentelo otra vez")
##        elif op==6 and op2==6:
##            print("la opcion a convertir es la misma intentelo otra vez")
##        elif op==1 and op==2:
##            res = cantidad/1000
##            print("la cantidad de kilometros son ",res)
##        elif op==2 and op2==1:
##            res = cantidad*1000
##            print("la cantidad de metros son ",res)
##        elif op==1 and op2==3:
##            res = cantidad*100
##            print("la cantidad de centimetros son ",res)
##        elif op==3 and op2==1:
##            res = cantidad/100
##            print("la cantidad de metros son ",res)
##        elif op==1 and op2==4:
##            res = cantidad/1.609
##            print("la cantidad de millas son ",res)
##        elif op==4 and op2==1:
##            res = cantidad/1.609
##            print("la cantidad de metros son ",res)
##        elif op==1 and op2==5:
##            res = cantidad*1.094
##            print("la cantidad de yardas son ",res)
##        elif op==5 and op2==1:
##            res = cantidad/1.094
##            print("la cantidad de metros son ",res)
##        elif op==1 and op2==6:
##            res = cantidad*39.37
##            print("la cantidad de pulgadas son ",res)
##        elif op==6 and op2==1:
##            res = cantidad/39.37
##            print("la cantidad de metros son ",res)
##        elif op==2 and op2==3:
##            res = cantidad*100000
##            print("la cantidad de centimetros son son ",res)
##        elif op==3 and op2==2:
##            res = cantidad/100000
##            print("la cantidad de kilometros son ",res)
##        elif op==2 and op2==4:
##            res = cantidad/1.609
##            print("la cantidad de millas son ",res)
##        elif op==4 and op2==2:
##            res = cantidad*1.609
##            print("la cantidad de kilometros son ",res)
##        elif op==2 and op2==5:
##            res = cantidad*1094
##            print("la cantidad de yardas son ",res)
##        elif op==5 and op2==2:
##            res = cantidad/1094
##            print("la cantidad de kilometros son ",res)
##        elif op==2 and op2==6:
##            res = cantidad*39370
##            print("la cantidad de pulgadas son ",res)
##        elif op==6 and op2==2:
##            res = cantidad/39370
##            print("la cantidad de kilometros son ",res)
##        elif op==3 and op2==4:
##            res = cantidad/160900
##            print("la cantidad de millas son ",res)
##        elif op==4 and op2==3:
##            res = cantidad*160900
##            print("la cantidad de centimetros son ",res)
##        elif op==3 and op2==5:
##            res = cantidad/91.44
##            print("la cantidad de yardas son ",res)
##        elif op==5 and op2==3:
##            res = cantidad*91.44
##            print("la cantidad de centimetros son ",res)
##        elif op==3 and op2==6:
##            res = cantidad/2.54
##            print("la cantidad de pulgadas son ",res)
##        elif op==6 and op2==3:
##            res = cantidad*2.54
##            print("la cantidad de centimetros son ",res)
##        elif op==4 and op2==5:
##            res = cantidad*1760
##            print("la cantidad de yardas son ",res)
##        elif op==5 and op2==4:
##            res = cantidad/1760
##            print("la cantidad de millas son ",res)
##        elif op==4 and op2==6:
##            res = cantidad*63360
##            print("la cantidad de pulgadas son ",res)
##        elif op==6 and op2==4:
##            res = cantidad/63360
##            print("la cantidad de millas son ",res)
##        elif op==5 and op2==6:
##            res = cantidad*36
##            print("la cantidad de pulgadas son ",res)
##        elif op==6 and op2==5:
##            res = cantidad/36
##            print("la cantidad de yardas son ",res)
##        else:
##         print("Error en la opción. Inténtalo de nuevo.")
##
##         print("\nSeleccione una nueva opción o ingrese 7 para salir:")
##         op = int(input("Opción deseada: "))
##
##
##        if op == 7:
##          print("Gracias por usar el convertidor. ¡Adiós!")
##          break
##    
        
 ##########6#########
##voto = input("ingrese el candidato por el cual votar A, B, C, o Voto blanco ")
##if voto == 'A':
##    print("usted ha votado por el candidato A")
##elif voto == 'B':
##    print("usted ha votado por el candidato B")
##elif voto == 'C':
##    print("usted ha votado por el candidato C")
##elif voto == 'BLANCO':
##    print("usted ha votado en blanco")
##else:
##    print("opcion incorrecta")

##########7#########
##estudiantes=[]
##
##numero=int(input("Ingrese la cantidad de estudiantes: "))
##
##for i in range(numero):
##    nombre=input("ingrese el nombre del estudiante del estudiante ")
##    estudiantes.append(nombre)
##buscar = input("ingrese el nombre que desea buscar ")
##if buscar in estudiantes:
##    print(buscar, "está en la lista de estudiantes")
##else:
##    print(buscar, "no está en la lista de estudiantes")
# Inicializar variables

##########8#########
##negativos=0
##positivos=0
##contp=0
##for i in range(5):
##    n=int(input("Ingrese un numero "))
##    if n<0:
##        negativos+=n
##        
##    elif n>0:
##        positivos+=n
##        contp += 1
##        
##print("La sumatoria de los números negativos es ",negativos)
##
##if positivos>0:
##    
##    prom = positivos / contp
##    print("El promedio de los números positivos es ",prom)
##    
##else:
##    
##    print("No se ingresaron números positivos")

##########9#########

            
        










    
       

