class PilhaException(Exception):
  def __init__(self,mensagem):
    super().__init__(mensagem)


class Node:
  def __init__(self, dado = None):
    self.__dado = dado
    self.__prox = None
  
  # get
  @property
  def dado(self):
    return self.__dado
  
  # set
  @dado.setter
  def dado(self, novo):
    self.__dado = novo

  # get
  @property
  def prox(self):
    return self.__prox
  
  # set
  @prox.setter
  def prox(self, novo):
    self.__prox = novo


class PilhaEncadeada:
  def __init__(self):
    self.__topo = None
    self.__tamanho = 0

  @property
  def topo(self):
      if self.vazia():
        raise PilhaException('A pilha está vazia')

      return self.__topo

  def vazia(self):
    return self.__tamanho == 0
  
  def tamanho(self):
    return self.__tamanho
  
  def inserir(self, dado):
    no = Node(dado)
    no.prox = self.__topo
    self.__topo = no

    self.__tamanho += 1  

  def remover(self):
      if self.vazia():
        raise PilhaException('A pilha está vazia')

      self.__topo = self.__topo.prox
      self.__tamanho -= 1  
  
  def __str__(self):
    saida = 'Pilha: ['
    p = self.__topo

    while p != None:
      saida += f'{p.dado}'
      p = p.prox

      if p != None:
        saida += ', '
    
    saida += ']'
    return saida

  def imprimir(self):
    print(self.__str__())

  def modificar(self, novoValor):
      if self.vazia():
        raise PilhaException('A pilha está vazia')
      
      self.__topo.dado = novoValor


p = PilhaEncadeada()

p.inserir(10)
p.inserir(20)
p.inserir(30)
p.inserir(40)
print(p)
p.remover()
print(p)
p.remover()
print(p)

