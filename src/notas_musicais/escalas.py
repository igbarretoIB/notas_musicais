config_dict = {
    'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
}
NOTAS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escalas(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala apartir de uma nota tônica e uma tonalidade

    Parameters:
        tonica: Nota que será a tônica da escala
        tonalidade: Tonalidade da escala

    Returns:
        Retorna um dicionário com as notas e as tonalidades

    Raises:
        ValueError: Caso a tônica não seja uma nota válida

        KeyError: Caso a escala não seja uma escala válida

    Examples:
        >>> escalas('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escalas('C#', 'maior')
        {'notas': ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escalas('a', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escalas('c#', 'maior')
        {'notas': ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    if len(tonica) == 2:
        tonica = tonica[0].upper() + tonica[1]
    else:
        tonica = tonica.upper()

    try:
        tonica_position = NOTAS.index(tonica)
    except ValueError:
        raise ValueError(f'Essa nota não existe! Tente uma dessas:\n{NOTAS}')

    try:
        intervalos = ESCALAS[tonalidade]
    except KeyError:
        raise KeyError(
            'Essa escala não existe ou não foi implementada!'
            f' Tente uma dessas:\n{list(ESCALAS.keys())}'
        )

    notas = [
        NOTAS[(tonica_position + intervalo) % 12] for intervalo in intervalos
    ]

    return {
        'notas': notas,
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
