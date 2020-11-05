class Data:
    def __init__(self, dia, mes, ano):
        self._dia = dia
        self._mes = mes
        self._ano = ano

    def get_dia(self):
        return self._dia

    def get_mes(self):
        return self._mes

    def get_ano(self):
        return self._ano

    def set_dia(self, dia):
        self._dia = dia

    def set_mes(self, mes):
        self._mes = mes
    
    def set_ano (self, ano):
        self._ano = ano

    def __str__(self):
        return f'A data com o formado dd/mm/aaaa ficou: {self._dia}/{self._mes}/{self._ano}'

dia = int(input('Digite o dia apenas com dois digitos: '))
mes = int(input('Digite o mes apenas com dois digitos: '))
ano = int(input('Digite o ano apenas com quatro digitos: '))

data1 = Data(dia, mes, ano)
print(data1)