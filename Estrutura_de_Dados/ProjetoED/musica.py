class Musica:
  def __init__(self):
      nome = input('digite o nome da música: ')
      banda = input('digite o nome da banda: ')
      album = input('digite o nome do album: ')
      genero = input('digite o nome do genero: ')
      anoLancado = input('digite o ano do Lançamento da música: ')

      self.nome = nome
      self.genero = genero
      self.banda = banda
      self.album = album
      self.anoLancado = anoLancado
  
  def __str__(self):
    return f'[{self.nome}, {self.genero}, {self.banda}, {self.album}, {self.anoLancado}]'

musica1 = Musica()
print(musica1)


