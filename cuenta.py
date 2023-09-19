class Cuenta:
    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        
    def __str__(self):
        return f"Numero: {self.numero}, Cliente: {self.cliente}, Saldo: {self.saldo}" 
        
    def depositar(self, plata):
        self.saldo += plata
        
    
    def extraer(self, plata):
        self.saldo -= plata
        
    def saldo(self):
        return self.saldo

class SalarioInsuficiente(Exception):
    def __init__(self, salario, message="No hay fondos"):
        self.salario = salario
        self.message = message
        super().__init__(self.message)