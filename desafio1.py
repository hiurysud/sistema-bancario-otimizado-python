# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo):
  
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 

  if consumo <= 10:
    return "Plano Essencial Fibra - 50Mbps"
    
  elif consumo > 11 and consumo <= 20:
    return "Plano Prata Fibra - 100Mbps"
  
  else:
    return "Plano Premium Fibra - 300Mbps"
    
#TODO: Retorne o plano de internet adequado:



# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Insira o consumo médio mensal de dados: "))

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
plano_recomendado = recomendar_plano(consumo)
print("O plano recomendado para o seu consumo é:",plano_recomendado)