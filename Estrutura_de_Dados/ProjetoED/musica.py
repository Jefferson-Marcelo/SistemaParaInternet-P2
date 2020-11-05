class Musica:
  def __init__(self, nome, banda, album, genero, anoLancado):
      self.nome = nome
      self.genero = genero
      self.banda = banda
      self.album = album
      self.anoLancado = anoLancado
  
  def __str__(self):
    return 'foo'

musica1 = Musica("faroeste", "legiao", "dois" , "rock", 2000 )
musica2 = Musica("caboclo", "legiao", "dois" , "rock", 2000 )


