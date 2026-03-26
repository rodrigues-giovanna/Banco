print("=== BANCO INTER ===")

cliente = input("Nome do Cliente: ")

saldo = 1000

while True:
    print("\nSelecione uma opção")
    print("1 - Saldo")
    print("2 - Extrato últimos 5 dias")
    print("3 - Empréstimo")
    print("4 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        print("Seu saldo é:", saldo)

    elif opcao == 2:
        print("Extrato dos últimos 5 dias:")
        print("Dia 1 - Compra 50")
        print("Dia 2 - Depósito 200")
        print("Dia 3 - Compra 30")

    elif opcao == 3:
        valor = float(input("Valor do empréstimo: "))
        saldo += valor
        print("Empréstimo aprovado!")

    elif opcao == 4:
        print("Encerrando sistema...")
        break