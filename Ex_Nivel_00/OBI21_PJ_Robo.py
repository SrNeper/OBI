'''
Robo - Prova Fase 2 [PJ] – OBI2021

Um Fazendeiro adquiriu um robo-espantalho que percorre um circuito sequencial, com
estações marcadas de 1~N. A cada estação o robo recebe um comando que o faz se movimentar
para a proxima estação (1) ou para a anterior (-1).

Porém, o fazendeiro percebeu que ele não está funcionando corretamente, pois uma area
da sua plantação foi atacada pelas aves e por isso ele quer saber quantas vezes o robo
esteve em uma determina estação.

Obs. O robo sempre inicia o circuito na estação 1.

Entrada:
1º Linha: N, C e S (nº inteiros)
Onnde:    N de estações         [2<=N>=100]
          C nº comandos         [1<=C>=1000]
          S estação desejada.   [S<=N]

2º Linha: Comandos -> -1 ou 1

Saida:
  nº de vezes em que o robo esteve na estação informada (S)

Exemplos:

A)                      B)                    C)                    D)
----------------------- --------------------- --------------------- ---------------------
  1º 8 8 3            | 1º 5 4 1            | 1º 2 1 1            | 1º 2 2 1            |
  2º 1 -1 1 1 1 -1 1 1| 2º 1 1 1 1          | 2º 1                | 2º -1 -1            |
  S  -> 2             | S  -> 1             | S  -> 1             | S  -> 2             |
----------------------- --------------------- --------------------- ---------------------

'''
#Recebe as primerias variaveis.
entrada = input()

#Testes
#entrada = '8 8 3'

#Nº de Estações
n = int(entrada[0])

#Quantidade de Comandos
qtComandos = int(entrada[2])

#Estação Monitorada
estacao = int(entrada[4])

#Recebe a lista de Comandos.
entrada = input()

#Testes
#entrada = '1 -1 1 1 1 -1 1 1'

#Transforma todos os numeros em uma lista.
listaComandos = []

#Split recorta a string de acordo com o parametro passado.
#Então 'num' corresponde aos numeros entre cada intervalo.
for num in entrada.split(' '):
  listaComandos.append(int(num))

#Range retorna uma seleção de numeros, iniciada em 1 e terminada em N+1

#Se o nº de estações for maior do que 1:
circuito = list(range(1,n+1))

#Posição do Robo
posRobo = 0
visitas = 0

print()

#Se a estacao averigada por a primeira.
if estacao == 1:
  #Conta o inicio do percurso como se fosse uma visita.
  visitas +=1

#Agora percorre a lista de Comandos.
for c in listaComandos:

  if circuito[posRobo] == estacao:
    print(f'\nEstou na {circuito[posRobo]}º Estação 🎯\n')

  if c == 1:
    #A posição do Robo avança em uma estação.
    posRobo += 1
    print(f'Vou para {circuito[posRobo]}º Estação')

    #Se o robô estiver dentro da estação averigada.
    if circuito[posRobo] == estacao:
      visitas += 1
  
  else: 
    #A posição do Robo regride em uma estação.
    posRobo -= 1
    print(f'Vou para {circuito[posRobo]}º Estação')

    #Essa verificação precisa ser feita 2x
    if circuito[posRobo] == estacao:
      visitas += 1


print(f'\nVisitei a {estacao}º Estacação: {visitas}x')