from pytest import mark, raises
from typer.testing import CliRunner

from src.notas_musicais.cli import app  # , escalas_cli

runner = CliRunner()


def test_escala_cli_deve_retornar_0_ao_stdout():

    # runner.invoke(escalas_cli)
    result = runner.invoke(app)
    assert result.exit_code == 0


@mark.parametrize('nota', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_escala_cli_deve_conter_as_notas_na_resposta(nota):
    result = runner.invoke(app)
    assert nota in result.stdout  # stdout --> Resultado mostrado no terminal


@mark.parametrize('nota', ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])
def test_escala_cli_deve_conter_as_notas_na_resposta_de_fa(nota):
    result = runner.invoke(app, ['F'])
    assert nota in result.stdout  # stdout --> Resultado mostrado no terminal


@mark.parametrize('grau', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_escala_cli_deve_conter_os_graus_na_resposta(grau):
    result = runner.invoke(app)
    assert grau in result.stdout  # stdout --> Resultado mostrado no terminal
