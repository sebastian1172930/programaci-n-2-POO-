import time as sb_time
SB_PRECIO_MOTO = 500
SB_PRECIO_CARRO = 1000 
sb_vehiculos = []
sb_total_motos = 0
sb_total_carros = 0
sb_total_dinero = 0

def sb_registrar_vehiculo():
    global sb_total_motos, sb_total_carros
    sb_tipo = input("Ingrese el tipo de vehículo (moto/carro): ").lower()

    if sb_tipo not in ["moto", "carro"]:
        print("Tipo de vehículo no válido.")
        return

    sb_placa = input("Ingrese la placa del vehículo: ").upper()
    sb_hora_entrada = input("Ingrese la hora de entrada (HH:MM, formato 24 horas): ")

    sb_vehiculo = {
        "tipo": sb_tipo,
        "placa": sb_placa,
        "hora_entrada": sb_hora_entrada,
        "hora_salida": None,
        "duracion": None,
        "precio": None
    }
    sb_vehiculos.append(sb_vehiculo)
    if sb_tipo == "moto":
        sb_total_motos += 1
    else:
        sb_total_carros += 1
    print(f"Vehículo {sb_tipo.upper()} con placa {sb_placa} registrado a las {sb_hora_entrada}.\n")

def sb_calcular_duracion(sb_hora_entrada, sb_hora_salida):
    sb_formato = "%H:%M"
    sb_entrada = sb_time.strptime(sb_hora_entrada, sb_formato)
    sb_salida = sb_time.strptime(sb_hora_salida, sb_formato)
    sb_entrada_minutos = sb_entrada.tm_hour * 60 + sb_entrada.tm_min
    sb_salida_minutos = sb_salida.tm_hour * 60 + sb_salida.tm_min
    sb_duracion = sb_salida_minutos - sb_entrada_minutos
    if sb_duracion < 0:
        sb_duracion += 24 * 60
    return sb_duracion

def sb_calcular_precio(sb_duracion, sb_tipo):
    sb_fracciones = (sb_duracion + 14) // 15
    if sb_tipo == "moto":
        return sb_fracciones * SB_PRECIO_MOTO
    else:
        return sb_fracciones * SB_PRECIO_CARRO

def sb_registrar_salida():
    global sb_total_dinero
    sb_placa = input("Ingrese la placa del vehículo que está saliendo: ").upper()
    sb_vehiculo = next((v for v in sb_vehiculos if v["placa"] == sb_placa and v["hora_salida"] is None), None)
    if sb_vehiculo is None:
        print("Vehículo no encontrado o ya ha sido retirado.\n")
        return
    sb_hora_salida = input("Ingrese la hora de salida (HH:MM, formato 24 horas): ")
    sb_duracion = sb_calcular_duracion(sb_vehiculo["hora_entrada"], sb_hora_salida)
    sb_precio = sb_calcular_precio(sb_duracion, sb_vehiculo["tipo"])
    sb_vehiculo["hora_salida"] = sb_hora_salida
    sb_vehiculo["duracion"] = sb_duracion
    sb_vehiculo["precio"] = sb_precio
    sb_total_dinero += sb_precio
    print(f"Duración del parqueo: {sb_duracion} minutos")
    print(f"Precio a cobrar: ${sb_precio}\n")

def sb_mostrar_resumen():
    print("\n--- Resumen del día ---")
    print(f"Total de motos ingresadas: {sb_total_motos}")
    print(f"Total de carros ingresados: {sb_total_carros}")
    print(f"Total de dinero recaudado: ${sb_total_dinero}")
    print("-----------------------\n")

def sb_menu():
    while True:
        print("1. Registrar vehículo")
        print("2. Registrar salida de vehículo")
        print("3. Mostrar resumen del día")
        print("4. Salir")
        sb_opcion = input("Seleccione una opción: ")
        if sb_opcion == "1":
            sb_registrar_vehiculo()
        elif sb_opcion == "2":
            sb_registrar_salida()
        elif sb_opcion == "3":
            sb_mostrar_resumen()
        elif sb_opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.\n")

sb_menu()
