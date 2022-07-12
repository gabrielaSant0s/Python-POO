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


conta = Conta(10, "Gabriela", 70)
conta2 = Conta(11, "Julia", 90, 2000)

# conta.extrato()
# conta.deposita(10)
# conta.extrato()
# conta.saca(20)
# conta.extrato()

conta.extrato()
conta2.extrato()

conta.transfere(10, conta2)

conta.extrato()
conta2.extrato()
