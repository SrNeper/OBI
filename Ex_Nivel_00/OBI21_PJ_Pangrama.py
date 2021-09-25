'''
Pangrama - Prova Fase 2 [PJ] – OBI2021

Um pangrama é uma frase que contém todas as letras de um determinado
alfabeto.

Em português, um pangrama pode incluir também letras acentuadas, mas
neste problema vamos desconsiderar os acentos (mesmo que isso torne a
frase mal escrita!)

Veja alguns exemplos de pangramas em português (sem acentos):

  • grave e cabisbaixo, o filho justo zelava pela querida mae doente
  
  • hoje a noite, sem luz, decidi xeretar a quinta gaveta de vovo: achei linguica, pao e fuba

  • marta foi a cozinha pois queria ver belo jogo de xicaras

Note que para os pangramas acima consideramos o alfabeto composto pelas letras

          'a b c d e f g h i j l m n o p q r s t u v x z'

(ou seja, não consideramos as letras k, w ou y). Note ainda que as
frases não contêm letras acentuadas mas podem conter símbolos gráficos
como espaço em branco, vírgula e dois pontos.

Entrada:
Uma frase com até 200 caracteres.

Saida:
S -> Se ela for um pangrama.
N -> Se ela não for um pangrama.

'''

#TESTES
#frase = 'a b c d e f g h i j l m n o p q r s t u v x z' #-> S
#frase = 'gazeta publica hoje: breve anuncio de faxina na quermesse'  #S
#frase = 'esta frase nao usa todas as letras, estao faltando algumas' #N

alfabeto = 'abcdefghijlmnopqrstuvxz'

frase = input('Digite uma frase: \n')
letras = set()

for l in frase:
  if l in alfabeto:
    letras.add(l)

'''
frase = ''.join(filter(str.isalnum, frase)) 
letras = set(frase)
'''

if len(letras) == len(alfabeto):
  print('S')
else:
  print('N')