def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Numero da conta {}".format(conta["numero"]))
    print("Titular {}".format(conta["titular"]))
    print("Saldo {}".format(conta["saldo"]))

    
