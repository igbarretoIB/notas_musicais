"""
TESTES AAA(3A)

- Arrange → Organizar

- Act → Agir

- Assert → Garantir
"""
from pytest import mark, raises

from src.notas_musicais.escalas import ESCALAS, NOTAS, escalas

### TESTE:


def test_deve_funcionar_com_notas_minusculas():
    # Arrange
    tonica = 'c'
    tonalidade = 'maior'

    # Act
    result = escalas(tonica, tonalidade)

    # assert
    assert result


def test_deve_retornar_uma_erro_dizendo_que_a_nota_não_existe():
    # Arrange
    tonica = 'X'
    tonalidade = 'maior'
    mensagem_de_erro = f'Essa nota não existe! Tente uma dessas:\n{NOTAS}'

    # Act
    with raises(ValueError) as error:
        result = escalas(tonica, tonalidade)
        print(error)

    # assert
    # assert False #(pytest --pdb)
    print(error)
    print(error.value.args[0])

    assert mensagem_de_erro == error.value.args[0]
    # assert result


def test_deve_retornar_uma_erro_dizendo_que_a_escala_não_existe():
    tonica = 'C'
    tonalidade = 'grauda'
    mensagem_de_erro = f'Essa escala não existe ou não foi implementada! Tente uma dessas:\n{list(ESCALAS.keys())}'

    with raises(KeyError) as error2:
        result = escalas(tonica, tonalidade)

    print(error2.value.args[0])
    assert mensagem_de_erro == error2.value.args[0]


# Arrange
@mark.parametrize(
    'tonica, tonalidade, esperado',
    [
        ('C', 'maior', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', 'maior', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', 'maior', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def deve_retornar_as_notas_corretas(tonica, tonalidade, esperado):

    # Act
    result = escalas(tonica, tonalidade)

    # Assert
    assert result['notas'] == esperado


def test_deve_retornar_os_sete_graus():

    # Arrange
    tonica = 'C'
    tonalidade = 'maior'
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    # Act
    result = escalas(tonica, tonalidade)

    # Assert
    assert result['graus'] == esperado
