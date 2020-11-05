class ListaException(Exception):
  def __init__(self,mensagem):
    super().__init__(mensagem)

"""## **Classe Nó**"""

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

"""## **Classe Lista Encadeada**"""

class ListaEncadeada:
  def __init__(self):
    self.__head = None
    self.__tamanho = 0

  @property
  def head(self):
    return self.__head
  
  @head.setter
  def head(self, no):
    self.__head = no

  def vazia(self):
    return self.__tamanho == 0
  
  def tamanho(self):
    return self.__tamanho
  
  def busca(self, dado):
    if self.vazia():
      raise ListaException('A lista está vazia')

    p = self.__head
    contador = 1

    while p != None:
      if p.dado == dado:
        return contador
      
      p = p.prox
      contador += 1

    raise ListaException('O valor procurado não está na lista')
  
  def elemento(self, posicao):

    try:
      assert posicao > 0
      
      if self.vazia():
          raise ListaException('A lista está vazia')
      

      p = self.__head
      contador = 1

      # Andar na lista
      while p != None and contador < posicao:
        p = p.prox
        contador += 1
      
      # Posição encontrada
      if p != None:
        return p.dado
      
      raise ListaException('A posição é inválida')
    
    except TypeError:
      raise ListaException('A posição deve ser um valor inteiro')
    except AssertionError:
      raise ListaException('Posição negativa não é válida')
    except:
      raise

  def inserir(self, posicao, dado):
    try:
      assert posicao > 0

      # CONDIÇÃO 1: Inserção se a lista estiver vazia
      if self.vazia():
        if posicao != 1:
          raise ListaException('A lista está vazia. Só poderá ser inserido na posição 1')

        self.__head = Node(dado)
        self.__tamanho += 1
        return
      
      # CONDIÇÃO 2: Inserção na primeira posição em uma lista não vazia
      if posicao == 1:
        novo = Node(dado)
        novo.prox = self.__head
        self.__head = novo
        self.__tamanho += 1
        return

      # CONDIÇÃO 3: Inserção após a primeira posição em uma lista não vazia
      p = self.__head
      contador = 1
      
      while (contador < posicao-1) and (p != None):
        p = p.prox
        contador += 1

      if p == None:
        raise ListaException('A posição é inválida para inserção')
      
      novo = Node(dado)
      novo.prox = p.prox
      p.prox = novo
      self.__tamanho += 1

    except TypeError:
      raise ListaException('A posição deve ser um valor inteiro')
    except AssertionError:
      raise ListaException('Posição negativa não é válida')
    except:
      raise

  def remover(self, posicao):
    try:
      assert posicao > 0

      if self.vazia():
        raise ListaException('Lista vazia. Não é possível remover elementos')

      p = self.__head
      contador = 1

      while (contador <= posicao-1) and (p != None):
        anterior = p
        p = p.prox
        contador += 1
      
      if p == None:
        raise ListaException('Posição inválida para remoção')
      
      dado = p.dado

      if posicao == 1:
        self.__head = p.prox
      
      else:
        anterior.prox = p.prox

    except TypeError:
      raise ListaException('A posição deve ser um valor inteiro')
    except AssertionError:
      raise ListaException('Posição negativa não é válida')
    except:
      raise
  
  def __str__(self):
    saida = 'Lista: ['
    p = self.__head

    while p != None:
      saida += f'{p.dado}'
      p = p.prox

      if p != None:
        saida += ', '
    
    saida += ']'
    return saida

  def imprimir(self):
    print(self.__str__())

  def modificar(self, posicao, novoValor):
    try:
      assert posicao > 0

      if self.vazia():
        raise ListaException('Lista vazia. Não é possível remover elementos')

      p = self.__head
      contador = 1

      while (p != None) and (contador < posicao):
        p = p.prox
        contador += 1
      
      if p != None:
        p.dado = novoValor
        return
      
      raise ListaException('Posição inválida para a lista')

    except TypeError:
      raise ListaException('A posição deve ser um valor inteiro')
    except AssertionError:
      raise ListaException('Posição negativa não é válida')
    except:
      raise

if __name__ == '__main__':
  lista = ListaEncadeada()
  lista.inserir(1,10)
  lista.inserir(1,20)
  lista.inserir(1,30)

  print(lista)

  # Inserir o valor 5 entre 30 e 20
  lista.inserir(2,5)
  print(lista)

  # Inserir o valor 12 na última posição
  lista.inserir(5,12)
  print(lista)

  # Modificar o valor da posição 3 (20), para 25
  lista.modificar(3,25)
  print(lista)

  # Remover o elemento da última posição
  lista.remover(5)
  print(lista)

  # Remover o elemento da posição 2
  lista.remover(2)
  print(lista)

  # Remover o elemento da posição 100 ==> ERRO ==> COMPLETE O CÓDIGO PARA TRATAR A EXCEÇÃO
  lista.remover(100)
  print(lista)