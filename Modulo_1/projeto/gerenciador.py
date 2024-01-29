def adicionar_tarefa(tarefas, nome_tarefa):

  # tarefa: nome da tarefa
  # completada: indicar se essa tarefa já foi completada ou não
  tarefa = {"tarefa": nome_tarefa, "completada": False}
  tarefas.append(tarefa)
  print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
  return

tarefas = []
while True:
  print("\nMenu do gerenciador de lista de tarefas:")
  print("1. Adicionar uma Tarefa")
  print("2. Ver Tarefas")
  print("3. Atualizar Tarefa")
  print("4. Completar Tarefa")
  print("5. Deletar tarefas completadas")
  print("6. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
    adicionar_tarefa(tarefas, nome_tarefa)
  elif escolha == "6":
    break

print("Programa finalizado")