# Cria uma lista vazia para armazenar os equipamentos
equipamentos = []

# Loop para solicitar ao usuário inserir até três equipamentos
for i in range(3):
    # Solicita ao usuário que insira as informações do equipamento
    nome = input("Insira o nome do equipamento: ")
    tipo = input("Insira o tipo do equipamento: ")
    numero_serie = input("Insira o número de série do equipamento: ")
    
    # Cria um dicionário para armazenar as informações do equipamento
    equipamento = {
        "Nome": nome,
        "Tipo": tipo,
        "Número de Série": numero_serie
    }
    
    # Adiciona o equipamento à lista de equipamentos
    equipamentos.append(equipamento)

# Exibe a lista de equipamentos
print("\nLista de Equipamentos:")
for equipamento in equipamentos:
    print("Nome:", equipamento["Nome"])
    print("Tipo:", equipamento["Tipo"])
    print("Número de Série:", equipamento["Número de Série"])
    print()  # Adiciona uma linha em branco para separar os equipamentos
