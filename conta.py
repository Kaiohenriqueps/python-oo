class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_saque):
        return valor_saque <= (self.__saldo + self.__limite)

    def saque(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite!")

    def extrato(self):
        print(f"Saldo: {self.__saldo}")

    def transfere(self, conta_recebedora, valor):
        self.saque(valor)
        conta_recebedora.deposita(valor)

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
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @staticmethod
    def cod_banco():
        return "001"

    @staticmethod
    def cods_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
