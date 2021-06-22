'''
  A turma do colégio vai fazer uma excursão na serra e
  todos os alunos e monitores vão tomar um bondinho para
  subir até o pico de uma montanha. A cabine do bondinho
  pode levar 50 pessoas no máximo, contando alunos e
  monitores, durante uma viagem até o pico. Neste problema
  dado como entrada o número de alunos A e o número de
  monitores M, você deve escrever um programa que diga se
  é possível ou não levar todos os alunos e monitores em
  apenas uma viagem!

Entrada:

  A primeira linha da entrada contém um inteiro A,
  representando a quantidade de alunos. A segunda linha da
  entrada contém um inteiro M, representando o número de
  monitores.

Saída:
  Seu programa deve imprimir uma linha contendo o
  caractere S se é possível levar todos os alunos e
  monitores em apenas uma viagem, ou o caractere N caso
  não seja possível.

Restrições:
  a) 1 ≤ A ≤ 50
  b) 1 ≤ M ≤ 50

Exemplos:
  | = pula uma linha.
  , = colocados lado a lado.

01>
  Entrada = 10|20
  Saída   = S

02>
  Entrada = 12|39
  Saída   = N

03>
  Entrada = 49|1
  Saída   = S

'''
#Iniciando as Variaveis:
#Dimensões da Caixa -> Altura, Largura e Comprimento.
#OBS. NÃO NECESSARIAMENTE NESSA ORDEM. /\
A = 0 
B = 0 
C = 0 

H = 0 #Altura da Janela
L = 0 #Largura da Janela.

#Validando e Pegando as Dimensões.
while not 1<= A <=100:
  A= int(input("digite o valor de A:\t"))

while not 1<= B <=100:
  B= int(input("digite o valor de B:\t"))

while not 1<= C <=100:
  C= int(input("digite o valor de C:\t"))

while not 1<= H <=100:
  H= int(input("digite o valor de H:\t"))

while not 1<= L <=100:
  L= int(input("digite o valor de L:\t"))

resposta = "N"

if ( A <= H and B <= L  ): resposta = "S"
if ( A <= L and B <= H  ): resposta = "S"
if ( A <= H and C <= L  ): resposta = "S"
if ( A <= L and C <= H  ): resposta = "S"
if ( B <= H and C <= L  ): resposta = "S"
if ( B <= L and C <= H  ): resposta = "S"

print(resposta)

#SE QUISER TESTAR A EFICIÊNCIA DESSE CÓDIGO ACESSE:
#https://olimpiada.ic.unicamp.br/pratique/pj/2017/f1/drone/
#obs. mas antes remova o texto dos inputs.