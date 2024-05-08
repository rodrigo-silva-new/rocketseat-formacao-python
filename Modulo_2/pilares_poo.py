# Exemplo de herança
print("\nExemplo de herança: ")
class Animal:
  def __init__(self, nome) -> None:
    self.nome = nome

  def andar(self):
    print(f"O animal {self.nome} andou")
    return
  
  def emitir_son(self):
    pass

class Cachorro(Animal):
  def emitir_son(self):
    return "Au, au"
  
class Gato(Animal):
  def emitir_son(self):
    return "Miau!"