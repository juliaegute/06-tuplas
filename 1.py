'''Implemente uma função em Python que recebe uma lista de tuplas, onde cada tupla representa as 
coordenadas (x, y) de um ponto no plano cartesiano. A função deve gerar e imprimir no terminal as 
seguintes informações:
a) O ponto mais distante da origem (0, 0).
b) O ponto mais próximo da origem (0, 0).
c) A média das distâncias dos pontos à origem.
Para calcular a distância de um ponto p de coordenas (x, y) até a origem (0, 0)
utiliza-se a expressão: distância = √(x² + y²)    -> d = sqrt(x*x + y*y)'''

from math import sqrt
from random import randint

# função para gerar a lista de pontos 
def gerar_pontos():
    lista = [] # --> litsa = list()
    for _ in range(randint(1, 5)):
        lista.append( (randint(-10, 10), randint(-10, 10)) )            # -> randint(-10, 10) gera um número aleatório entre -10 e 10
    return lista

# função para calcular a distância de cada ponto até a origem (0,0)
def calcular_distancias(lista):
    distancia = []
    for i in range(len(lista)):
        x, y = lista[i]
        distancia.append(sqrt(x*x + y*y))                     # calcula a distância e adiciona na lista de distâncias
    return distancia
        
# função para retornar o ponto mais distante da origem
def mais_distante(lista, distancia):
    ponto = lista[0]
    maior = distancia[0]
    for i in range(len(lista)):
        if distancia[i] > maior:
            maior = distancia[i]
            ponto = lista[i]
    return ponto

# função para retornar o ponto mais próximo da origem
def mais_proximo(lista, distancia):
    ponto = lista[0]
    menor = distancia[0]
    for i in range(len(lista)):                             # percorre a lista de pontos
        if distancia[i] < menor:                 # compara a distância atual com a menor distância encontrada / [i] -> acessa o elemento na posição i da lista
            menor = distancia[i]
            ponto = lista[i]
    return ponto

# função para caucular a média das distâncias
def distancia_media(lista, distancia):
    media = 0
    for d in distancia:
        media += d
    return media / len(lista)
        
# função main
def main():
    lista = gerar_pontos()
    distancia = calcular_distancias(lista)
    for i in range(len(lista)):
        print(f"Ponto: {lista[i]} - Distância até a origem: {distancia[i]:.2f}")
    
    print(f"Ponto mais distante da origem: {mais_distante(lista, distancia)}")
    print(f"Ponto mais próximo da origem: {mais_proximo(lista, distancia)}")
    print(f"Distância média até a origem: {distancia_media(lista, distancia):.2f}")
    
if __name__ == "__main__":
    main()
    