class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco


class Conta:
    def __init__(self, numero, usuario):
        self.agencia = "0001"
        self.numero = numero
        self.usuario = usuario


def menu():
    print("\n=== Sistema Bancário ===")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Novo Usuário")
    print("[5] Nova Conta")
    print("[6] Listar Usuários")
    print("[7] Listar Contas")
    print("[8] Sair")


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
    usuario = next((u for u in usuarios if u.cpf == cpf), None)
    if usuario:
        print("Usuário já cadastrado.")
        return usuarios

    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ").strip()

    novo_usuario = Usuario(nome, cpf, data_nascimento, endereco)
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!")
    return usuarios


def criar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = next((u for u in usuarios if u.cpf == cpf), None)
    if not usuario:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
        return contas

    numero_conta = len(contas) + 1
    nova_conta = Conta(numero_conta, usuario)
    contas.append(nova_conta)
    print(f"Conta criada com sucesso! Agência: {nova_conta.agencia} Número: {nova_conta.numero}")
    return contas


def listar_usuarios(usuarios):
    print("\n=== Lista de Usuários ===")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"Nome: {usuario.nome}, CPF: {usuario.cpf}, Nascimento: {usuario.data_nascimento}, Endereço: {usuario.endereco}")


def listar_contas(contas):
    print("\n=== Lista de Contas ===")
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print(f"Agência: {conta.agencia}, Número: {conta.numero}, Titular: {conta.usuario.nome}, CPF: {conta.usuario.cpf}")


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
            listar_usuarios(usuarios)

        elif opcao == '7':
            listar_contas(contas)

        elif opcao == '8':
            print("Obrigado por usar nosso sistema bancário. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
