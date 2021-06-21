'''
Cifra da Nlogônia - Prova Fase 1 [P2] – OBI2021

O rei da Nlogônia ordenou que todos os documentos
importantes sejam “cifrados”, para que apenas
quem tem conhecimento da cifra possa lê-los (cifrar um
documento signiﬁca alterar o original
modiﬁcando as letras de acordo com algum algoritmo de cifra).

O rei decretou que o seguinte algotimo deve ser usado para
cifrar os documentos:

  • Cada consoante deve ser substituída por exatamente três
  letras, na seguinte ordem:

    1. a própria consoante (vamos chamar de consoante
    original);
    
    2. a vogal mais próxima da consoante original no
    alfabeto, com a regra adicional de que se a consoante original está à mesma distância de duas vogais, então a vogal mais próxima do início do alfabeto é usada. Por exemplo, se a consoante original é d, a vogal que deve
    ser usada é e, pois esta é a vogal mais próxima; se a consoante original é c, a vogal que
    deve ser utilizada é a, porque c está à mesma distância de a e e, e a é mais próxima do início do alfabeto.

    3. a consoante que segue a consoante original, na ordem
    do início ao ﬁm do alfabeto. Por exemplo, se a consoante
    original é d, a consoante a ser utilizada é f. No caso
    de a consoante original ser z, deve ser utilizada a
    própria letra z.

• As vogais não são modiﬁcadas.

Nesta tarefa, o alfabeto é
  a b c d e f g h i j k l m n o p q r s t u v x z

  e as vogais são: a e i o u

Por exemplo, a cifra da palavra “ter” é “tuveros” 
(tuv-e-ros) e a cifra da palavra “paz” é “poqazuz”
(poq-a-zuz).

O rei da Nlogônia procura por alguém que saiba escrever um
programa que produza a cifra de uma palavra dada. Você pode
ajudá-lo?

Entrada
A primeira e única linha da entrada contém uma palavra P
formada por letras minúsculas sem acentuação.

Saída
Seu programa deve produzir uma única linha, contendo a palavra cifrada.


Exemplo 01:
entrada: 'ter'
saída:   'tuveros'

Exemplo 02:
entrada: 'rei'
saida:   'rosei'

Exemplo 03:
entrada: 'arteiro'
saída:   'arostuveiroso'

'''



#Tupla com o alfabeto
alfabeto = ( 'a',  'b',  'c',  'd',
             'e',  'f',  'g',  'h',
             'i',  'j',  'k',  'l',
             'm',  'n',  'o',  'p',
             'q',  'r',  's',  't',
             'u',  'v',  'x',  'z')

#Posição das Vogais no Alfabeto
posVogais = {'a':0, 'e':4, 'i':8, 'o':14, 'u':20}

palavra = str(input())

#posOriginal = palavra[0]

