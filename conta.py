class Conta:
    def __init__(self, numero, titular, saldo, limite=1000):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

conta = Conta(10, "Gabriela", 70)
conta2 = Conta(11, "Julia", 90, 2000)

print(conta.saldo)
