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