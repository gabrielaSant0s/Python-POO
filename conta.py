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

    def __pode_sacar(self, valor):
        return valor <= self.saldo + self.limite

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Você não tem crédito pra sacar {} valor".format(valor))

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

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


conta = Conta(10, "Gabriela", 70)
conta2 = Conta(11, "Julia", 90, 2000)

# conta.extrato()
# conta.deposita(10)
# conta.extrato()
conta.saca(20)
# conta.extrato()

# conta.extrato()
# conta2.extrato()

# conta.transfere(10, conta2)

conta.extrato()
# conta2.extrato()

# print(conta.saldo)
# print(conta.titular)
# conta.limite = 6000
# print(conta.limite)

print(Conta.codigo_banco())
print(Conta.codigos_bancos())
