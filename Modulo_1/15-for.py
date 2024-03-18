print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
  print(elemento)

print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
  print(elemento)

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print("\nFor utilizando dicionario - chaves")
for chave in pessoa.keys():
  print(chave)

print("\nFor utilizando dicionario - valores")
for valor in pessoa.values():
  print(valor)

print("\nFor utilizando dicionario - items")
for chave, valor in pessoa.items():
  print(f"{chave}: {valor}")








# range(): intervalo numerico
# print(list(range(0, 10)))
  
print("\nUtilizando a função range()")
for numero in range(5):
  print("Numero:", numero)


print("\nUtilizando a função range() com len()")
lista2 = [1, 2, 3, 4, 5]
print(lista2)
for indice in range(0, len(lista2)):
  if indice == 3:
    lista2[indice] = 5
  else:
    lista2[indice] = 0
print(lista2)





# enumarate() permite que use uma lista pra extrair o valor e o indice desse valor
print("\nLista enumerate:")
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
  print(f"{indice}: {valor}")
  if indice == 1:
    print("Indice 1 acima")