'''
  Você está de volta em seu hotel na Tailândia
  depois de um dia de mergulhos. O seu quarto
  tem duas lâmpadas. Vamos chamá-las de A e B.
  No hotel há dois interruptores, que chamaremos
  de I1 e I2. Ao apertar I1, a lâmpada A troca de
  estado, ou seja, acende se estiver apagada e
  apaga se estiver acesa. Se apertar I2, ambas
  as lâmpadas A e B trocam de estado. As lâmpadas
  inicialmente estão ambas apagadas. Seu amigo
  resolveu bolar um desafio para você. Ele irá
  apertar os interruptores em uma certa
  sequência, e gostaria que você respondesse
  o estado final das lâmpadas A e B.

Entrada:
  A primeira linha contém um número N que
  representa quantas vezes seu amigo irá
  apertar algum interruptor. Na linha
  seguinte seguirão N números, que pode
  ser 1, se o interruptor I1 foi apertado,
  ou 2, se o interruptor I2 foi apertado.

Saída:
  Seu programa deve imprimir dois valores,
  em linhas separadas. Na primeira linha,
  imprima 1 se a lâmpada A estiver acesa no
  final das operações e 0 caso contrário.
  Na segunda linha, imprima 1 se a lâmpada B
  estiver acesa no final das operações
  e 0 caso contrário.

Exemplos:
  | = pula uma linha.
  , = colocados lado a lado.

01>
  Entrada = 3 | 1,2,2
  Saída   = 1 | 0
02>
  Entrada = 4 | 2,1,2,2
  Saída   = 1 | 1

'''
#Guarda a quantidade de vezes em que as pessoas usaram o interruptor
n_acoes = int(input())

#Lampadas apagadas
lampadas = [False, False]

#Inicia as interações.
for i in range(n_acoes):
  
  #Pega a ação realizada.
  acao = int(input())

  #Se tiverem apertado o 1º interruptor
  if acao == 1:
    
    #Muda o status da 1º lampada.
    lampadas[0] = not lampadas[0] #True -> False // False -> True
  
  #Se for o 2º
  else: 
    #Muda o status da 2º lampada.
    lampadas[1] = not lampadas[1]

#Percorre a lista de lampadas
for status in lampadas:

  #Se o status dessa lampada for verdadeiro.
  if status == True:
    #Mostra 1 = Ligada
    print(1)
  
  #Se não...
  else:
    #Mostra 0 = Desligada
    print(0)
  