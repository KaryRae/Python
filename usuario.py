class Usuario:

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.balance_cuenta= 0

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
    
    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name} , {self.balance_cuenta}")
        
Pedro =Usuario("Pedro López", "pedro@dojo.com")
Pedro.hacer_deposito(1000)
Pedro.hacer_deposito(2000)
Pedro.hacer_deposito(200)
Pedro.hacer_retiro(500)
Pedro.mostrar_balance_usuario()

carla = Usuario("Carla Merino", "carla@dojo.com")
carla.hacer_deposito(2000)
carla.hacer_deposito(500)
carla.hacer_retiro(100)
carla.hacer_retiro(1000)
carla.mostrar_balance_usuario()

marce = Usuario("Marce Lin", "marce@dojo.com")
marce.hacer_deposito(5000)
marce.hacer_retiro(300)
marce.hacer_retiro(1000)
marce.hacer_retiro(500)
marce.mostrar_balance_usuario()

