'''
Zero - - Prova Fase 1 [P1] – OBI2021

Seu chefe está ao telefone, nervoso. Ele quer que você
compute a soma de uma sequência de números que ele vai
falar para você ao telefone, para saber o total das
vendas em sua mais recente viagem de negócios.

Infelizmente, de vez em quando seu chefe fala números
errados para você ao telefone. Felizmente, seu chefe
rapidamente percebe que falou um número errado e diz
“zero”, que como combinado previamente quer dizer ignore
o último número corrente. Infelizmente, seu chefe pode
cometer erros repetidos, e diz “zero” para cada erro.

Por exemplo, seu chefe pode falar ao telefone:

“Um, três, cinco, quatro, zero, zero, sete, zero, zero,
seis”, o que signiﬁca uma soma total igual a 7, conforme
explicado na tabela abaixo:

Fala do chefe             -- Números correntes  -- Explicação
“um, três, cinco, quatro” |      1,3,5,4        | registre os quatro números
“zero, zero”              |      1,3            | ignore os dois últimos números
“sete”                    |      1, 3, 7        | registre o sete ao ﬁnal da lista
“zero, zero”              |      1              | ignore os dois últimos números
“seis”                    |      1, 6           | registre seis ao ﬁnal da lista

Para não deixar seu chefe ainda mais nervoso, escreva um
programa que determine a soma total dos números falados
por seu chefe ao telefone.

Exemplo 01:
Entrada: 4 - 3 - 0 - 4 - 0
Saida: 0


Exemplo 02:
Entrada: 10 - 1 - 3 - 5 - 4 - 0 - 0 - 7 - 0 - 0 - 6
Saida: 7

'''

qtNumeros = int(input())

nAnotados = []

for i in range(qtNumeros):

  n = int(input())

  if n != 0:
    #add um n na lista
    #print('Add:', n)
    nAnotados.append(n)
  else:
    #remove o ultimo n da lista
    #print('Remove:', nAnotados[-1])
    nAnotados.pop()

print(sum(nAnotados))
#print(nAnotados)
