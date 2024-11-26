#ejercicio 3 de encapsulamiento
import pandas 
class Banco():
    def __init__(self):
        self.nombre=input('ingrese su nombre y apellidos: ')
        self.direccion=input('ingrese su dirección: ')
        self.telefono=int(input('ingrese su numero telefonico: '))
        self.tipocuenta=input('ingrese tipo de cuenta: ')
        self.apertura=float(input("cuanto dinero abre la cuenta"))
        self.__dinero=self.apertura - 50000.0 #float(input('ingrese dinero de apertura cuenta: '))
        self.Menu()

    def Recibo(self):
        print(self.nombre, self.direccion, self.telefono, self.tipocuenta, self.__dinero)
        return (self.nombre, self.direccion, self.telefono, self.tipocuenta, self.__dinero)

    def Retirar(self, valor):
        if valor > self.__dinero:
            print("saldo insuficiente")
        else:
            self.__dinero-=valor
            print("Retiro exitoso")
        self.Menu()

    def Consignar(self, valor):
        self.__dinero+=valor
        print("-------Consignacion exitosa--------")

    def Menu(self):
        print("-------------Bienvendo a su banco favorito------------")
        op=input("""ingrese la accion que desea realizar 1:ver Recibo
                                                    2:Retirar
                                                    3:Consiganar
                                                    4:salir""")
        if op == "1":
            self.Recibo()
        elif op == "2":
            value = float(input("valor a retirar"))
            self.Retirar(value)
        elif op == "3":
            self.Consiganar()
        elif op == "4":
            print("------gracias por preferirnos-------")
        else:
            print("Error de ingreso")

a=Banco()


        
            
        

