#!/usr/bin/python3
import cuenta
import cajaahorro
import cuentacorriente

def mostrarListado(cuentas):
    for c in cuentas:
        print(c)

def main():
    ca1 = cajaahorro.CajaAhorro(1,"Jose")
    ca2 = cajaahorro.CajaAhorro(2,"Ro")
    cc1 = cuentacorriente.CuentaCorriente(3,"Abel", -500)
    cc2 = cuentacorriente.CuentaCorriente(4,"Pepe", -500)
    cuentas = [ca1, ca2, cc1, cc2]
    try:
        ca1.depositar(400)
        print(ca1)

    except cuenta.SalarioInsuficiente:
        print("No hay dinero disponible")
    else:
        print("Sin problemas")
    try:
        ca1.extraer(200)
        print(ca1)
        ca1.extraer(300)
        print(ca1)

    except cuenta.SalarioInsuficiente:
        print("No hay dinero disponible")
    else:
        print("Sin problemas")
    try:
        cc1.depositar(300)
        print(cc1)
        cc1.extraer(700)
        print(cc1)

    except cuenta.SalarioInsuficiente:
        print("No hay dinero disponible")
    else:
        print("Sin problemas")
    try:

        cc1.extraer(200)
        print(cc1)

    except cuenta.SalarioInsuficiente:
        print("No hay dinero disponible")
    else:
        print("Sin problemas")
    print("-----------")
    mostrarListado(cuentas)

if __name__ == "__main__":
    main()
    


