# Função para determinar a prioridade no atendimento
def prioridade(paciente):
    _, idade, status = paciente
    if status.lower() == "urgente":
        return  (0, -idade) 
    elif idade >= 60:
        return (1, -idade)
    else:
        return (2, -idade)

# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# Ordene por prioridade: urgente > idosos > demais:
pacientes_ordenados = sorted(pacientes, key=prioridade)

# Extrai somente os nomes na ordem de prioridade definida
ordem_atendimento = [nome for nome, _, _ in pacientes_ordenados]

# Exiba a ordem de atendimento com título e vírgulas:
print("Ordem de Atendimento: " + ", ".join(ordem_atendimento))
