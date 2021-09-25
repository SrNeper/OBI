'''
Duplas de Tenis - Prova Fase 2 [PJ] – OBI2021

Quatro amigos combinaram de jogar tênis em duplas. Cada um dos amigos tem um nível de jogo,
que é representado por um número inteiro:quanto maior o número, melhor o nível do jogador.

Os quatro amigos querem formar as duplas para iniciar o jogo. De forma a tornar o jogo mais
interessante, eles querem que os níveis dos dois times formados sejam o mais próximo
possível. O nível de um time é a soma dos níveis dos jogadores do time.

Embora eles sejam muito bons jogadores de tênis, os quatro amigos não são muito bons em
algumas outras coisas, como lógica ou matemática. Você pode ajudá-los e encontrar a menor
diferença possível entre os níveis dos times que podem ser formados?

Entrada:

A pontuação de cada jogador:
  Ex: A = 50 / B = 100 / C = 20 / D = 30 -> 50 100 20 30 (uma por linha)

Saída:
  Seu programa deve produzir uma única linha, contendo um único inteiro, a menor diferença entre os níveis dos dois times formados.

'''
#Testes:
#pontos = [4,7,10,20]  #-> 7
#pontos = [0,0,1,1000] #-> 999
#pontos = [1,2,3,4]    #-> 0

pontos = []

for i in range(4):
  pontos.append(int(input(f'{i+1}º Jogador - Pontuação: \t')))

#Diferença de Pontos da Dula A: 
dif_dupla_A = abs(pontos[0]-pontos[1]) #10 - 5 = 5 // 5 - 10 = -5 -> 5 

#Diferença de Pontos da Dula B: 
dif_dupla_B = abs(pontos[2]-pontos[3])

'''
time1 = nivel_dos_jogadores[0] + nivel_dos_jogadores[3]
time2 = nivel_dos_jogadores[1] + nivel_dos_jogadores[2]
print(abs(time1 - time2))

'''

#Obs. abs() retorna o valor absoluto, que é sempre positivo.
#     Por exemplo: 6-3 = 3 & 3-6 = -3 -> positivo/negativo
#     Mas com abs() esse valor é sempre positivo. Isso dispensa o uso dos ifs

#Diferença de pontos entre as duas Duplas.
dif_Duplas = abs(dif_dupla_A - dif_dupla_B) 

print(dif_Duplas)