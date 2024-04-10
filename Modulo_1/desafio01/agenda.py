def adiciona_contato(contatos, nome_contato, telefone_contato, email_contato):
  contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
  contatos.append(contato)
  return

def ver_contatos(contatos):
  print("\nLista de contatos:")
  for indice, contato in enumerate(contatos, start=1):
    nome_contato = contato["nome"]
    telefone_contato = contato["telefone"]
    email_contato = contato["email"]
    favorito = "★ " if contato["favorito"] else ""
    print(f"{favorito}{indice}. {nome_contato} - Telefone: {telefone_contato} - E-mail: {email_contato}")

def editar_contato(contatos, indice_contato):
  indice = int(indice_contato) - 1
  while True:
    print("\n1. Nome")
    print("2. Telefone")
    print("3. E-mail")
    print("4. Encerrar edição de contato")

    escolha = input("Qual informação deseja editar: ")

    if escolha == '1':
      novo_nome = input("Digite o novo nome: ")
      contatos[indice]["nome"] = novo_nome
    elif escolha == '2':
      novo_telefone = input("Digite o novo telefone: ")
      contatos[indice]["telefone"] = novo_telefone
    elif escolha == '3':
      novo_email = input("Digite o novo e-mail: ")
      contatos[indice]["email"] = novo_email
    elif escolha == '4':
      print("Edição de contato encerrada!")
      break

def favoritos(contatos):
  while True:
    print("\n1. Favoritar contato")
    print("2. Remover contato dos favoritos")
    print("3. Ver contatos")
    print("4. Encerrar")

    escolha = int(input("Digite a opção que deseja: "))

    if escolha == 1:
      ver_contatos(contatos)
      indice_contato = int(input("Digite o número do contato que deseja favoritar: "))
      contatos[indice_contato - 1]["favorito"] = True
      print("Contato favoritado com sucesso")
    elif escolha == 2:
      ver_contatos(contatos)
      indice_contato = int(input("Digite o número do contato que deseja remover de favoritos: "))
      contatos[indice_contato - 1]["favorito"] = False
      print("Contato removido dos favoritos com sucesso")
    elif escolha == 3:
      ver_contatos(contatos)
    elif escolha == 4:
      break

def ver_favoritos(contatos):
  print("\nLista de favoritos:")
  for indice, contato in enumerate(contatos, start=1):
    if contato["favorito"] == True:
      print(contato)

def apagar_contato(contatos, indice_contato):
  contato_excluir = indice_contato

  for indice, contato in enumerate(contatos, start=1):
    if indice == contato_excluir:
      contatos.remove(contato)
  print("Contato apagado com sucesso!")
      

contatos = []

while True:
  print("\n1. Adicionar um contato")
  print("2. Ver lista de contatos")
  print("3. Editar um contato")
  print("4. Adicionar ou remover de favoritos")
  print("5. Ver lista de favoritos")
  print("6. Apagar um contato")
  print("7. Fechar agenda")
  
  opcao = input("\nDigite qual opção deseja utilizar: ")

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
  elif opcao == "4":
    ver_contatos(contatos)
    favoritos(contatos)
  elif opcao == "5":
    ver_favoritos(contatos)
  elif opcao == "6":
    ver_contatos(contatos)
    indice_contato = int(input("\nDigite o contato que quer excluir: "))
    apagar_contato(contatos, indice_contato)
  elif opcao == "7":
    break