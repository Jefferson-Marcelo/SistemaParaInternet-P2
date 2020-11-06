import musica


class Node:
  def __init__(self, data = None):    
    self.__data = data
    self.__next = None
  
  # get
  @property
  def data(self):
    return self.__data
  
  # set
  @data.setter
  def data(self, newData):
    self.__data = newData

  # get
  @property
  def next(self):
    return self.__next
  
  # set
  @next.setter
  def next(self, newData):
    self.__next = newData

# no1 = Node(musica.musica1)
#print(no1.data.nome)
#print(no1.data)