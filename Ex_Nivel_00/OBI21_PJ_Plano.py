'''
Plano de Internet - Prova Fase 1 [PJ] – OBI2021

João conseguiu contratar um ótimo plano de Internet para o seu telefone celular.
O plano permite que João utilize uma quota de até X megabytes de dados por mês para navegar na
Internet. Se João não usa toda a sua quota no mês, os megabytes que ele não usou são adicionados
à quota do mês seguinte. Pelo contrato, João nunca pode usar mais megabytes do que a sua quota
corrente.

Por exemplo, se X = 200 megabytes e João usou 150 no primeiro mês e 220 megabytes no segundo
mês, então no terceiro mês João tem uma quota de 230 megabytes para usar (50 megabytes são
transferidos do primeiro para o segundo mês, 30 megabytes são transferidos do segundo para o
terceiro mês).

Nesta tarefa são dados o valor da quota mensal X e quantos megabytes João usou em cada um dos
primeiros N meses do plano. Você deve determinar quantos megabytes João tem para usar no mês
N + 1.

Entrada:
A primeira linha da entrada contém um número inteiro X, o valor da quota mensal em megabytes.
A segunda linha contém um inteiro N, o número de meses. Cada uma das linhas seguintes contém
um número inteiro Mi, indicando a quantidade de megabytes que João usou em cada mês, do mês
1 até o mês N.

Saída:
Seu programa deve produzir uma única linha, contendo um único número inteiro, a quantidade de
megabytes que João tem para usar no mês N + 1.

Exemplo 01:
Entrada: 100 - 2 - 50 - 120
Saída:   130

Exemplo 02:
Entrada: 10 - 3 - 4 - 6 - 2
Saída:   28

Exemplo 03:
Entrada: 100 - 2 - 100 - 100
Saída:   100

'''

quotaMensal  = int(input('Quota Mensal: '))

mesesConsumo = int(input('Meses de Consumo: '))

mgAcumulados = 0

for i in range(mesesConsumo):
  mgAcumulados += quotaMensal - int(input())

print("MegaBytes Acumulados: ", mgAcumulados+quotaMensal)
