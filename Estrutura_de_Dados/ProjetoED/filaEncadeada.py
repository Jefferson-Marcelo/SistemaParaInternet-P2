import node, exception


class FilaEncadeada:
  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
      if self.vazia():
        raise exception.Exception('A fila está vazia')

      return self.__head

  def vazia(self):
    return self.__size == 0
  
  def size(self):
    return self.__size
  
  def inserir(self, data):
    createNode = node.Node(data)
    if self.vazia():
      self.__head = createNode
      self.__tail = createNode        
    
    self.__tail.next = createNode
    self.__tail = createNode 
    self.__size +=1 
     

  def remover(self):
    if self.vazia():
      raise exception.Exception('A fila está vazia')

    self.__head = self.__head.next
    self.__size -=1 
    return

     
  def __str__(self):
    saida = 'Fila: ['
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
  




