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
Saída: 2 6 - 3 6


Exemplos 02:
Entrada: 14 - R 12 - T  2 - R 23 - T  3 - R 45
              E 45 - R 45 - E 23 - R 23 - T  2
              E 23 - R 34 - E 12 - E 34

Saída: 12 13 - 23 8 - 34 2 - 45 -1

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

#SAÍDA: 45 -1

#Amigo: 23
#Ex: R 23 -> Recebido        ==  add na lista de amigos
#    T  3 -> Tempo Resposta  ==  add T +3
#    E 23 -> Enviado         ==  Ignora pq teve o tempo antes.
#    R 23 -> Recebido        ==  Ignora pq já tá na lista
#    E 23 -> Enviado         ==  add T +1

#SAÍDA: 23 4 


from os import system, name

#LimparTela
def clear():
  if name == "nt":
    _ = system('cls')
  else:
    _ = system('clear')

quadroMensagens = [[],[],[],[],[]]

#Pessoa X.
pessoa = quadroMensagens[0]

#lst = ultimo momento em que recebi uma mensagem da pessoa x
lst = quadroMensagens[1]

#waiting = true se, e só se, ainda não respondi a pessoa x 
waiting = quadroMensagens[2]

#exist = true se, e só se, existe alguma pessoa com o id x
exist = quadroMensagens[3]

#total = tempo de resposta total atual da pessoa x
total = quadroMensagens[4]


#Recebe o nº total de registos.
qtRegistros = int(input("Digite o nº de registros \n"))

#tmp é o horário atual, e t é true se, e só se, o registro anterior é do tipo 'T'
tmp, t = 0, False

for i in range(qtRegistros+1):
  txt = input(f"Digite o {i+1} registro: ")

  #Corta o texto para pegar o status (R, T ou E)
  status = txt[0]

  #Corta o texto para pegar o nº.
  n = int(txt[2:])

  #Se o anterior não é um registro 'T' e o atual não é um registro 'T',
	#significa que se passou 1 segundo.
  if t == False and status != "T":
    tmp +=1

  #Se status == 'T', então precisamops aumentar o horário atual.
  if status == 'T':
    tmp += n
    t = True

    #Para esse ciclo e da continuidade ao for.
    continue

  #Se status == 'R' a pessoa x está aguardando pela resposta, 
	#a ultima vez que ela enviou uma mensagem agora é tmp e
	#ela, obviamente existe.
  if status == 'R':

    if n not in pessoa:

      #Add esse amigo no quadro
      pessoa.append(n)

      
      #Add esse tempo de espera
      lst.append(tmp)
      
      #Marca que ele está esperando.
      waiting.append(True)
  
      #Marca que ele existe
      exist.append(True)

      #Inicia o tempo de espera
      total.append(0)
    
    else:

      #Descobre onde ele está:
      amigoID = pessoa.index(n)

      #Add esse tempo de espera
      lst[amigoID] = tmp
      
      #Marca que ele está esperando.
      waiting[amigoID] = True
  
      #Marca que ele existe
      exist[amigoID] = True

      #Atualiza o tempo de espera
      total[amigoID] = 0
      
  #Se c == 'E', a pessoa x não está mais aguardando resposta,
	#e podemos incrementar seu tempo total de espera.    
  else:
    amigoID = pessoa.index(n)

    #Marca que ele está esperando.
    waiting[amigoID] = False
    
    #Calcula o tempo de espera
    total[amigoID] += tmp - lst[amigoID]
    
  #O atual vai se tornar o anterior na próxima iteração, 
	#e como não é um registro do tipo 'T', a flag t será falsa.
  t = False

for i in range(len(pessoa)):
  if exist[i] == True and waiting[i] == False:
    print(pessoa[i], total[i])
  
  else:
    print(pessoa[i], -1)