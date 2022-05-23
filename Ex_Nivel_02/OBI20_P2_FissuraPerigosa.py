"""
OBI20 - P2 - F1 - Fissura Perigosa:

A erupção do vulcão Kilauea em 2018 no Havaí atraiu a atenção de todo o mundo.
Inicialmente a força da erupção era menor e a lava avançou para o sul com
relativamente poucos danos. Após algumas semanas, porém, a fissura 8 começou a
jorrar com mais força e a lava avançou também para o norte trazendo muita
destruição.

Você está ajudando na implementação de um sistema para simular a área por onde a
lava avançaria, em função da força da erupção. O mapa será representado
simplificadamente por uma matriz quadrada de caracteres, de 1 a 9, indicando a
altitude do terreno em cada posição da matriz. Vamos considerar que a fissura 8,
por onde a erupção se inicia, está sempre na posição do canto superior esquerdo
da matriz. Dada a força da erupção, que será um valor inteiro, de 0 a 9, seu
programa deve imprimir a matriz de caracteres representando o avanço final da
lava. Se a lava consegue invadir uma posição da matriz, o caractere naquela
posição deve ser trocado por um asterisco ('*'). Uma posição será invadida pela
lava se seu valor for menor ou igual à força da erupção e for a posição inicial;
ou estiver adjacente, ortogonalmente (abaixo, acima, à esquerda ou à direita), a
uma posição invadida.

A figura abaixo mostra um exemplo de mapa e o avanço final da lava para quatro
forças de erupção: 1, 3, 6 e 8, respectivamente da esquerda para a direita.

            27755478     *7755478     *7755478     ********
            29985439     *9985439     *9985439     *99****9
            34899989     *4899989     **899989     ***999*9
            22115569     ****5569     *******9     *******9
            66736689     667*6689     **7***89     *******9
            99886555     99886555     9988****     99******
            44433399     44433399     ******99     ******99
            99986991     99986991     9998*991     999**991

Entrada
A primeira linha da entrada contém dois inteiros N e F representando,
respectivamente o número de linhas (que é igual ao de colunas) da matriz e a
força da erupção. Cada uma das N linhas seguintes contém uma string de N
caracteres, entre 1 e 9, indicando o mapa de entrada.

Saída
Seu programa deve imprimir N linhas contendo, cada uma, N caracteres
representando o avanço final da lava de acordo com o enunciado.

Restrições
1 ≤ N ≤ 500
0 ≤ F ≤ 9

Exemplo 01:
  Entrada:          Saída 
    8 6
    27755478       *7755478
    29985439       *9985439
    34899989       **899989
    22115569       *******9
    66736689       **7***89
    99886555       9988****
    44433399       ******99
    99986991       9998*991


Exemplo 02:
  Entrada:          Saída 
    5 4
    25679          *5679
    35234          *5***
    17182          *7*8*
    39993          *999*
    11223          *****

Exemplo 03:
  Entrada:         Saída 
    2 8
    91             91
    11             11
"""

#Importando funções de interface //
from os import system, name

def clear(ide = "x"):
  '''
  Clear é uma função que limpa o console
  de acordo com a IDE e as biliotecas 
  utilizadas. No google colab ela usa
  a 'IPython.display', mas fora dele
  pode ser usada a 'os' que permite
  acessar os comandos do sistema
  operacional: cls ou clear.

  Abaixo estão os comandos para importar
  as bibliotecas.

  from os import system, name
  from IPython.display import clear_output

  Como parametro informe a IDE que está
  utilizando: 'g' para o Google
  ou 'x' para qualquer outra.
  '''

  if ide != 'g': 
    if name == "nt":
      _ = system('cls')
    else:
      _ = system('clear')

  #Se tiver importado a IPython
  #use o método: clear_output()


def mostrarMapa(matriz:list):
  '''
  Essa função recebe a matriz do mapa
  e exibe ele na tela como Tabela,
  ajudando na visualização dos eventos
  que ocorrem durante a erupção.
  '''
  print('\n','-='*25) #frufru = exiba '-=' 15 vezes.

  #Exibindo o Mapa
  print(f'\n{"Mapa:":^50}\n')
  
  areas = list(range(1,len(matriz)+1))
  print(f'Areas:  {areas}')
  
  #Exibindo cada coluna/linha do mapa.
  for c in range(len(matriz)):
    print(f'R  0{c+1}:  {matriz[c]}', end='')
    print() #quebra a linha para formar a tabela.
  
  print()
  print('-='*25)

#Funções de Entrada e Implementação.

#Funções de Entrada e Construção da Matriz

def getParametros (exe = 0) -> list:
  """
  getParametros interage com o usuario
  para obter a escala da matriz e a força
  da erupção.

  Se a variavel exe for passada, ele
  passa esses valores de acordo com
  os exemplos do enunciado.
  """

  parametros = ""
  
  exemplos = {
    0:parametros,
    1:"86",
    2:"54",
    3:"28",
  }
  
  if exe == 0:
    parametros = input().replace(" ", "")
  
  else:
    
    parametros = exemplos[exe]
    
  return [int(parametros[0]), int(parametros[1])]

#Escolha um exemplo de 1 a 3 ou deixe 0 para rodar de verdade.

def getRelevos(escala = 0, exe = 0) -> list:
  '''
  getRelevos é uma função que interage com o usuário
  para obter os relevos que preencherão o mapa.
  Esses valores retornam como uma lista
  de strings e devem ser processados para montar
  a matriz.

  Em caso de teste, a variavel exe pode ser passada
  para que ao invés de interagir com o usuario,
  a função retorne os valores de relevo correspondentes
  aos exemplos descritos no enunciado. Nesse caso
  o valor da escala tbm será alterado de acordo 
  com o exemplo.

  Se os parametros informados estiverem errados
  a função retorna como "None".
  '''
  relevos = []

  if escala != 0 and exe == 0:
    for i in range(escala):
  
      #Relevo é uma string comoosta por numeros.
      relevos.append(input().replace(" ", ""))
  
  elif exe == 1:
    relevos = [
      "27755478",
      "29985439",
      "34899989",
      "22115569",
      "66736689",
      "99886555",
      "44433399",
      "99986991",
    ]    
  
  elif exe == 2:
    relevos = [
      "25679",          
      "35234",          
      "17182",
      "39993",          
      "11223",
    ]
    
  elif exe == 3:
    relevos = [
      "91",          
      "11",          
    ]    
    
  else:
    #os dados informados estão errados.
    return 

  return relevos


def preencherMapa(escala:int, mapa:list, relevos:list) -> list:
  '''
  Preencher Mapa, recebe como parametro a
  escala do território, a matriz usada
  como mapa e os valores dos relevos.

  Cria e preenche a matriz com esses
  valores e retorna ela montada
  para o usuario.

  Obs. Relevo é uma lista de strings.
  '''
  if relevos != [] and escala !=0 and type(mapa) == list:
    
    for i in range(escala):

      r = relevos[i] 

      mapa.append([int(n) for n in r])
  
  else:
    #Se as condições não forem atendidas, retorna como vazio.
    return 
    
  return mapa


def checkRegiao(forca:int, regiao:list, start = 0) -> list:
      
  for area in range(start, len(regiao)):
          
    if regiao[area] != 0 and forca>= regiao[area]:
      #print(f"  -> Essa região, teve a area {area+1}: Destruida. \n")
      regiao[area] = 0
      
    else:  
      #print(f"  -> O avanço da lava foi bloqueado na area {area+1}.\n")
      break

  #Se ainda houver um ponto fraco nessa regiao
  if forca in regiao:
    #print("\n  -> Antes: ", regiao)
    idA = regiao.index(f)

    #E antes dele houver um zero, voltamos a checar.
    if regiao[idA-1] == 0:
      checkRegiao(forca, regiao, idA)
      #print("\n  -> Depois: ", regiao)

  return regiao



exe = 1

mapa = []

#Paramentros = 0 -> Escala / 1 -> Força da Erupção.
p = getParametros(exe)

relevos = getRelevos(p[0],exe)

mapa = preencherMapa(p[0], mapa, relevos)

for r in relevos:
  print(r)

mostrarMapa(mapa)

for f in range(1, p[1]+1):
   
  #print(f"\n{f}º Erupção: \n")
  
  for regiao in mapa:  
    
    idR = mapa.index(regiao)

    #Essa regiao possui areas que podem ser derrubadas por essa força?
    if f in regiao:
      
      #Vamos descobrir a onde está essa area.
      idA = regiao.index(f)

      #E recortar o trecho que vem antes dela.
      trecho = regiao[:idA+1]

      #Se o maior valor desse trecho, for menor que f
      if f>=max(trecho): 
        #print(f"A lava entrou na {idR+1}º Região. \n")
            
        #Então esse trecho pode ser derrubado, area a area. 
        mapa[idR] = checkRegiao(f, regiao)
      
        
      #Se não for, podemos verificar se alguma outra região
      #é vizinha a esse ponto fraco.
      elif regiao == mapa[0]:

        #Se essa região for a primeira, ela só faz fronteira com a 2º
        if mapa[1][idA] == 0:
          
          #print(f"A lava da região 2, transbordou para 1. \n")
          
          #O trecho a ser percorrido, vai dela (idA), pra frente.
          resto = regiao[idA:]
          
          #Depois junta tudo de novo.
          mapa[idR] = regiao[:idA]+checkRegiao(f, resto)
      
      #Se essa região for a ultima
      elif regiao == mapa[-1]:
        
        #Ela só faz fronteira com a penultima
        if mapa[-2][idA] == 0:
          #print(f"A lava da região {len(mapa)-1}, transbordou para {len(mapa)}. \n")

          resto = regiao[idA:]
          mapa[idR] = regiao[:idA]+checkRegiao(f, resto)

      #Se ela não for nem a primeira, nem a ultima, pode vazar dos 2 lados.
      else:

        #print(f"  \nATENÇÃO - LAVA PODE TRANSBORDAR p/ região {idR+1}!!")
        #print(f"  O Ponto Fraco dela é a area: {idA} ")
        #print(f"""  SITUAÇÃO: 
                #{idR}º :{mapa[idR-1]}
                #{idR+1}º :{mapa[idR]}
                #{idR+2}º :{mapa[idR+1]}\n
              #""")
        
        #Ela só faz fronteira com a penultima
        if mapa[idR-1][idA] == 0 or mapa[idR+1][idA] == 0:
          #print(f"\nA lava da região {idR} ou {idR+2},"+
                #f" transbordou para {idR+1}. \n")

          #E o trecho a ser percorrido, vai dela (idA), pra frente.
          resto = regiao[idA:]

          #print(f"  -> Trecho afetado: {resto}")
          
          #Depois junta tudo de novo e atualiza o mapa.
          mapa[idR] = regiao[:idA]+checkRegiao(f, resto)
        
        #else:
          #print(f"  -> Felizmente, ela não foi invadida!")
          #print(f"    Já que a area {idA} dos seus vizinhos não\n"+
               #"    foram destruidas.\n")
          
    #else:
      #print(f"A {idR+1}º Região saiu ilesa dessa erupção. \n")


  #mostrarMapa(mapa)
  #input()
  #clear()

print()
for regiao in mapa:
  print("".join([str(n) for n in regiao]).replace("0", "*"))