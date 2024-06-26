import textwrap

def menu():
    menu = """\n
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuario
    [q]\tSair
    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor          
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n==== Desposito realizado com sucesso! ====")
    else:
       print("\n==== Operação falhou! O valor informado é invalido. ====")

    return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numero_saques, limites_saques):
    excedeu_saldo = valor > saldo       
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limites_saques

    if excedeu_saldo:
        print("\nOperação Falhou, Saldo insuficiente")
    
    elif excedeu_limite:
        print("\nOperação falhou, o valor do saque excede o limite")

    elif excedeu_saques:
        print("\nOperação falhou, Numero maximo de saques excedido")
    
    elif valor > 0: 
        saldo -= valor  
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        
    else:
        print("Operação falhou, o valor informado é invalido")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato,):
    print("\nExtrato")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
 
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuario com esse CPF!")
        return
    
    nome = input("Informe o noem completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa)")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado)")

    usuario.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF dos usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuario não encontrado, fluxo de criação de conta encerrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print("textwrap.dedent(linha)")

def main():
    LIMITE_SAQUES = 3       
    AGENCIA = "0001"

    saldo = 0   
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()   

        if opcao == "d":
        
            valor = float(input("Informe o valor do deposito: "))
        
            saldo, extrato = depositar(saldo, valor, extrato)


        elif opcao == "s":  
            valor = float(input("Informe o valor do saque: "))  

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limites_saques=LIMITE_SAQUES,
        )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
    
        elif opcao == "lc":
            listar_contas(contas)
    
        elif opcao == "q":
            break       
    
        else:
            print("Operação Invalida, por favor selecione novamente a operação desejada.")

main()
