'''
  Os administradores da Fazenda Fartura planejam criar uma
  nova plantação de morangos, no formato retangular. Eles
  têm vários locais possíveis para a nova plantação, com
  diferentes dimensões de comprimento e largura. Para os
  administradores, o melhor local é aquele que tem a maior
  área. Eles gostariam de ter um programa de computador
  que, dadas as dimensões de dois locais, determina o que
  tem maior área. Você pode ajudá-los?

Entrada:
  A entrada contém quatro linhas, cada uma contendo um
  número inteiro. As duas primeiras linhas indicam as
  dimensões (comprimento e largura) de um dos possíveis
  locais. As duas últimas linhas indicam as dimensões
  (comprimento e largura) de um outro possível local para
  a plantação de morangos. As dimensões são dadas em
  metros.

Saída:
  Seu programa deve escrever uma linha contendo um único
  inteiro, a área, em metros quadrados, do melhor local
  para a plantação, entre os dois locais dados na entrada.

Restrições:
 a) 1 ≤ comprimento ≤ 100
 b) 1 ≤ largura ≤ 100

Exemplos:
  | = pula uma linha.
  , = colocados lado a lado.

01>
  Entrada = 30|8|11|56
  Saída   = 616
02>
  Entrada = 12|38|5|20
  Saída   = 456

'''
medidas = list()
#medidas[0] -> A = Comprimento do Local A //
#medidas[1] -> B = Comprimento do Local A //
#medidas[2] -> C = Comprimento do Local B //
#medidas[3] -> D = Comprimento do Local B //

#lados é uma variável auxiliar que vai nos ajudar a interagir com o usuário.
#na OBI a interação via texto com o usuário não ocorre, mas pra testar, ajuda muito. 
lados = 'abcd'

#Vamos receber 4 valores.
for i in range(4):
    #X é nossa variável de entrada.
    x = 0

    #Pegando e Validando as Dimensões
    while not 1<= x <=100:
        x = int(input(f"Digite o valor de {lados[i]}:\t"))
    
    #Se as dimensões forem validas, guardamos na lista.
    else:
        medidas.append(x)

#Agora que não precisamos mais interagir, podemos apagar essa variável.
del(lados)

#Calculando o tamanho dos locais.
localA = medidas[0]*medidas[1] #A*B
localB = medidas[2]*medidas[3] #C*D

#Verificando quem é maior
if localA > localB:
    
    #Exibindo o resultado.
    print(localA)
else:
    print(localB)
