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
    alfabeto, com a regra adicional de que se a consoante
    original está à mesma distância de duas vogais,
    então a vogal mais próxima do início do alfabeto
    é usada. Por exemplo, se a consoante original é D,
    a vogal que deve ser usada é E, pois esta é a vogal
    mais próxima; se a consoante original é C, a vogal que
    deve ser utilizada é A, porque C está à mesma distância
    de A e E, e A é mais próxima do início do alfabeto.

    3. a consoante que segue a consoante original, na ordem
    do início ao ﬁm do alfabeto. Por exemplo, se a consoante
    original é D, a consoante a ser utilizada é F. No caso
    de a consoante original ser Z, deve ser utilizada a
    própria letra Z.

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
saída:   'rosei'

Exemplo 03:
entrada: 'arteiro'
saída:   'arostuveiroso'

'''
#Resumo: A cifra é composta pela letra original + vogal e consoante prox.
#Exemplo: T -> Tuv //
#Se 2 vogais forem prox, pega a + prox do inicio.
#Exemplo: C -> Cad // AbCdE <- A dist entre A e E é igual. 
#Se for o Z, a prox consoante é o proprio Z ele não reinicia o Alfabeto.
#Se a letra já for uma vogal, não troca.


def getProxConsoante(consoante:str) -> str:

  global alfabeto, vogais
  
  posConsoante = alfabeto.index(consoante)

  #Se a consoante for a letra Z, a prox é ela mesma.
  if consoante == 'z':
    proxConsoante = 'z'
  else:
    proxConsoante = ' '

  #N é uma variavel auxiliar que vai nos ajudar a procurar pela proxConsoante.
  n = 1

  #Repita enquanto a proxConsoante estiver vazia ou for uma vogal
  while proxConsoante in vogais or proxConsoante == ' ':

    proxConsoante = alfabeto[posConsoante + n]
    n += 1

  return proxConsoante

def getProxVogal(consoante:str) -> str:
  
  #Posição das Vogais no Alfabeto
  posVogais = [0,4,8,14,20]

  #Qual é a posição dessa consoante?
  posicao = alfabeto.index(consoante)  

  #Primeiro mapeamos a posição da letra original
  #em relação a posição das Vogais.
  mapa = sorted([posicao] + posVogais)

  #Depois precisamos ver qual é a distancia dela em
  #relação as demais.

  #Se ela for a ultima do mapa
  if mapa[-1] == posicao:
    #A vogal mais prox é a que vem antes dela.
    vogal = mapa.index(posicao)-1
  
  #Se não...
  else:
    
    #Precisamos calcular essa distancia.
    #Distancia_A é igual a diferença entre a posição dela e a da prox vogal.
    #Exemplo: T = 19 / U = 20 -> Distancia_A = 20-19 = 1
    dist_a = mapa[mapa.index(posicao)+1] - posicao

    #Distancia_B é igual a diferença entre a posicao dela e a da vogal anterior.
    #Exemplo: T = 19 / O = 14 -> Distancia_B = 19-14 = 5
    dist_b = posicao - mapa[mapa.index(posicao)-1]

    #print(f'P: {posicao} | ProxV: {mapa[mapa.index(posicao)+1]} | DA', dist_a)
    #print(f'P: {posicao} | AntV:  {mapa[mapa.index(posicao)-1]} | DB', dist_b)

    #Se a distancia A for maior ou igual a que a B
    if dist_a >= dist_b:
      #Pegamos a posição da vogal anterior a consoante.
      #Exemplo: C = 2 / A = 0 / E = 4
      #dist_a = 4-2 = 2
      #dist_b = 2-0 = 2
      #vogal =  0 -> A
      vogal = mapa.index(posicao)-1
      
    else:
      #Caso contrario, pegamos a prox.
      #Exemplo: T = 19 / O = 14 / U = 20
      #dist_a = 20-19 = 1
      #dist_b = 19-14 = 5
      #vogal =  20 -> U
      vogal = mapa.index(posicao)+1

  #Com isso, basta encontra-la no alfabeto
  return alfabeto[mapa[vogal]]


def cifra(palavra:str) -> str:

  cifra = ''

  #Percorre cada letra da palavra enviada:
  for i in range(len(palavra)):

    letra = palavra[i]

    #Se essa letra não for uma vogal.
    if letra not in vogais:
      #Descobre quem é a prox consoante.
      proxConsoante = getProxConsoante(letra)

      #E qual é a vogal mais proxima dela.
      vogal = getProxVogal(letra)

      cifra += letra + vogal + proxConsoante

    else:
      cifra += letra

  #Cifra gerada pelo nosso código  
  return cifra

#Tupla com o alfabeto
alfabeto = ( 'a',  'b',  'c',  'd', #00~03
             'e',  'f',  'g',  'h', #04~07
             'i',  'j',  'k',  'l', #08~11
             'm',  'n',  'o',  'p', #12~15
             'q',  'r',  's',  't', #16~18
             'u',  'v',  'x',  'z') #19~22

vogais = 'aeiou'

palavra = str(input('\nDigite uma palavra: \t')).lower()

print('\nPalavra Original: ',palavra.capitalize())
print('Palavra Cifrada:  ',cifra(palavra).capitalize())
