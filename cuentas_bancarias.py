class Cuentas_bancarias:
    def __init__(self,tasa_interes=0.01, balance=0):
        self.tasa_interes = tasa_interes
        self.balance= balance

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if self.balance >=amount:
            self.balance -=amount
        else:
            print(f'Fondos insuficientes: cobrando una tarifa de $5')
            self.balance -= 5
        return self


    def mostrar_info_cuenta(self):
        print(f'Balance: ${self.balance}')
        return self

    def generar_interes(self):
        if self.balance >0:
            self.balance += self.balance * self.tasa_interes
        return self

cuenta_1= Cuentas_bancarias()
cuenta_2= Cuentas_bancarias()
#haz 3 depósitos y 1 retiro, luego genera intereses y muestra la información de la cuenta
cuenta_1.deposito(1000).deposito(2000).deposito(500).retiro(500).mostrar_info_cuenta()
#haz 2 depósitos y 4 retiros, luego genera intereses y muestra la información de la cuenta
cuenta_2.deposito(1000).deposito(5000).retiro(500).retiro(600).retiro(700).retiro(500).mostrar_info_cuenta()