config_dict = {
    'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
}
NOTAS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escalas(tonica:str, tonalidade:str) -> dict[str,list[str]]:
    """
    Gera uma escala apartir de uma nota tônica e uma tonalidade

    Parameters:
        tonica: Nota que será a tônica da escala
        tonalidade: Tonalidade da escala
    
    Returns: 
        Retorna um dicionário com as notas e as tonalidades

    Examples:
        >>> escalas('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escalas('A', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """

    intervalos = ESCALAS[tonalidade]
    tonica_position = NOTAS.index(tonica)

    notas = [
        NOTAS[(tonica_position + intervalo) % 12] for intervalo in intervalos
    ]

    return {
        'notas': notas,
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
