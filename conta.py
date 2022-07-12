class Conta:
    def __init__(self, numero, titular, saldo, limite=1000):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O titular {} possui saldo de {} reais".format(self.titular,self.saldo))

    def deposita(self,valor):
        self.saldo+=valor

    def saca(self,valor):
        self.saldo-=valor

conta = Conta(10, "Gabriela", 70)
conta2 = Conta(11, "Julia", 90, 2000)

print(conta.saldo)

conta.extrato()
conta.deposita(10)
conta.extrato()
conta.saca(20)
conta.extrato()


