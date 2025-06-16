# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:
if (
    "@" in email and
    not email.startswith("@") and
    not email.endswith("@") and
    " " not in email and
    "." in email.split("@")[-1]  # Verifica se o domínio tem ponto
):
    print("E-mail válido")
else:
    print("E-mail inválido")
