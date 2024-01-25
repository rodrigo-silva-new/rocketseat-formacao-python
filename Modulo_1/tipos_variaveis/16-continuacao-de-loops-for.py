print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
  print(elemento)

print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
  print(elemento)

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print("For utilizando dicionário - chaves")
for chave in pessoa.keys():
  print(chave)

print("For utilizando dicionário - valores")
for valor in pessoa.values():
  print(valor)

print("For utilizando dicionário - items")
for chave, valor in pessoa.items():
  print(f"{chave}: {valor}")




# range(): intervalo numérico
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nUtilizando a função range()")
for numero in range(5):
  print("Número:", numero)

print("\nUtilizando a função range() com len()")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
  if indice == 3:
    lista[indice] = 5
  else:
    lista[indice] = 0

# enumarate()
lista_enumarate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumarate):
  print(f"{indice}: {valor}")