class Musica:
  def __init__(self):
      self.nome = input('digite o nome da música: ')
      self.banda = input('digite o nome da banda: ')
      self.album = input('digite o nome do album: ')
      self.genero = input('digite o nome do genero: ')
      self.anoLancado = input('digite o ano do Lançamento da música: ')
 
  def __str__(self):
    return f'[{self.nome}, {self.genero}, {self.banda}, {self.album}, {self.anoLancado}]'

musica1 = Musica()
print(musica1)

