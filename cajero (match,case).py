cajero=input("ingrese una de las opciones: Retiro, Consulta, Tra, Resibos ")
match cajero:
    case "Retiro":
        plata=int(input("cuanto va a retirar "))
        print("retiro exitoso")
    case"Consulta":
        print("su saldo es: $150.000.000.000")
    case"tra":
        print("Transeferencia exitosa")
    case"Resibos":
        print("aguea,luz,celular,internet")
