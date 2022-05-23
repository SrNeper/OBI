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
s = 12    #resultado da soma.
a = 10   #inicio
b = 200   #final

'''
s = int(input('Valor Desejado: \t'))
a = int(input('Inicio do Intervalo: \t'))
b = int(input('Fim do Intervalo: \t'))
'''
numbers = []

#Combinar os digitos de 0 à 9 é mais rapido do que percorrer todos os
#valores existentes entre A e B

#Então se o S tiver apenas 1 digito
if s<=9:
  
  for i in range(s+1):
    x = str(i)
    y = str(s-i)
    
    z = int(x+y)

    #print(f'X: {x}, Y: {y}, Z: {z}')
    
    #Adicionamos todas as dezenas possiveis dentro de numbers.
    if z>=a and z<=b:
      numbers.append(z)

elif s<=18:
  
  aux = s-9

  for i in range(aux, 10):
    x = str(i)
    y = str(s-i)
    
    z = int(x+y) 
     

    #print(f'X: {x}, Y: {y}, Z: {z}')
    #Adicionamos todas as dezenas possiveis dentro de numbers.
    if z>=a and z<=b:
      numbers.append(z)


print(numbers)

#Se numbers ainda estiver vazio, contamos do começo.
if len(numbers) == 0:  
  
  for i in range(a,b+1):
    algorismo = str(i)
    soma = 0
     
    #Soma cada digito do algorismo informado.      
    for d in algorismo:
      
      soma += int(d)

    #Se a soma, for igual ao nº informado, adiciona ele na lista.
    if soma == s:
      numbers.append(i)

#Se não estiver, contamos a partir do ultimo numero add a ele.
#Mas se o B for menor do que 100, todos os valores possiveis já
#foram adicionados.
elif b>100:
  
  a = numbers[-1]+1

  for i in range(a,b+1):
    algorismo = str(i)
    soma = 0
      
    #Soma cada digito do algorismo informado.      
    for d in algorismo:
      
      soma += int(d)

    #Se a soma, for igual ao nº informado, adiciona ele na lista.
    if soma == s:
      numbers.append(i)


total = len(numbers)

#Se houver algo em numbers
if total != 0:
  print()
  
  #Numere e exiba esses valores:
  for i,e in enumerate(numbers):
  
    #Preenche com Zeros a esquerda dos valores com o nº de digitos
    #menor que o do maior valor.
    difA = len(str(total)) - len(str(i+1))
    auxA = '0'*difA
    
    difB = len(str(numbers[-1])) - len(str(e)) 
    auxB = '0'*difB

    print(f'{auxA}{i+1}º  -> {auxB}{e}')
    
print(f'\nTotal: {total}')

