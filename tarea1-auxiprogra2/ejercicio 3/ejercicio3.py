class CuentaBancaria:
    def __init__(self, titular, nroCuenta, saldo):
        self.titular = titular
        self.nroCuenta = nroCuenta
        self.saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            print("Error: El monto a depositar debe ser mayor a 0.")
        else:
            self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            print("Error: Fondos insuficientes.")
        else:
            self.saldo -= monto

    def mostrar_datos(self):
        print(f"Titular: {self.titular}, Nro Cuenta: {self.nroCuenta}, Saldo: {self.saldo}")

cuenta = CuentaBancaria("Juan Perez", "12345678", 500.0)
cuenta.depositar(-50)
cuenta.retirar(600)
cuenta.depositar(200)
cuenta.retirar(150)
cuenta.mostrar_datos()
