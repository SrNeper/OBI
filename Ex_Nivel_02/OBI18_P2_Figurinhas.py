'''
Em ano de Copa do Mundo de Futebol, o álbum de figurinhas oficial é sempre um grande sucesso entre crianças e também entre adultos. Para quem não conhece, o álbum contém espaços numerados de 1 a N para colar as figurinhas; cada figurinha, também numerada de 1 a N, é uma pequena foto de um jogador de uma das seleções que jogarão a Copa do Mundo. O objetivo é colar todas as figurinhas nos respectivos espaços no álbum, de modo a completar o álbum (ou seja, não deixar nenhum espaço sem a correspondente figurinha). 

Algumas figurinhas são carimbadas (efetivamente têm um carimbo impresso sobre a fotografia do jogador) e são mais raras, mais difíceis de conseguir.

As figurinhas são vendidas em envelopes fechados, de forma que o comprador não sabe quais figurinhas está comprando, e pode ocorrer de comprar uma figurinha que ele já tenha colado no álbum. Para ajudar os usuários, a empresa responsável pela venda do álbum e das figurinhas quer criar um aplicativo que permite gerenciar facilmente as figurinhas que faltam para completar o álbum. 
Dados o número total de espaços e figurinhas do álbum (N), a lista das figurinhas carimbadas e uma lista das figurinhas já compradas (que pode conter figurinhas repetidas), sua tarefa é determinar quantas figurinhas carimbadas faltam para completar o álbum. 

Entrada 
A primeira linha contém três números inteiros N, C e M indicando respectivamente o número de figurinhas (e espaços) do álbum, o número de figurinhas carimbadas do álbum e o número de figurinhas já compradas. A segunda linha contém C números inteiros distintos indicando as figurinhas carimbadas do álbum. A terceira linha contém M números inteiros indicando as figurinhas já compradas. 

Saída 
Seu programa deve produzir um inteiro representando o número de figurinhas carimbadas que falta para completar o álbum. 

Exemplo 1:
  Entrada 
  10 2 5 
  4 7 
  7 1 2 8 3
  Saída 
  1

Exemplo 2:
  Entrada 
  10 2 6 
  4 7 
  7 1 8 4 9 3
  Saída
  0

Exemplo 3:
  Entrada
  8 4 10 
  2 4 6 8 
  3 1 1 5 9 1 7 7 1 1
  Saída
  4


'''

# album de figurinhas

n,c,m = [int(i) for i in input().split()]

# usando um conjunto para as figurinhas carimbadas jรก compradas
album = set()
carimbadas = [int(i) for i in input().split()]
compradas = [int(i) for i in input().split()]

for x in compradas:
    if (x in carimbadas):
        album.add(x)

# escreve a resposta
print(len(carimbadas) - len(album))