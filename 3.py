'''3. Implemente uma função em Python chamada cadastro() que receba um número variável de funcionários 
com seus respectivos dados (nome, idade, cargo). Além disso, implemente uma função chamada atualizar() 
que receba um dicionário com as informações de um funcionário e atualize esses dados. Utilizar os conceitos 
de gather e scatter. Requisitos:
a) A função cadastro() deve uma quantidade variável de funcionários (tuplas) e
retornar uma lista de dicionários.
b) A função atualizar() deve aceitar um dicionário que representa um
funcionário e permita atualizar suas informações.
c) Exibir a lista de funcionários cadastrados ao final.
'''

# função para cadastrar: recebe N tuplas (nome, idade, cargo) via *args (gather)
def cadastro(*funcionarios):                    # *funcionarios indica que a função pode receber um número variável de argumentos
    lista = []
    for registro in funcionarios:
        nome, idade, cargo = registro
        lista.append({"nome": nome, "idade": int(idade), "cargo": cargo})
    return lista

# atualizar: recebe o dicionário do funcionário + campos a atualizar via **kwargs (scatter)
def atualizar(funcionario, **novos_dados):      # **novos_dados indica que a função pode receber um número variável de argumentos nomeados, ou seja, um dicionário - 
    for chave, valor in novos_dados.items():
        funcionario[chave] = valor
    return funcionario


# função principal do programa (sempre chamada a partir do programa principal)
def main():
    # gather: várias tuplas passadas para cadastro(*args)
    funcionarios = cadastro(
        ("Ana", 28, "Analista"),
        ("Bruno", 35, "Gerente"),
        ("Carla", 22, "Estagiária")
    )

    # scatter: dicionário de atualizações espalhado em **kwargs
    dados_ana = {"idade": 29, "cargo": "Analista Pleno"}
    atualizar(funcionarios[0], **dados_ana)

    atualizar(funcionarios[1], cargo="Gerente Sênior")  
    atualizar(funcionarios[2], idade=23)

    # exibir lista final
    print("Funcionários cadastrados/atualizados:")
    for f in funcionarios:
        print(f)

# programa principal
if __name__ == "__main__":
    main()