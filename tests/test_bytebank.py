from codigo.bytebank import Funcionario
import pytest


class TestClass:
    def test_quando_idade_recebe_13_03_200_deve_retorna_24(self):
        """ Teste na função idade """
        entrada = '13/03/2000' # contexto
        esperado = 24
        # Arrange
        Funcionario_test = Funcionario('teste',entrada,1111)
        # Assert / when-ção 
        resultado = Funcionario_test.idade( ) 

        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_carvalho_deve_retorn_carvalho(self):
        entrada = ' Lucas Carvalho '
        esperado = 'Carvalho'

        Funcionario_tes = Funcionario(entrada, '11/11/2000',2000)

        resultado = Funcionario_tes.sobrenome()

        assert resultado == esperado

    def test_quando_descrescimo_salario_recebe_100000_deve_retorna_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_tes = Funcionario(entrada_nome,'11/11/2000',entrada_salario)

        funcionario_tes.decrescimo_salario()

        resultado = funcionario_tes.salario

        assert resultado == esperado


