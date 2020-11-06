class Musica:
  def __init__(self):
      self.nome = input('digite o nome da música: ')
      self.banda = input('digite o nome da banda: ')
      self.album = input('digite o nome do album: ')
    #  self.genero = input('digite o nome do genero: ')
    #  self.anoLancado = input('digite o ano do Lançamento da música: ')
 
  def __str__(self):
    return f'[{self.nome}, {self.banda}, {self.album}]'    
#    return f'[{self.nome}, {self.genero}, {self.banda}, {self.album}, {self.anoLancado}]'
  
  def asdict(self):
    return {'nome': self.nome, 'banda': self.banda, 'album': self.album}

# print(musica1)

musica1 = Musica()
musica1 = musica1.asdict()

print(musica1)
print(sorted(musica1))