# Criando um dicionário de exemplo
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Exibindo o dicionário
print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])

pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionário de exemplo:", pessoa)


# Métodos: keys(), values(), items()
chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

# Métodos values:
valores = list(pessoa.values())
print("Valores do dicionário:", valores)
print("Primeiro valore do dicionário:", valores[0])

# Métodos items
items = list(pessoa.items())
print("Pares chave-valor do dicionário:", items)
print("Primeiro valor", items[0][0])
print("Primeira chave-valor: %s = %s" % (items[0][0], items[0][1]))