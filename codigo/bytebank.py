from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def funcionario_is_diretor(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return ((self.sobrenome() in sobrenomes) and (self._salario >= 10000)  )

    def decrescimo_salario(self):
        if  (self.funcionario_is_diretor()):
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo
             
    

    def sobrenome(self):
        nome_completo = self._nome.strip()
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'