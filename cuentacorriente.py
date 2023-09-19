import cuenta

class CuentaCorriente(cuenta.Cuenta):
    def __init__(self, numero, cliente, acuerdo, saldo=0):
        super().__init__(numero, cliente, saldo)
        self.acuerdo = acuerdo
    
    def __str__(self):
        return f"{super().__str__()}, Acuerdo: {self.acuerdo}"
    
    def extraer(self, plata):
        if self.acuerdo <= (self.saldo - plata):
            self.saldo -= plata
        else:
            raise cuenta.SalarioInsuficiente(self.saldo, "No hay mas dinero disponible")