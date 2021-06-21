'''
A idade de Camila - Prova Fase 1 [PJ] – OBI2021

Cibele, Camila e Celeste são três irmãs inseparáveis. Estão
sempre juntas e adoram fazer esportes, ler, cozinhar, jogar no
computador... Agora estão aprendendo a programar computadores
para desenvolverem seus próprios jogos.

Mas nada disso interessa para esta tarefa: estamos interessados
apenas nas suas idades. Sabemos que Cibele nasceu antes de
Camila e Celeste nasceu depois de Camila. Dados três números
inteiros indicando as idades das irmãs, escreva um
programa para determinar a idade de Camila.

Entrada:

A entrada é composta por três linhas, cada linha contendo um
número inteiro N, a idade de uma das irmãs.

Saída:

Seu programa deve produzir uma única linha, contendo um único
número inteiro, a idade de Camila.

Exemplo 01:
Entrada: 16 - 9 - 7
Saída: 7

Exemplo 02:
Entrada: 34 - 36 - 38
Saída: 36

Exemplo 03:
Entrada: 22 - 25 - 22
Saída: 22

Exemplo 04:
Entrada: 91 - 91 - 91
Saída: 91

'''
idades = []

for i in range(3):
  #idades.append(int(input(f'Digite a idade {i+1}: \n')))
  idades.append(int(input()))


#Organiza os valores em ordem crescente
#exibi o que estiver no meio da lista.
print(sorted(idades)[1])
