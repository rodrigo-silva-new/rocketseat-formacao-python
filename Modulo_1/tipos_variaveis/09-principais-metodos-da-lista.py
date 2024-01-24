# Declaração

minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# Exibindo a lista
print("Minha lista de exemplo", minha_lista)

# Exibindo a lista
minha_lista[0] = "python"
print("Minha lista de exemplo", minha_lista)

print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7])
print("minha_lista[:6]:", minha_lista[:6])
print("minha_lista[2:]:", minha_lista[2:])

# Métodos de lista:

# Método append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Apos append(6):", minha_lista)

# Método index
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

# Método insert: Insere um elemento em um indice especifico
minha_lista.insert(2, 10)
print("Apos o insert(2, 10):", minha_lista)

# Método pop
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Apos pop(3):", minha_lista)

# Método remove
minha_lista.remove(True)
print("Apos remove(True)", minha_lista)

# Metodo sort()
lista_numerica = [1, 10, 3, 3, 5, 6, 7, 8, 112]

lista_numerica.sort()
print("Apos sort()", lista_numerica)