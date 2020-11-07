from listaEncadeada import ListaEncadeada
from pilhaEncadeada import PilhaEncadeada
from musica import Musica
from modulo.shutil import print_centralizado

if __name__ == "__main__":
    print_centralizado('Início da classe Lista Encadeada.')
    print_centralizado('Serão ADICIONADOS todos os dados sobre as músicas a seguir.')
    input("\nPressione ENTER para continuar...")


############################### LISTA ENCADEADA

    lista = ListaEncadeada()

    with open("musicas.txt", "r", encoding="utf8") as arq:
        musicas = arq.readlines()
        for i in range(len(musicas)):
            colocacao, nome, banda, compositor, ano = musicas[i].split(";")
            ano = ano.strip("\n")
            musica = Musica(colocacao, nome, banda, compositor, ano)
            lista.inserir(i + 1, musica)
        print(lista)

    print_centralizado('Inserção completa. Próximo passo: REMOÇÃO.')
    print_centralizado('A remoção será feita, respectivamente, nas posicoes: 1, 51 e 5')
    input("\nPressione ENTER para continuar...")

    lista.remover(51)
    lista.remover(5)
    lista.remover(1)

    print(lista)

    print_centralizado('Remoção completa. Próximo passo: Checar se está vazio, caso não, imprimir o tamanho.')
    input("\nPressione ENTER para continuar...")

    if lista.vazia():
        print_centralizado('A lista está vazia.')
    else:
        print_centralizado(f'A lista possui tamanho: {lista.tamanho()}')
        print_centralizado('A lista NÃO está vazia')

    print_centralizado('Checagem completa. Próximo passo: MOSTRAR ELEMENTO')
    print_centralizado('Será mostrado o elemento 7')
    input("\nPressione ENTER para continuar...")

    print_centralizado(f'{lista.elemento(7)}')

    print_centralizado('Elemento mostrado. Próximo passo: ORDENAR')
    print_centralizado('A ordenação será feita pelo ano de lançamento')
    input("\nPressione ENTER para continuar...")

    lista.ordena()
    print(lista)

    print_centralizado('Elemento mostrado. Próximo passo: BUSCAR')
    print_centralizado('Serão buscadas as músicas do cantor Geraldo Vandré')
    input("\nPressione ENTER para continuar...")

    print_centralizado(f'{lista.buscar("Geraldo Vandré")}')

    print_centralizado('Busca feita. FIM DA LISTA ENCADEADA. Próximo passo: PILHA')
    input("\nPressione ENTER para continuar...")

############################### PILHA ENCADEADA


    # print_centralizado('Início da classe Pilha Encadeada.')
    # print_centralizado('Serão ADICIONADOS os dados das primeiras 5 músicas.')
    # input("\nPressione ENTER para continuar...")

    # pilha = PilhaEncadeada()

    # with open("musicas.txt", "r", encoding="utf8") as arq:
    #     musicas = arq.readlines()
    #     for i in range(5):
    #         colocacao, nome, banda, compositor, ano = musicas[i].split(";")
    #         ano = ano.strip("\n")
    #         musica = Musica(colocacao, nome, banda, compositor, ano)
    #         pilha.inserir(i, musica)
    #         i += 1
    #     print(pilha)

    # print_centralizado('Inserção completa. Próximo passo: REMOÇÃO.')
    # print_centralizado('A remoção será feita, respectivamente, nas posicoes: 1, 51 e 5')
    # input("\nPressione ENTER para continuar...")

    # pilha.remover(51)
    # pilha.remover(5)
    # pilha.remover(1)

    # print(pilha)

    # print_centralizado('Remoção completa. Próximo passo: Checar se está vazio, caso não, imprimir o tamanho.')
    # input("\nPressione ENTER para continuar...")

    # if pilha.vazia():
    #     print_centralizado('A pilha está vazia.')
    # else:
    #     print_centralizado(f'A pilha possui tamanho: {pilha.tamanho()}')
    #     print_centralizado('A pilha NÃO está vazia')

    # print_centralizado('Checagem completa. Próximo passo: MOSTRAR ELEMENTO')
    # print_centralizado('Será mostrado o elemento 7')
    # input("\nPressione ENTER para continuar...")

    # print_centralizado(f'{pilha.elemento(7)}')

    # print_centralizado('Elemento mostrado. Próximo passo: ORDENAR')
    # print_centralizado('A ordenação será feita pelo ano de lançamento')
    # input("\nPressione ENTER para continuar...")

    # pilha.ordena()
    # print(Pilha)

    # print_centralizado('Elemento mostrado. Próximo passo: BUSCAR')
    # print_centralizado('Serão buscadas as músicas do cantor Geraldo Vandré')
    # input("\nPressione ENTER para continuar...")

    # print_centralizado(f'{Pilha.buscar("Geraldo Vandré")}')

    # print_centralizado('Busca feita. FIM DA LISTA ENCADEADA. Próximo passo: PILHA')
    # input("\nPressione ENTER para continuar...")