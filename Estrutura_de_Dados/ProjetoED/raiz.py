from lista import ListaEncadeada
from musica import Musica

if __name__ == "__main__":
    lista = ListaEncadeada()

    with open("musicas.txt", "r") as arq:
        musicas = arq.readlines()

        for i in range(len(musicas)):
            nome, banda, album, ano = musicas[i].split(",")
            ano = ano.strip("\n")
            musica = Musica(nome, banda, album, ano)

            lista.inserir(i + 1, musica)

        print(lista)

        lista.ordena()

        print(lista)
