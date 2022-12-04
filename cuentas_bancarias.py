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


class Usuario:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.cuenta= Cuentas_bancarias(tasa_interes=0.02,balance=0)

    def hacer_deposito(self):
        self.cuenta.deposito
        return self
    
    def hacer_retiro(self):
        self.cuenta.retiro
        return self

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name} , {self.cuenta.mostrar_info_cuenta}")
        return self

    def transferencia(self,amount,usuario):
        self.balace_cuenta -= amount
        usuario.balance_cuenta += amount
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()


cuenta_1= Cuentas_bancarias()
cuenta_2= Cuentas_bancarias()
#haz 3 depósitos y 1 retiro, luego genera intereses y muestra la información de la cuenta
cuenta_1.deposito(1000).deposito(2000).deposito(500).retiro(500).mostrar_info_cuenta()
#haz 2 depósitos y 4 retiros, luego genera intereses y muestra la información de la cuenta
cuenta_2.deposito(1000).deposito(5000).retiro(500).retiro(600).retiro(700).retiro(500).mostrar_info_cuenta()


Pedro = Usuario("Pedro López", "pedro@dojo.com")
Marce = Usuario("Marcela Pascal", "marcelin@gmail.com")
Pedro.cuenta.deposito(1000).deposito(100).deposito(500).retiro(2000).mostrar_info_cuenta()
Marce.cuenta.deposito(1000).deposito(5000).retiro(500).retiro(600).retiro(700).retiro(500).mostrar_info_cuenta()

