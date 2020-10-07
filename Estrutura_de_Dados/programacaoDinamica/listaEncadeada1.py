class Node:
    def __init__(self, date):
        self.date = date
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            #inserção quando a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            #primeira inserção
            self.head = Node(elem)
        self._size += 1

    def __len__(self):
        #retorna o tamanho da lista
        return self._size
    def get(self,index):
        pass
    def set(self, index, elem):
        pass
    def __getitem__(self, index):
        # a = lista[6]
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        # lista[5] = 9
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

        

        


lista = LinkedList()
lista.append(7)
lista.append(80)
lista.append(56)
print(len(lista))
print(lista[0])


