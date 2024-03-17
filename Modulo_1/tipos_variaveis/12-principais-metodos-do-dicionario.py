# Criando um dicionario de exemplo
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Exibindo o dicionário
print("Meu dicionário de excemplo:", pessoa)


# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])
print("Meu dicionário de excemplo:", pessoa)

pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]

print("Meu dicionário de excemplo:", pessoa)

# Métodos: keys() = retorno de todas as chaves em formato de lista
# Métodos: values() = retorno de todos os valores em formato de lista
# Método: items() = retorna uma lista de tuplas contendo todos os pares chave-valor

# metodo keys()
chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0]) # não funciona porque não é uma lista direta, tem que transformar em lista

# metodo values
valores = list(pessoa.values())
print("Valores do dicionario:", valores)
print("Primeiro valor do dicionario:", valores[0])

# metodo items
itens = list(pessoa.items())
print("Pares chave-valor do dicionario:", itens)
print("Primeiro valor:", itens[0][1])
print(f"Primeiro chave-valor: {itens[0][0]} = {itens[0][1]}")