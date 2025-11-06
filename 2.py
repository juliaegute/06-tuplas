''' Implemente uma função em Python para comparar as notas de alguns alunos na primeira prova e na segunda 
prova aplicada por um professor. A função deve receber como parâmetro duas listas de tuplas, onde cada
tupla contém o nome de um aluno e sua nota em uma prova. A função deve exibir os seguintes resultados:
    a) Alunos que melhoraram suas notas da primeira prova para a segunda.
    b) Alunos que pioraram suas notas.
    c) Alunos que mantiveram a mesma nota.'''

p1 = [("Selmini", 8), ("Flavio", 7), ("Rafa", 9), ("Surian", 10)]
p2 = [("Selmini", 2), ("Flavio", 7), ("Rafa", 10), ("Surian", 10)]

melhor = []
pior = []
manteve = []

for i in range(len(p1)):                            # percorre as listas de tuplas 
    aluno, nota1 = p1[i]                            # desempacota a tupla da primeira prova
    aluno, nota2 = p2[i]
    delta = nota2 - nota1                           # calcula a diferença entre as notas
    aux = (aluno, nota1, nota2, delta)              # cria uma tupla auxiliar com nome, nota1, nota2 e delta
    if nota2 > nota1:                               # compara as notas
        melhor.append(aux)                          # adiciona a tupla na lista de melhoraram - append -> adicionar elemento na lista
    elif nota2 < nota1:
        pior.append(aux)
    else:
        manteve.append(aux)                         # adiciona a tupla na lista de mantiveram (aux) -> variável auxiliar que serve para guardar temporariamente um valor

print(f"alunos que melhoraram: {melhor}")
print(f"alunos que mantiveram: {manteve}")
print(f"alunos que pioraram: {pior}")
