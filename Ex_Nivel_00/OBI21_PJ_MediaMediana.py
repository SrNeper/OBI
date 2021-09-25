'''
Média e Mediana - Prova Fase 2 [PJ] – OBI2021

A média de três números inteiros A, B e C é (A + B + C)=3. A mediana de
três números inteiros é o número que ficaria no meio se os três números
fossem ordenados em ordem não-decrescente.

Sua tarefa é escrever um programa que, dados dois números inteiros
distintos A e B, calcule o menor inteiro possível C tal que a média
e a mediana de A, B e C sejam iguais.

Obs. A é sempre menor do que B.
'''

#As entradas serão feitas em uma unica linha, separadas por espaço.

#Testes
#entrada = '1 2'          #0
#entrada = '6 10'         #2
#entrada = '1 1000000000' #-999999998

entrada = input()
pCorte = entrada.find(' ')

a = int(entrada[:pCorte])
b = int(entrada[pCorte:])

possibilidades = []

#C é o menor inteiro possivel.
possibilidades.append((2*a)-b) #Isso significa que ele pode ser a sub de A por B
possibilidades.append((2*b)-a) #Ou de B por A

#Média desses dois valores:
media = (a+b)//2
possibilidades.append(media)

#Organiza os valores em ordem crescente.
possibilidades.sort()

#Obtem o ménor valor.
c = possibilidades[0]

mediana = possibilidades[1]

print(c)

"""
print(f'''

A = {a} / B = {b} / C = {c}

Média   (AB)  = {media}
Mediana (ABM) = {mediana} 

Valores Ordenados:
{possibilidades}
''')

"""


