'''
Tempo de resposta - Prova Fase 1 [P1] – OBI2021

Sara adora trocar mensagens com amigos. Como ela recebe e envia muitas
mensagens, está preocupada com o tempo que seus amigos esperam
para receber respostas das mensagens.

As seguintes regras de etiqueta são sempre obedecidas:

  • as únicas mensagens que Sara envia
  são respostas a mensagens que ela recebeu.

  • Sara envia no máximo uma mensagem como
  reposta a uma mensagem que recebeu.

  • um amigo de Sara nunca envia uma nova
  mensagem para Sara até que tenha recebido resposta
  da mensagem que enviou anteriormente.

O aplicativo de mensagens que Sara e seus amigos usam recebe e envia
mensagens instantaneamente. O envio e o recebimento de mensagens são
chamados de eventos. O aplicativo registra cada evento na ordem em que os
eventos ocorrem, usando dois tipos de registro:

  • R X indica que uma mensagem foi recebida do amigo X.
  • E X indica que uma mensagem foi enviada ao amigo X.

O aplicativo usa ainda um outro tipo de registro, para indicar o tempo que se passou entre dois eventos consecutivos, na forma

  • T X indicando que X segundos se passaram entre o evento anterior e o evento posterior a esse registro.

Se não há registro do tipo T X entre dois registros de eventos consecutivos signiﬁca que exatamente 1 segundo se passou entre esses dois eventos.

O Tempo de Resposta de uma mensagem é o tempo que se passa entre o
recebimento da mensagem por Sara e o envio da resposta a essa mensagem por
Sara. Se um amigo recebeu respostas para todas as suas mensagens, o Tempo
de Resposta Total para esse amigo é a soma dos Tempos de Respostas
para as mensagens desse amigo; caso contrário o Tempo de Resposta Total
para esse amigo é −1.

Dada a lista de registros do aplicativo de Sara, sua tarefa é determinar o
Tempo de Resposta Total para cada amigo.


Exemplos 01:
Entrada: 5 - R 2 - R 3 - T 5 - E 2 - E 3
Saida: 2 6 - 3 6


Exemplos 02:
Entrada: 14 - R 12 - T  2 - R 23 - T  3 - R 45
              E 45 - R 45 - E 23 - R 23 - T  2
              E 23 - R 34 - E 12 - E 34

Saida: 12 13 - 23 8 - 34 2 - 45 -1

'''
#RESUMO:

#RX   = Recebido de  X
#EX   = Enviado para X
#TX   = Tempo de Resposta

#Objetivo é Calcular o tempo de resposta total para cada amigo.

#Regras

#Ñ TX = Quanto não tem o TX, T X é igual a 1
#Se houver resposta (E), para de contar o tempo.
#Se houver uma resposta em aberto (R), o tempo final será -1 (Ñ Houve resposta). 


#Amigo: 45
#Ex: R 45 -> Recebido ==  add na lista de amigos
#    E 45 -> Enviado  ==  add T +1
#    R 45 -> Recebido ==  Como não houve resposta, T = -1

#SAIDA: 45 -1

#Amigo: 23
#Ex: R 23 -> Recebido        ==  add na lista de amigos
#    T  3 -> Tempo Resposta  ==  add T +3
#    E 23 -> Enviado         ==  Ignora pq teve o tempo antes.
#    R 23 -> Recebido        ==  Ignora pq já tá na lista
#    E 23 -> Enviado         ==  add T +1

#SAIDA: 23 4 

#Varios Amigos:
#Ex: R 12 -> Recebido        ==  add na lista de amigos -> [12]
#    T  2 -> Tempo Resposta  ==  add T +2               -> (12, 2)
#    R 23 -> Recebido        ==  add na lista de amigos -> [12, 23]
#    T  3 -> Tempo Resposta  ==  add T +3               -> (23, 3)/(12, 2+3)
#    R 45 -> Recebido        ==  add na lista de amigos -> [12, 23, 45]
#    E 45 -> Enviado         ==  add T +1               -> (23, 4) / (12, 6) / (45, 1)

#    R 45 -> Recebido        ==  N add nenhum amigo, mas temos uma msg aberta de 45.
#                                add T +1 p/ TODO MUNDO -> (23, 5) / (12, 7) / (45, 1)

#    E 23 -> Enviado         ==  add T +1               -> (23, 6) / (12, 8) / (45, 2)

#    R 23 -> Recebido        ==  N add nenhum amigo, mas temos uma msg aberta de 23.
#                                add T +1 p/ Todos      -> (23, 6) / (12, 9) / (45, 3)
#                                menos o 23, pq ele foi respondido.

#    T  2 -> Tempo Resposta  ==  add T +2               -> (23, 8) / (12, 12) / (45, 5)
#    E 23 -> Enviado         ==  N add T, pois já há.   -> (23, 8) / (12, 12) / (45, 5)
#    R 34 -> Recebido        ==  add na lista de amigos -> [12, 23, 34, 45] 
#    E 12 -> Enviado         ==  add T +1, menos o 23   -> (23, 8) / (12, 13) / (45, 6) / (34, 1)
#    E 34 -> Enviado         ==  add T +1, menos o 12   -> (23, 8) / (12, 13) / (45, 7) / (34, 2)

#    Como o 45 não obteve resposta a sua ultima msg ele fica com -1

#Saida: 12 13 - 23 8 - 34 2 - 45 -1


#Se houver mais de um amigo, responda em ordem crescente
#Ex: 23 8 - 45 -1

from os import system, name

#LimparTela
def clear():
  if name == "nt":
    _ = system('cls')
  else:
    _ = system('clear')

def tabelada(matriz):
  print('\n','-='*15) #frufru = exiba '-=' 15 vezes.

  #Exibindo Matriz
  print('\nTabelada:')

  for l in range(len(matriz)):
        for c in range(0,len(matriz[l])):
              #essa string está formatada,
              #o valor de c vai até 5 casas
              #decimais e está centralizado.
              print(f'[{matriz[l][c]:^5}]', end='')
        print() #quebra a linha para formar a tabela.
  
  print()
  print('-='*15)

def getPosAmigo(amigo:int) -> int:
  '''
  Get Posição do Amigo, recebe o 'nome'
  de um amigo do Quadro de Mensagens e
  retorna a posição em que ele está ou
  em que deveria ser colocado.
  '''
  global amigosAdd

  #Descobre em que posição ele foi adicionado na matriz
  #e retorna o valor dessa posição.
  return sorted(amigosAdd).index(amigo)


def addTempo (tempo):
  
  #Minha matriz é a variavel global, 'quadroMensagens'
  global quadroMensagens

  '''
  Adicionar tempo, acrescenta X tempo
  a todos os amigos N respondidos no
  Quadro de mensagens.

  Exemplo:
  addTempo(1)  -> Add +1 para todos.
 
  '''
  
  #Percorre o quadro de mensagens
  for i in range(len(quadroMensagens)):
  
    #Se esse amigo Ñ foi respondido
    if quadroMensagens[i][2]  == False:
      quadroMensagens[i][1] += tempo
    else:
      print('Menos ', quadroMensagens[i][0])
    

def addAmigo (amigo:int):
  '''
  Adicionar amigo, recebe como parametro
  a identificação de um amigo e adiciona
  ele em um Conjunto de Amigos (amigosAdd)
  e no Quadro de Mensagens.

  Exemplo:
  addAmigo(23) -> Add o amigo 23 no quadro.
  
  Lembrando que cada amigo é uma coluna do 
  nosso Quadro em que temos:
  
  id, tempo e status -> [ 23,  0 , False ]
  '''

  global amigosAdd
  global quadroMensagens
  
  #Se ele não estiver, add ele na lista
  amigosAdd.add(amigo)

  #Organiza os dados iniciais dele: Id, Tempo, Status
  novoAmigo = [amigo, 0, False]

  #Add esses dados no meu quadro de Mensagens.
  quadroMensagens.insert(getPosAmigo(amigo), novoAmigo)

def changeStatus(amigo:int):
  global amigosAdd

  p = getPosAmigo(amigo)

  #Atualiza o status da mensagem dele, para o valor inverso:
  quadroMensagens[p][2] = not quadroMensagens[p][2]


def test(entradas:list):

  lista_letras = ''

  for i in range(len(entradas)):
    msg = entradas[i]
    
    print(msg)

    letra  = msg[0]
    
    if i == 0:
      #Como essa é a minha 1º Letra, vou guarda-la na lista.
      lista_letras = letra

    if letra != 'T':
      #Guarda a identificação do amigo.
      amigo = msg[1:]
      
    else:
      #Guarda o tempo acumulado.
      tempo = int(msg[1:])

    #Feita a tratativa da msg, não precisamos mais dela.
    del(msg)

    #Se a 1º letra da msg for R
    if letra == 'R':  

      #Verifica se esse amigo já está na minha lista de amigos.
      if amigo not in amigosAdd:

        #Add esse nosso novo amigo no Quadro de Mensagens.
        addAmigo(amigo)
        
      #Se ele já estiver na lista...
      else:
        #Muda o Status da mensagem desse amigo.
        changeStatus(amigo)
        
    #Se a 1º letra da mensagem for E
    elif letra == 'E':
      
      changeStatus(amigo)
    
    #Depois da 2º entrada, iniciamos a contagem do tempo.
    if i != 0:
      #Se a ultima letra e a letra atual forem diferentes de T
      if lista_letras[-1] != 'T' and letra != 'T':
        
        print('Add 1 sg pra todos')
        #Add 1s p/ todos os amigos que N foram respondidos.
        addTempo(1)
      
      elif letra == 'T':
        #Mas se a letra atual for igual a T, add esse tempo.
        print(f'Add {tempo} sg pra todos')
        addTempo(tempo)

    #Guarda a ultima letra recebida
    lista_letras += letra

    #Para fins de debug:
    tabelada(quadroMensagens)
    input('Aperte enter p/ continuar')
    clear()


#Quadro de Mensagens é uma matriz em que cada coluna informa: Amigo, Tempo, Status
quadroMensagens = []

#Amigos Add é um conjunto de amigos que já foram adicionados.
amigosAdd       = set()

#Quantidade de Entradas é o nº de registros que vamos receber.
#qtEntradas = int(input(''))

exemplo_1 = ['R02','R03','T05','E02','E03']
#Saida Esperada: 2 6 - 3 6

exemplo_2 = [
    'R12','T02','R23','T03',
    'R45','E45','R45','E23',
    'R23','T02','E23','R34',
    'E12','E34']
#Saida Esperada: 23 8 - 45 -1

exemplo_3 = ['R45','E45','R45']
#Saida Esperada: 45 -1

exemplo_4 = ['R23','T03','E23','R23','E23']
#Saida Esperada: 23 4


test(exemplo_2)
print('\n')

#Exibindo o resultado:
#Percorre o quadro de mensagens.
for amigo in quadroMensagens:
  
  #Se esse amigo foi respondido:
  if amigo[2] != False:
    #Mostra o 'nome' dele e o tempo decorrido.
    print(amigo[0], amigo[1])
  
  else:
    #Se não, indica o nome e que N houve resposta.
    print(amigo[0], -1)

#Para fins de debug:
tabelada(quadroMensagens)