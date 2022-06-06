class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

# Getters and Setters
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero 
    
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
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

# Metodos da Classe
    def extrato(self):
        print(f"Titular: {self.titular} Saldo: {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if (self.__testa_limite(valor)):
            self.saldo -= valor
        else:
            print(f"O valor {valor} passou do limite")

    def __testa_limite(self, valor):
        valor_disponivel = self.saldo + self.limite
        return valor <= valor_disponivel

    def transfere(self, destino, valor):
        origem = self
        origem.sacar(valor)
        destino.depositar(valor)
