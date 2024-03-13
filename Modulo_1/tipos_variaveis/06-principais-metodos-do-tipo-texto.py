nome = "Gabriel"
sobrenome = "Casemiro"
nome_completo = "Gabriel Casemiro"

# obs: o valor das variáveis é imutável, os métodos só exibem o conteúdo delas e aplicam suas funcionalidades
# para alterar o valor da variável, apenas criando uma nova
print(nome.upper())
print(nome.lower())
print(nome[0])
print(nome_completo.count("a"))
print(nome_completo.find("a"))
# print(nome.encode()) # a string está decodificada em bytes
# print(nome.decode()) # decodifica pra o tipo texto comum

print(nome_completo.replace("b", "a"))
print(nome_completo.replace("a", "123"))

telefone = "(19)97325-0502"
print(telefone.replace("(", "").replace(")", "").replace("-", ""))
print("_".join("Gabriel"))
print(nome_completo.split())

nome_teste = "xGabriel Casemirox"
print(nome_teste.strip("x"))
print(nome_teste.rstrip("x"))
print(nome_teste.lstrip("x"))


print(nome_completo.startswith("Ga"))
print(nome_completo.startswith("Be"))

print("el" in nome_completo)
print("bra" in nome_completo)

print("el" not in nome_completo)
print("bra" not in nome_completo)