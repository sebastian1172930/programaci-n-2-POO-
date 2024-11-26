############ejercisios aplicaciones####################
##datos = [
##    ("Ángela", "Vargas", "1192743646", "Carrera 10A #30-24", "3046584196"),
##    ("Sebastian", "Bonilla", "1058352450", "Calle 5 #10-58", "3238001573"),
##    ("Sofia", "Cabezas", "11111111", "Carrera 789, Velez", "3006986566")
##]
##def bdatos(base):
##    print(f"{'Nombre':<10} {'Apellido':<10} {'Documento':<12} {'Dirección':<30} {'Teléfono':<12}")
##    print("="*75)
##    for persona in base:
##        nombre, apellido, documento, direccion, telefono = persona
##        print(f"{nombre:<10} {apellido:<10} {documento:<12} {direccion:<30} {telefono:<12}")
##
##bdatos(datos)
###########2##########
##meses = ("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","nomviembre","diciembre")
##
##def mes():
##    while True:
##        number = int(input("ingrese un numero entre 1 y 12 o ingrese el 0 para salir del programa"))
##        if number>=1 and number<=12:
##            print("el mes correspondiente es :",{meses[number-1]})
##        elif number==0:
##            print("fin del programa")
##            break
##        else:
##            print("dato ingresado erroneo")
##
##mes()
###########3##########
##datos = [
##    ["1", "Ángela", "Vargas", "1192743646", "Carrera 10A #30-24", "3046584196"],
##    ["2", "Sebastian", "Bonilla", "1058352450", "Calle 5 #10-58", "3238001573"],
##    ["3", "Sofia", "Cabezas", "11111111", "Carrera 789, Velez", "3006986566"]
##]
##def bdatos(base):
##    print(f"{'ID':<5} {'Nombre':<10} {'Apellido':<10} {'Documento':<12} {'Dirección':<30} {'Teléfono':<12}")
##    print("="*85)
##    for persona in base:
##        id_persona, nombre, apellido, documento, direccion, telefono = persona
##        print(f"{id_persona:<5} {nombre:<10} {apellido:<10} {documento:<12} {direccion:<30} {telefono:<12}")
##bdatos(datos)
##
##def menu():
##    id_seleccion = input("Ingrese el ID de la persona que desea editar: ")
##    persona_encontrada = None
##    for persona in datos:
##        if persona[0] == id_seleccion:
##            persona_encontrada = persona
##            break
##    
##    if not persona_encontrada:
##        print("ID no encontrado.")
##        return
##    
##    seleccion = int(input("""Ingrese la opción de la acción que desea realizar:  
##    1: Editar nombre
##    2: Editar apellido
##    3: Editar número de identidad
##    4: Editar dirección
##    5: Editar número de teléfono
##    """))
##
##    if seleccion == 1:
##        nuevnombre = input("Ingrese el nuevo nombre: ")
##        persona_encontrada[1] = nuevnombre
##        print("Nombre actualizado.")
##    elif seleccion == 2:
##        nuevapellido = input("Ingrese el nuevo apellido: ")
##        persona_encontrada[2] = nuevapellido
##        print("Apellido actualizado.")
##    elif seleccion == 3:
##        nuevnum = input("Ingrese el nuevo número de identidad: ")
##        persona_encontrada[3] = nuevnum
##        print("Número de identidad actualizado.")
##    elif seleccion == 4:
##        nuevadi = input("Ingrese la nueva dirección: ")
##        persona_encontrada[4] = nuevadi
##        print("Dirección actualizada.")
##    elif seleccion == 5:
##        nuevtel = input("Ingrese el nuevo número de teléfono: ")
##        persona_encontrada[5] = nuevtel
##        print("Número de teléfono actualizado.")
##    else:
##        print("Opción no válida.")
##    bdatos(datos)
##menu()














    
