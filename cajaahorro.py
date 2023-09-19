import cuenta
class CajaAhorro(cuenta.Cuenta):
    def __init__(self, numero, cliente, saldo=0):
        super().__init__(numero, cliente, saldo)
    
    
    def extraer(self, plata):
        if self.saldo >= plata:
            self.saldo -= plata
        else:
            raise cuenta.SalarioInsuficiente(self.saldo, "No hay fondos")
    