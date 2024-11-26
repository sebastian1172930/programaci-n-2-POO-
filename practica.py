class Romano_a_entero():
    def __init__(self):
        self.romano_a_entero_diccionario = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def conversion(self, romano):
        total = 0
        valor = 0

        for cabecera in reversed(romano):
            val = self.romano_a_entero_diccionario[cabecera]

            if val < valor:
                total -= val
            else:
                total += val
            valor = val

        return total


class Entero_a_romano():
    def __init__(self):
        self.entero_a_romano_lista = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

    def convertir(self, numero):
        romano = ""
        for value, symbol in self.entero_a_romano_lista:
            while numero >= value:
                romano += symbol
                numero -= value
        return romano


class Menu():
    def __init__(self):
        self.romano_a_entero_convertir = Romano_a_entero()
        self.entero_a_romano_convertir = Entero_a_romano()

    def hierbabuena(self):
        while True:
            print("\nSeleccione una opción:")
            print("1: Pasar de romano a entero")
            print("2: Pasar de entero a romano")
            print("3: Salir")
            
            try:
                opcion = int(input("Ingrese la opción que desea realizar: "))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

            if opcion == 1:
                romano = input("Por favor, ingrese el número romano que desea pasar a entero: ").upper()
                try:
                    resultado = self.romano_a_entero_convertir.conversion(romano)
                    print(f"El número romano {romano} equivale al entero {resultado}.")
                except KeyError:
                    print("El número romano ingresado no es válido. Intente de nuevo.")
            elif opcion == 2:
                try:
                    numero = int(input("Por favor, ingrese el número entero que quiera pasar a romano: "))
                    if numero <= 0:
                        print("Por favor, ingrese un número mayor a 0.")
                        continue
                    resultado = self.entero_a_romano_convertir.convertir(numero)
                    print(f"El número entero {numero} en romano es {resultado}.")
                except ValueError:
                    print("Por favor, ingrese un número entero válido.")
            elif opcion == 3:
                print("Chao cacao. ¡Hasta luego!")
                break
            else:
                print("Opción incorrecta. Intente nuevamente.")

menu = Menu()
menu.hierbabuena()











            
            
    
        
        
