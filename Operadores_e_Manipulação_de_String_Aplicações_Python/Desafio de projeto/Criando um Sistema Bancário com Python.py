def menu():
    print("\n=== Sistema Bancário ===")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Sair")


def formatar_valor(valor):
    return f"R$ {valor:.2f}"


def main():
    saldo = 0.0
    extrato = []
    LIMITE_SAQUE = 500.0
    MAX_SAQUES_DIARIOS = 3
    saques_realizados = 0

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: {formatar_valor(valor)}")
                print("Depósito realizado com sucesso!")
            else:
                print("Valor inválido para depósito.")

        elif opcao == '2':
            if saques_realizados >= MAX_SAQUES_DIARIOS:
                print("Limite diário de saques atingido.")
                continue

            valor = float(input("Informe o valor do saque: "))

            if valor > LIMITE_SAQUE:
                print(f"O valor do saque excede o limite por saque ({formatar_valor(LIMITE_SAQUE)}).")
            elif valor > saldo:
                print("Saldo insuficiente para o saque.")
            elif valor <= 0:
                print("Valor inválido para saque.")
            else:
                saldo -= valor
                extrato.append(f"Saque: {formatar_valor(valor)}")
                saques_realizados += 1
                print("Saque realizado com sucesso!")

        elif opcao == '3':
            print("\n=== Extrato ===")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                for item in extrato:
                    print(item)
            print(f"\nSaldo atual: {formatar_valor(saldo)}")

        elif opcao == '4':
            print("Obrigado por usar nosso sistema bancário. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
