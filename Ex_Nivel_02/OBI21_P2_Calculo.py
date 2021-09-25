'''
Calculo - Prova Fase 2 [P2] – OBI2021

Algumas pessoas conseguem fazer cálculos matemáticos com uma
velocidade impressionante. Laurinha tem essa habilidade!

Um cálculo que ela consegue fazer muito rapidamente é, dados três
números inteiros S, A, e B, determinar quantos números do intervalo
[A; B] têm a soma de seus dígitos igual a S.

Por exemplo:
  Se S = 3, A = 10 e B = 30,
  então a reposta é 3! 
  Pois existem três números no intervalo [10; 30] 
  cuja soma dos dígitos é igual a três: 12, 21 e 30.

Sua tarefa é escrever um programa de computador para, dados os três números
tentar calcular a resposta mais rapidamente do que Laurinha consegue.


Restrições: S [1~36] | A&B [1~10000] | A<=B

Ex 01:
Entrada: 3 - 10 - 30 
Saida: 3

Ex 02:
Entrada: 15 - 1 - 20 
Saida: 0

Ex 03:
Entrada: 1 - 1 - 10000 
Saida: 5

'''
#Testes
s = 3     #resultado da soma.
a = 1    #inicio
b = 10000   #final
test = 1 

'''
s = int(input('Valor Desejado: \t'))
a = int(input('Inicio do Intervalo: \t'))
b = int(input('Fim do Intervalo: \t'))
'''
numbers = []

def comum():
  #Resolução Comum - Tempo de Execução maior:
  global numbers  
  numbers = []
  
  for i in range(a,b+1):
    algorismo = str(i)
    soma = 0
    
    #Soma cada digito do algorismo informado.      
    for d in algorismo:
      soma += int(d)

    #Se a soma, for igual ao nº informado, adiciona ele na lista.
    if soma == s:
      numbers.append(i)

def alternativa():
  global numbers
  aux = a

  while aux%s != 0:
    aux-=1
    
  numbers = []
  id = aux//s

  while True:
    x = s*id
    soma = 0
    
    for i in (str(x)):
        soma += int(i)
    
    if soma == s and x<=b and x>=a:
        numbers.append(x)
    
    id+=1
    
    if x>=b:
        break

def sum_algorismos():
  global numbers, b

  n = s
  d = len(str(b))

  numbers, test = [], []

  for i in range(d):
    for o in range(n):
      test.append((n-o+o*10)*10**i)
    
      if test[-1]>n and test[-1]<n*10:
        x = str(test[-1])
        
        n1 = int(x[0]) 
        n2 = int(x[1])
        
        y = (n1*100)+n2 
        
        test.append(y)
        
        if int(x[1]+x[0]) not in test or x[0] == x[1]:
            
          #Se os dois forem pares e maiores do que 1.
          if n1%2 == 0 and n2%2 == 0 and n1>1:
            A = str(n1//2)
            B = str(n2//2)       
                
            if x[0] != x[1]:
              test.append(int(str(n1)+B*2))
              test.append(int(str(n2)+A*2))
              test.append(int(B*2+str(n1)))
              test.append(int(A*2+str(n2)))
              test.append(int(A*2+B*2))
              test.append(int(B*2+A*2))
                
            else:
              test.append(int(str(n1)+B*2))
              test.append(int(A*2+str(n2)))
              test.append(int(A*2+B*2))
          
          elif n1%2 == 0 and n2%2 != 0 and n1>1:
                A = str(n1//2)                            
                
                if int(A) != n1:
                  test.append(int(A*2+str(n2)))
                  test.append(int(str(n2)+A*2))
                else:
                  test.append(int(A*2+str(n2)))

          elif n1%2 != 0 and n2%2 == 0 and n2>1:
                B = str(n2//2)

                if int(B) != n2:                            
                  test.append(int(B*2+str(n1)))
                  test.append(int(str(n1)+B*2))
                else:
                  test.append(int(B*2+str(n1)))
              
  test.append(n*10**d)
  test.sort()

  for i in test:
    if i>=a and i<=b and i not in numbers:
      numbers.append(i)


import time

tempo = []
nTestes = 1

if test == 0:
  print(f'\nT0 - Nº Encontrados entre {a} & {b}\n')
  #só funciona com b<=100 e s<=16
  for i in range(nTestes+1):

    ini = time.time()
    sum_algorismos() 
    fim = time.time()
  
    t = fim-ini
    tempo.append(t)
  
elif test == 1:
  print(f'\nT1 - Nº Encontrados entre {a} & {b}\n')
  for i in range(nTestes+1):

    ini = time.time()
    comum() 
    fim = time.time()
  
    t = fim-ini
    tempo.append(t)

elif test == 2:
  print(f'\nT2 - Nº Encontrados entre {a} & {b}\n')
  for i in range(nTestes+1):

    ini = time.time()
    alternativa() 
    fim = time.time()
  
    t = fim-ini
    tempo.append(t)

for i, e in enumerate(numbers): 
  if i<9 and e<9:
    print(f'0{i+1}º: {0}{e}  -> Soma = {s} -> Multiplo ({e%s == 0})')
  
  elif i<9:
    print(f'0{i+1}º: {e}  -> Soma = {s} -> Multiplo ({e%s == 0})')

  elif e<9:
    print(f'{i+1}º: 0{e}  -> Soma = {s} -> Multiplo ({e%s == 0})')
  
  else:
    print(f'{i+1}º: {e} -> Soma = {s} -> Multiplo ({e%s == 0})')

print(f'\nTotal: {len(numbers)}')
print(f'Tempo: {sum(tempo)/len(tempo):0.6f} seconds')
print(f'nº Tentativas: {nTestes}')
