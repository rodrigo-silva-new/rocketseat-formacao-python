# Exemplo
def saudacao(nome):
  print(f"Olá, {nome}!")

print("\nChamando a função sauadção:")
saudacao("Alice")
saudacao("Bob")




# Funcao com retorno
def quadrado(numero):
  resultado = numero ** 2
  return resultado

print("\nChamando a função quadrado:")
resultado_quadrado = quadrado(6)
print("Resultado da funcao quadrado:", resultado_quadrado)








# Funcao com multiplos parametros
def soma(numero1, numero2):
  resultado = numero1 + numero2
  return resultado

print("\nChamando a funcao soma:")
numero1 = 20
numero2 = 50
resultado_soma = soma(numero1, numero2)
print(f"A soma do numero {numero1} e numero {numero2} é", resultado_soma)