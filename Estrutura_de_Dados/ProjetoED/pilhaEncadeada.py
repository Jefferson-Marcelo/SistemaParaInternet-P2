from node import Node
from modulo.exception import Exception
import musica

class PilhaEncadeada:
  def __init__(self):
    self.__head = None
    self.__tamanho = 0

  @property
  def head(self):
      if self.vazia():
        raise exception.Exception('A pilha está vazia')

      return self.__head

  def vazia(self):
    return self.__tamanho == 0
  
  def tamanho(self):
    return self.__tamanho
  
  def inserir(self, dado):
    no = node.Node(dado)
    no.next = self.__head
    self.__head = no

    self.__tamanho += 1  

  def remover(self):
      if self.vazia():
        raise exception.Exception('A pilha está vazia')

      self.__head = self.__head.next
      self.__tamanho -= 1  
  
  def __str__(self):
    saida = 'Pilha: ['
    p = self.__head

    while p != None:
      saida += f'{p.data}'
      p = p.next

      if p != None:
        saida += ', '
    
    saida += ']'
    return saida

  def imprimir(self):
    print(self.__str__())

  def modificar(self, novoValor):
      if self.vazia():
        raise exception.Exception('A pilha está vazia')
      
      self.__head.dado = novoValor