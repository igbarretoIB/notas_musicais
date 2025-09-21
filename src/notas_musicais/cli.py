# from rich import print
from rich.console import Console
from rich.table import Table
from typer import Argument, Typer, run

from src.notas_musicais.escalas import escalas

HELP_TONICA = 'Tônica da Escala'

HELP_TONALIDADE = 'Tonalidade da Escala'


console = Console()
app = Typer()


@app.command()
def escalas_cli(
    tonica=Argument('C', help=HELP_TONICA),
    tonalidade=Argument('maior', help=HELP_TONALIDADE),
):
    escala = escalas(tonica, tonalidade)
    notas, graus = escala.values()

    table = Table()

    for grau in graus:
        table.add_column(grau)

    table.add_row(*notas)
    console.print(escalas(tonica, tonalidade))
    print(' ')
    console.print(table)


# run(escalas_cli)
