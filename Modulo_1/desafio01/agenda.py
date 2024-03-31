def adiciona_contato(contatos, nome_contato, telefone_contato, email_contato):
  contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
  contatos.append(contato)
  return

def ver_contatos(contatos):
  print("\nLista de contatos:")
  for indice, contato in enumerate(contatos, start=1):
    nome_contato = contato["nome"]
    print(f"{indice}. {nome_contato}")

def editar_contato(contatos, indice_contato):
  indice = int(indice_contato)
  while True:
    print("\n1. Nome")
    print("2. Telefone")
    print("3. E-mail")
    print("4. Encerrar edição de contato")

    escolha = input("Qual informação deseja editar: ")

    if escolha == 1:
      novo_nome = input("Digite o novo nome: ")
      contatos[indice]["nome"] = novo_nome
    elif escolha == 2:
      novo_telefone = input("Digite o novo telefone: ")
      contatos["telefone"] = novo_telefone
    elif escolha == 3:
      novo_email = input("Digite o novo e-mail: ")
      contatos["email"] = novo_email
    elif escolha == 4:
      print("Edição de contato encerrada!")
      break

    print(contatos)

contatos = []
favoritos = []

while True:
  print("\n1. Adicionar um contato")
  print("2. Ver lista de contatos")
  print("3. Editar um contato")
  print("4. Adicionar ou remover de favoritos")
  print("5. Ver lista de favoritos")
  print("6. Apagar um contato")
  print("7. Fechar agenda")
  
  opcao = input("Digite qual opção deseja utilizar: ")

  if opcao == "1":
    nome_contato = input("Digite o nome do contato: ")
    telefone_contato = input("Digite o telefone do contato: ")
    email_contato = input("Digite o e-mail do contato: ")
    adiciona_contato(contatos, nome_contato, telefone_contato, email_contato)
    print(f"\nContato {nome_contato} adicionado.")
  elif opcao == "2":
    ver_contatos(contatos)
  elif opcao == "3":
    ver_contatos(contatos)
    indice_contato = input("Digite o índice do contato que deseja editar: ")
    editar_contato(contatos, indice_contato)
  elif opcao == "7":
    break