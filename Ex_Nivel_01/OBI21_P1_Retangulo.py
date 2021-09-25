'''
Retangulo - Prova Fase 2 [P1] – OBI2021

Vô Pedro, é muito organizado e recentemente ele fez uma plantação no centro de um
circulo de 8 arvores, anteriormente plantadas por ele. Agora ele quer passar uma corda
entre as arvores, afim de demarcar os retangulos e quadrados que poderão ser formados
dentro dessa area.

Por exemplo:
Entre as arvores, existe um arco que compõem o circulo, logo 8 arvores, 8 arcos.
Imagine que o tamanho de cada um deles é: 2, 2, 2, 6, 2, 4, 3 e 3

Um retangulo possui 2 lados iguais e um quadrado possui 4 lados iguais.
Com base nos arcos informados, temos:

  1 Retangulo:
  2 & 2                  -> 2 lados de um retangulo.
  4/3/3 (10) & 2/2/6 (10)-> são os outros 2 lados desse retangulo.

  1 Quadrado:
  2/2/2 & 4/2 (6)        -> 2 lados de um quadrado.
  6 & 3/3 (6)            -> são os outros 2 lados desse quadrado.


Entrada:
1º Linha -> Nº de Arvores   [4<=N<=10^5]
2º Linha -> Valor dos Arcos [sentido anti-Horario]
'''

#Pegamos a quantidade de arvores.
qtArvores = int(input('\nNº de Arvores: \t'))
print()

arcos = []

#Depois o tamanho de cada Arco.
for a in range(qtArvores):
  arcos.append(int(input(f'{a+1}º Arco: \t')))

#Descobrimos qual é o maior Arco.
maiorArco = max(arcos)

#E para dividir esse circulo em 2 partes e descobrir se é possivel formar um retangulo/quadrado
arcosImpares = [] #Criamos uma lista para os arcos Impares
arcosPares   = [] #E uma para os Pares.

#Separamos esses valores  
for a in arcos:
  if a%2 != 0:
    arcosImpares.append(a)
  else:
    arcosPares.append(a) 

metadeImpar = sum(arcosImpares) #Uma metade é a soma de todos os impares
metadePar   = sum(arcosPares)   #A outra é a soma dos pares.

#Se a soma de ao menos uma dessas metades não for Zero e a quantidade de arvores for Par.
if metadeImpar > 0 or metadePar > 0 and qtArvores%2 == 0:
  
  #Verificamos se as metades são diferentes e possuem valores acima de Zero.
  if metadeImpar != metadePar and metadeImpar > 0 and metadePar > 0: 
    
    #Com isso temos um retangulo.
    print('\nS -> Retangulo')

  #Se uma dessas metades for igual a Zero:
  #Verificamos se a circuferencia é divisivel pelo maior dos arcos
  #E se uma dessas metades é divisivel por 4.
  elif sum(arcos)%maiorArco == 0 and metadeImpar%4 == 0 or metadePar%4 == 0:
    
    #Se isso for verdade, temos um Quadrado.
    print('\nS -> Quadrado')
  
  #Mas se nada disso for verdade ou se a quantidade de arvores for impar.
  else:
    print('\nN')    

else:

  #Não conseguiremos formar um quadrado ou um retangulo.
  print('\nN')
