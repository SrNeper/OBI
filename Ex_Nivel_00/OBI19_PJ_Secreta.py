qtNumeros = int(input('Quantos nº são? \t')) 

n = 0
check = 0
marcados = 0

#Começa a anotar os nº.
for i in range(qtNumeros):
  n = int(input(f'{i+1}º n: \t'))

  #Sempre que o nº for diferente do ultimo
  if n != check:
    # 'Marcamos' ele e guardamos em check.
    marcados += 1
    check = n

print(f"Total de Numeros Marcados: {marcados}")

