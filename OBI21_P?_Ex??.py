n1 = '69961'  #input('Digite o 1º Valor: \t')
n2 = '487926' #input('Digite o 2º Valor: \t')


#Deixando as strings com o mesmo tamanho.
if len(n1) > len(n2):
  dif = len(n1) - len(n2)
  
  #Complementando elas com 0 a esquerda.
  aux = '0'*dif
  n2 = aux+n2

elif len(n1) < len(n2):
  dif = len(n2) - len(n1)
  aux = '0'*dif
  n1 = aux+n1

del(aux)

aux1 = ''
aux2 = ''

#Comparando os valores de cada string.  
for i in range(len(n1)):

  #Se o valor de n1[i] for maior que n2[i]  
  if int(n1[i]) > int(n2[i]):
    
    #Guarda esse valor na aux1
    aux1 += n1[i]
    
  elif int(n2[i]) > int(n1[i]):
    aux2 += n2[i]
    
  else:
    #Se os valores forem iguais guarda eles nas
    #duas variaveis auxiliares.
    aux1 += n1[i]
    aux2 += n2[i]

#Se nenhum valor tiver sido guardado.        
if len(aux1) == 0:
  aux1 = '-1'

if len(n2) == 0:
  aux2 = '-1'

#Exibe os valores obtidos.
print(f'{aux2} {aux1}')    