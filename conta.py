class Conta:
    def __init__(self, numero, titular, saldo, limite=1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O titular {} possui saldo de {} reais".format(
            self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite


conta = Conta(10, "Gabriela", 70)
conta2 = Conta(11, "Julia", 90, 2000)

# conta.extrato()
# conta.deposita(10)
# conta.extrato()
# conta.saca(20)
# conta.extrato()

# conta.extrato()
# conta2.extrato()

# conta.transfere(10, conta2)

# conta.extrato()
# conta2.extrato()

print(conta.saldo)
print(conta.titular)
conta.limite = 6000
print(conta.limite)
