# Clase
class Usuario:
    # Constructor
    def __init__(self, nombre, balance):
        # Atributos
        self.nombre = nombre
        self.balance = balance

    # métodos
    def hacer_deposito(self, monto):
        self.balance += monto

    def hacer_retiro(self, monto):
        self.balance -= monto

    def mostrar_balance(self):
        print(f"Usuario: {self.nombre}, Balance: {self.balance}")

    def transferencia(self,otro_usuario,monto):
        self.hacer_retiro(monto)
        otro_usuario.hacer_deposito(monto)
    # instancias

guido = Usuario("Guido van Rossum", 2000)
guido.hacer_deposito(500)
guido.hacer_retiro(800)

guido.mostrar_balance()





