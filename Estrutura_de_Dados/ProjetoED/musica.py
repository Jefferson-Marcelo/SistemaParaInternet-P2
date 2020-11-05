

class Musica:
  def __init__(self):
    inserir_musica = False
    rodar_programa = True

    while rodar_programa:
      print("Olá, bem vindo, selecione um opção:")
      print("1 - Inserir Música")
      print("2 - Encerrar Programa")
      decisao = str(input("Digite sua decisão: "))
      if decisao == '1':
        inserir_musica = True
      elif decisao == '2':
        inserir_musica = False
        rodar_programa = False
      else:
        print("Decisão Inválida.")

      if inserir_musica:
        while inserir_musica:
          self.nome = input('digite o nome da música: ')
          self.banda = input('digite o nome da banda: ')
          self.album = input('digite o nome do album: ')
          self.genero = input('digite o nome do genero: ')
          self.anoLancado = input('digite o ano do Lançamento da música: ')

          listar = input(f"Deseja inserir mais alguma música? (S/N).").upper()
          if listar == 'S':
            inserir_musica = True
          elif listar == 'N':
            inserir_musica = False
          else:
            validade = False
            while not validade:
              perguntar = input("Input inválido, Deseja inserir mais um música?").upper()
              if perguntar == 'S':
                validade = True
              else:
                validade = False
        else:
          print(f'Programa encerrado.')


 
  def __str__(self):
    return f'[{self.nome}, {self.genero}, {self.banda}, {self.album}, {self.anoLancado}]'

musica1 = Musica()
print(musica1)


