# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# Aplique o desconto se o cupom for válido
desconto = descontos.get(cupom, 0.00)
preco_final = preco * (1 - desconto)

# Saída formatada com duas casas decimais
print(f"{preco_final:.2f}")
