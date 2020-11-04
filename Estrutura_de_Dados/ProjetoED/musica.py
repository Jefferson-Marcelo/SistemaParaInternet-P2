class Musica:
  def __init__(self, nome, banda, album, genero, anoLancado):
      self.nome = nome
      self.genero = genero
      self.banda = banda
      self.album = album
      self.anoLancado = anoLancado
      


musica1 = Musica("faroeste", "legiao", "dois" , "rock", 2000 )
musica2 = Musica("caboclo", "legiao", "dois" , "rock", 2000 )



#print(musica1.nome)
#print(musica2.nome)



      # self.nome = input("Digite o nome da música: ")
      # self.genero = input("Digite o gênero: ")
      # self.banda = input("Digite o nome da banda: ")
      # self.album = input("Digite o nome do albúm: ")
      # self.anoLancado = input("Digite o ano de lançamento: ")
