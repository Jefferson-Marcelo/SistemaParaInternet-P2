class Aluno:
    def __init__(self, nome, matricula):
        self.nome = str(nome)
        self.matricula = int(matricula)
        self.notas = []

    def _add_notas(self):
        numNotas = int(input('Quantas notas você deseja inserir? '))        
        for n in range(numNotas):
            n = float(input('Digite a {}ª nota: '.format(n+1)))
            self.notas.append(n)           

    def media(self):
        totalNotas = 0
        for i in range(len(self.notas)):
            totalNotas += i
        return totalNotas/len(self.notas)    

    def get_nome(self):
        return self.nome

    def __reduce__(self):
        return self.notas
    #def get_matricula(self):
    #    return f'A matricula do aluno {self.nome} é {self.matricula}'

aluno1 = Aluno('Jefferson', 20192370036)
aluno1._add_notas()
print(aluno1.media())

