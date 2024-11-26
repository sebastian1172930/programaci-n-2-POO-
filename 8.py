segundos = int(input("Ingrese una cantidad de segundos "))
minutos = segundos/60
horas = minutos/60
segundo2 = (segundos%3600)%60
print("la cantidad de minutos son ",minutos)
print("la cantidad de horas son ",horas)
print("la cantidad de segundos son ",segundo2)
