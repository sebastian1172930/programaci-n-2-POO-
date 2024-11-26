def calcular_serie(resistencias):
    return sum(resistencias)

def calcular_paralelo(resistencias):
    return 1 / sum([1/r for r in resistencias])

def main():
    while True:
        # Solicitar tipo de circuito
        tipo = input("Seleccione el tipo de circuito (serie/paralelo): ").strip().lower()
        
        # Solicitar cantidad de resistencias
        N = int(input("Ingrese la cantidad de resistencias (mínimo 2): "))
        if N < 2:
            print("Debe ingresar al menos 2 resistencias.")
            continue
        
        # Solicitar los valores de las resistencias
        resistencias = []
        for i in range(N):
            r = float(input(f"Ingrese el valor de la resistencia R{i+1} en ohmios: "))
            resistencias.append(r)
        
        # Solicitar el valor de la fuente de voltaje
        voltaje = float(input("Ingrese el valor de la fuente de voltaje en voltios: "))
        
        # Calcular la resistencia equivalente
        if tipo == "serie":
            R_eq = calcular_serie(resistencias)
        elif tipo == "paralelo":
            R_eq = calcular_paralelo(resistencias)
        else:
            print("Tipo de circuito no válido.")
            continue
        
        # Calcular corriente total (I = V / R_eq)
        corriente_total = voltaje / R_eq
        
        # Calcular potencia (P = V * I)
        potencia_total = voltaje * corriente_total
        
        # Asumir un tiempo (t) de 1 segundo para energía (E = P * t)
        tiempo = 1  # En segundos
        energia_total = potencia_total * tiempo
        
        # Mostrar resultados
        print("\nResultados:")
        print(f"Resistencia equivalente: {R_eq:.2f} ohmios")
        print(f"Corriente total: {corriente_total:.2f} amperios")
        print(f"Potencia total: {potencia_total:.2f} vatios")
        print(f"Energía consumida en {tiempo} segundo(s): {energia_total:.2f} joules")
        
        # Preguntar si desea realizar otro cálculo
        continuar = input("\n¿Desea realizar otro cálculo? (si/no): ").strip().lower()
        if continuar != "si":
            break
main()
