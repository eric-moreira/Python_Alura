from conta import Conta

conta = Conta(123, "Nico", 2000.00, 1000.00)
conta.depositar(3000)
conta.extrato()
conta.sacar(150)
conta.extrato()

