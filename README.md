# Data-Analisys---TETO

## Como usa-lo localmente

0. Antes de tudo, tenha o Python instalado no seu computador.
1. Para usa-lo clone o repositório em seu computador e dentro da pasta criada **"Data-Analisys---TETO"** coloque o excel gerado pela Kobo.
2. Abra a pasta **"Data-Analisys---TETO"** no **VSCode**.
3. Insta-le as deependencias rodando o comando `pip install -r requirements.txt` no terminal do VSCode.
4. Rode a aplicação com o comando `python ./src/index.py` (para linux ❤️) e `python .\src\index.py` (para windows 💔 )

## Sobre o código

Todo o código esta na pasta _src_

### index.py

Está o código que ativa a interface gráfica com auxílio da biblioteca `tkinter`
Ela também importa duas funções:

```
from allPlots import makeAllPlots
from onePlot import makeOnePlot
```

`makeAllPlots`serve para criar todos os gráficos;  
`makeOnePlot`serve para criar um gráfico com o apartir do nome da coluna que foi especificado na entrada de texto;

Daí notamos outros dois arquivos de código: `allPlots` e `onePlot`:

### allPlots.py
