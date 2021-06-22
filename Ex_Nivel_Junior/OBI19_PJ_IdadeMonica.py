'''
Dona Mônica é mãe de três filhos que têm idades diferentes. Ela notou que, neste ano, a soma das idades dos seus três filhos é igual à idade dela. Neste problema, dada a idade de dona Mônica e as idades de dois dos filhos, seu programa deve computar e imprimir a idade do filho mais velho.

Por exemplo, se sabemos que dona Mônica tem 52 anos e as idades conhecidas de dois dos filhos são 14 e 18 anos, então a idade do outro filho, que não era conhecida, tem que ser 20 anos, pois a soma das três idades tem que ser 52. Portanto, a idade do filho mais velho é 20. Em mais um exemplo, se dona Mônica tem 47 anos e as idades de dois dos filhos são 21 e 9 anos, então o outro filho tem que ter 17 anos e, portanto, a idade do filho mais velho é 21.

Entrada
A primeira linha da entrada contém um inteiro M representando a idade de dona Mônica. A segunda linha da entrada contém um inteiro A representando a idade de um dos filhos. A terceira linha da entrada contém um inteiro B representando a idade de outro filho.
Saída
Seu programa deve imprimir uma linha, contendo um número inteiro, representando a idade do filho mais velho de dona Mônica.

'''
#Idades é uma lista que vai armazenar todas as idades recebidas.
idades = []
print('Digite as respectivas idades: Mônica, Filho 1 e Filho 2:\n')

for i in range(3):
  idades.append(int(input()))


'''
A Soma da Idade dos 3 Filhos é igual a idade da Dona Mônica.

idades[0] é a da Mônica.
idades[1] e idades[2] é a dos seus filhos.

Logo a idade do terceiro filho é:
x = idades[0] - (sum(idades[1:]))

'''
#Faz a conta e adiciona a idade do terceiro filho na lista.
idades.append(idades[0] - (sum(idades[1:])))

#Mostra a idade do filho mais velho.
print(f'\nO filho mais velho tem: {max(idades[1:])}')

#Para fins de teste:

idades.sort() #Poem as idades em ordem e atualiza a lista.

dIdades = {0:'do mais novo', 1:'do meio', 2:'do mais velho', 3:'da Mônica'}

for i in range(4):
  print(f'\nA idade {dIdades[i]} é {idades[i]}')

del(dIdades)