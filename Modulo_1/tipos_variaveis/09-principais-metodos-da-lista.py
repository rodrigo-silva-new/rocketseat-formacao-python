# Declaracao
minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# Exibindo a lista
print("Minha lista de exemplo", minha_lista)

# Exibindo os elementos
minha_lista[0] = "python"
print("Minha lista de exemplo", minha_lista)

print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7])
print("minha_lista[:6]:" ,minha_lista[:6])
print("minha_lista[2:]:" ,minha_lista[2:])

# Métodos de lista

# Método append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Apos append(6):", minha_lista)

# Método index
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

# Método insert: Insere um elemento em um indice especifico
minha_lista.insert(2, 10)
print("Apos o insert(2, 10):", minha_lista)

# Método pop: remove e retorna o elemento de um indice especifico
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Apos pop(3):", minha_lista)

# Método remove: remove o primeiro elemento ou o valor especificado
minha_lista.remove(True)
print("Após remover(True)", minha_lista)

# Método sort: organizar a lista
minha_lista.sort()
print("Após sort()", minha_lista)