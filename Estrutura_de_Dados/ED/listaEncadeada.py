class ListaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Node:
    def __init__(self,dado):
        self.__dado = dado
        self.__prox = None


    @property
    def dado(self):
        return self.__dado

    @property
    def prox(self):
        return self.__prox

    @dado.setter
    def dado(self, novoDado):
        self.__dado = novoDado

    @prox.setter
    def prox(self, novoProx):
        self.__prox = novoProx

    def __str__(self):
        return str(self.__dado)

        
class Lista:


    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    def vazia(self):
        return True if self.__tamanho == 0 else False

  # def cheia(self):
  #     pass

    def tamanho(self):
        return self.__tamanho

    def busca(self, dado):
        if (self.vazia()):
            raise ListaException('A lista esta vazia')

        cursor = self.__head
        contador = 1

        while(cursor != None):
            if (cursor.dado == dado):
                return contador

            cursor = cursor.prox
            contador += 1
        
        raise ListaException('O valor informado na busca não esta na lista')

    def elemento(self,posicao):
        #valor negativo:
        #posição invalida (IndexError)
        #posição com o tipo de dado diferente de Int TypeError
        try:
            assert posicao > 0 #Assegure que posição é maior que zero
            if (self.vazia()):
                raise ListaException('A lista esta vazia')

            cursor = self.__head
            contador = 1

            while( (cursor != None) and (contador < posicao)):
                cursor = cursor.prox
                contador +=1

            if (cursor != None):
                return cursor.dado

            raise ListaException('A procição é invalido para a lista')
        
        except TypeError:
            raise ListaException('Coloque um número inteiro para fazer a busca')        
        except AssertionError:
            raise ListaException('Posição negativa não é valida para lista')
        except:
            raise


    def inserir(self, posicao, dado):
        try:
            assert posicao > 0
            #CONDIÇÃO 1: Inserção se a lista estiver vazia

            if (self.vazia()):
                if (posicao != 1):
                    raise('A lista esta vazia. Defina o argumento da posição como 1')
                self.__head = Node(dado)
                self.__tamanho +=1
                return
            
            #CONDIÇÃO 2: Inserção na primeira posição em uma lista vazia
            if (posicao == 1):
                novo = Node(dado)
                novo.prox =  self.__head
                self.__head = novo
                self.__tamanho +=1
                return

        except TypeError:
            raise ListaException('Coloque um número inteiro para fazer a busca')
        except IndexError:
            raise ListaException('Esse índice não esta na lista')
        except AssertionError:
            raise ListaException('Posição negativa não é valida para lista')
        except:
            raise


    def remover(self, posicao):
        try:
            assert posicao > 0
            if (self.vazia()):
                raise ListaException('Lista vazia. Não é possível remover elementos')
            valor = self.__head[posicao-1]
            del self.__head[posicao-1]
            return valor
        except TypeError:
            raise ListaException('Coloque um número inteiro para fazer a busca')
        except IndexError:
            raise ListaException('Esse índice não esta na lista')
        except AssertionError:
            raise ListaException('Posição negativa não é valida para lista')
        except:
            raise

    def __str__(self):
        return self.__head.__str__()

    def imprimir(self):
        print(self.__str__())

    def modificar(self, posicao, novoValor):
        try:
            assert posicao > 0
            if (self.vazia()):
                raise ListaException('Lista vazia. Não é possível modificar elementos')
            self.__head[posicao-1] = novoValor
            return True
        except TypeError:
            raise ListaException('Coloque um número inteiro para fazer a busca')
        except IndexError:
            raise ListaException('Esse índice não esta na lista')
        except AssertionError:
            raise ListaException('Posição negativa não é valida para lista')
        except:
            raise        
            
            
l1 = Lista()
if (l1.vazia()):
    print('lista vazia')

print('Tamanho: ', l1.tamanho())

for i in range(10):
    l1.inserir(1, i*10)
    print(l1)

print('Tamanho: ', l1.tamanho())

valorRemover = l1.remover(20)
print(valorRemover)
print(l1)

print()

l1.imprimir()

l1.modificar(3,7)

l1.imprimir()

#l1.inserir(-10,99)

#try:
#    #print(f'O indice do elemento que esta procurando se encontra na posição: {l1.busca(55)}')
#    #print(l1.elemento(5))
#    #l1.inserir(5,111)
#    #print(l1)
#    #l1.remover('1')
#    l1.modificar(100,999)
#    
#except ListaException as li:
#    print(li)