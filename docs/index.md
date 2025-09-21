![logo_do projeto](assets/logo1.png){width="200" .center}
# Notas Musicais

## Como usar:
Você pode chamar as escalas via linha de comando (CLI). Por exemplo:

```bash
poetry run escalas
```
Retornando os graus e as notas correspondentes

```md
|---|----|-----|----|---|----|-----|
| I | II | III | IV | V | VI | VII |
|---|----|-----|----|---|----|-----|
│ C │ D  │ E   │ F  │ G │ A  │ B   │
|---|----|-----|----|---|----|-----|
```

### Alteração na escala:
O primeiro parâmetro do CLI é a tônica da escala que deseja exibir. Dessa forma, você pode alterar a escla retornada baseado na tônica:

```bash
poetry run escalas C
```


### Alteração na tônica da escala:
O primeiro parâmetro do CLI é a tônica da escala que deseja exibir. Dessa forma, você pode alterar a escla retornada baseado na tônica. Por exemplo F:

```bash
poetry run escalas F
```

```md
|---|----|-----|----|---|----|-----|
| I | II | III | IV | V | VI | VII |
|---|----|-----|----|---|----|-----|
│ F │ G  │ A   │ A# │ C │ D  │ E   │
|---|----|-----|----|---|----|-----|
``` 
### Alteração na tonalidade da escala:
Você pode alterar a tonalidade da escala também! Esse é o segundo parâmetro da CLI. Por exemplo tonalidade maior:

```bash
poetry run escalas G maior
```

```md
|---|----|-----|----|---|----|-----|
| I | II | III | IV | V | VI | VII |
|---|----|-----|----|---|----|-----|
│ G │ A  │ B   │ C  │ D │ E  │ F#  │
|---|----|-----|----|---|----|-----|
``` 

### Mais informações sobre o CLI 

Para descobrir mais informações sobre o CLI, você pode utilizar a flag `--help`

```bash

poetry run escalas --help

```                                                         
                                                                                              ```md                                                                                         Usage: 
                                                                                              escalas [OPTIONS] [TONICA] [TONALIDADE] 

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tônica da Escala [default: C]                                        │
│   tonalidade      [TONALIDADE]  Tonalidade da Escala [default: maior]                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────
```
For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
