'''
Torneio de tênis - Prova Fase 1 [PJ] – OBI2021

A prefeitura contratou um novo professor para ensinar as crianças do bairro a jogar tênis na quadra de tênis do parque municipal. O professor convidou todas
as crianças do bairro interessadas em aprender a jogar tênis. Ao ﬁnal do
primeiro mês de aulas e treinamentos foi organizado um torneio
em que cada participante disputou exatamente seis jogos. O professor vai usar o
desempenho no torneio para separar as crianças em três grupos, de forma a ter
grupos de treino em que os participantes tenham habilidades mais ou menos iguais, usando o
seguinte critério:

• participantes que venceram 5 ou 6 jogos serão colocados no Grupo 1;
• participantes que venceram 3 ou 4 jogos serão colocados no Grupo 2;
• participantes que venceram 1 ou 2 jogos serão colocados no Grupo 3;

• participantes que não venceram nenhum jogo não serão convidados a continuar 
  com os treinamentos.

Dada uma lista com o resultado dos jogos de um participante, escreva um programa para determinar
em qual grupo ele será colocado.

Entrada:
A entrada consiste de seis linhas, cada linha indicando o resultado de um jogo do participante.

Cada linha contém um único caractere: V se o participante venceu o jogo, ou P se o jogador perdeu
o jogo. Não há empates nos jogos.

Saída:
Seu programa deve produzir uma única linha na saída, contendo um único inteiro,
identiﬁcando o grupo em que o participante será colocado. Se o participante não
for colocado em nenhum dos três grupos seu programa deve imprimir o valor −1.

Exemplo 01:
Entrada: V - V - P - P - P - V
Saida: 2

Exemplo 02:
Entrada: P - P - P - P - P - P
Saida: -1

'''

#5 ou 6 -> G1
#3 ou 4 -> G2
#2 ou 1 -> G3;
#0      -> -1

#V = venceu // P = Perdeu

resultadoJogos = []

for i in range(6):
  resultadoJogos.append(str(input()))


if resultadoJogos.count('V') >=5:

  print(1)

elif resultadoJogos.count('V') >=3:

  print(2)

elif resultadoJogos.count('V') >=1:

  print(3)

else:
  print(-1)