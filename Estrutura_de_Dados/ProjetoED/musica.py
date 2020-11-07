class Musica:
    def __init__(self, nome, banda, album, ano):
        self.__nome = nome
        self.__banda = banda
        self.__album = album
        self.__ano = ano

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome

    @property
    def banda(self):
        return self.__nome

    @banda.setter
    def banda(self, novaBanda):
        self.__nome = novaBanda

    @property
    def album(self):
        return self.__album

    @album.setter
    def album(self, novoAlbum):
        self.__album = novoAlbum

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, novoAno):
        self.__ano = novoAno

    def __repr__(self):
        return f'[{self.__nome}, {self.__banda}, {self.__album}, {self.__ano}]\n'
