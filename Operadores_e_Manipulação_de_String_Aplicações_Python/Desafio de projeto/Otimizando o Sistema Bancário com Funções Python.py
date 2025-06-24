def menu():
    print("\n=== Sistema Bancário ===")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Criar Usuário")
    print("[5] Criar Conta Corrente")
    print("[6] Sair")


def formatar_valor(valor):
    return f"R$ {valor:.2f}"


def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: {formatar_valor(valor)}")
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato


def sacar(*, saldo, extrato, valor, limite, saques_realizados, limite_saques):
    if saques_realizados >= limite_saques:
        print("Limite diário de saques atingido.")
    elif valor > limite:
        print(f"O valor do saque excede o limite por saque ({formatar_valor(limite)}).")
    elif valor > saldo:
        print("Saldo insuficiente para o saque.")
    elif valor <= 0:
        print("Valor inválido para saque.")
    else:
        saldo -= valor
        extrato.append(f"Saque: {formatar_valor(valor)}")
        saques_realizados += 1
        print("Saque realizado com sucesso!")
    return saldo, extrato, saques_realizados


def exibir_extrato(saldo, extrato):
    print("\n=== Extrato ===")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:
            print(item)
    print(f"\nSaldo atual: {formatar_valor(saldo)}")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario:
        print("Usuário já cadastrado.")
        return usuarios

    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ").strip()

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso!")
    return usuarios


def criar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if not usuario:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
        return contas

    numero_conta = len(contas) + 1
    contas.append({"agencia": "0001", "numero": numero_conta, "usuario": usuario})
    print(f"Conta criada com sucesso! Agência: 0001 Número: {numero_conta}")
    return contas


def main():
    saldo = 0.0
    extrato = []
    LIMITE_SAQUE = 500.0
    MAX_SAQUES_DIARIOS = 3
    saques_realizados = 0
    usuarios = []
    contas = []

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, extrato, valor)

        elif opcao == '2':
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, saques_realizados = sacar(
                saldo=saldo,
                extrato=extrato,
                valor=valor,
                limite=LIMITE_SAQUE,
                saques_realizados=saques_realizados,
                limite_saques=MAX_SAQUES_DIARIOS
            )

        elif opcao == '3':
            exibir_extrato(saldo, extrato)

        elif opcao == '4':
            usuarios = criar_usuario(usuarios)

        elif opcao == '5':
            contas = criar_conta(contas, usuarios)

        elif opcao == '6':
            print("Obrigado por usar nosso sistema bancário. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
