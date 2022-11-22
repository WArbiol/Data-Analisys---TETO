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

Possui três principais funções: `makePlotsOfSheet`, `makeAllPlots`, `take_out_tests`.

- makeAllPlots: Lê o excel, ve as planilhas (sheets) que o excel possui e para cada planilha (sheet) cra os gráficos com `makePlotsOfSheet(excel, sheet)`.
- makePlotsOfSheet: Lê as colunas do excel, tira as linhas que a Teto usou para teste (o nome da pessoa entrevistada seria Teste..algumacoisa..) com a função `take_out_tests`, e para cada coluna analisa se é uma coluna de pergunta, se é uma coluna repetida (o que acontece com perguntas que pode-se marcar varias alternativas) e se é uma pergunta de multiplas respostas faz os plots com `PlotService.makeOptionsPlot(df, column, columns)`, se é uma pergunta simples, de uma resposta `PlotService.makeSimplePlot(df, column)`.
- take_out_tests: deleta as linhas que o nome do entrevistado contém "Teste", o nome dessa coluna é 'start' ou 'Nome completo do/a morador/a que responderá e assinará a enquete:'.

### booleanService.py

Possui funções de "pergunta" que retornam True or False, os nomes das funções são auto explicativas: `isQuestion`, `repeated`, `hasMultipleOptions`

### plotService.py

Possui as funções de criar os gráficos, funções principais: `makeSimplePlot` e `makeOptionsPlot`, eles salvam os gráficos com as funções `TableService.saveSimpleTable(respostas, pathAndTitle, title)` e `TableService.saveOptionsTable(df, pathAndTitle, title)`, e salvam as tabelas com `saveBar(respostas, pathAndTitle, title)`

### tableService.py

Onde estão as funções referentes às tabelas, como salva-las, adicionar porcentagem e renomear colunas.

### optionsService.py

Funções referentes às perguntas que pode-se marcar varias alternativas.

- getAnswerOfTheOption: retorna um dataframe com o numero de respostas de cada opção.
- getTheColumnsWithOptions: retorna uma lista com as opções de respostas que o entrevistado tem.

### pathTitleService.py

Retorna o path do grafico que será gerado e o titulo da pergunta, criando os diretórios se preciso e fazendo as devidas alterações nos nomes das colunas para virar nome das perguntas.

### pieService.py

Código referente a criar os graficos de pizza, entretanto há um problema para se resolver para criar o gráfico de pizza das questões que se pode marmar multilas alternativas, por isso não é utilizada.

### onePlot.py

Análogo ao allPlots.py mas adaptado a apenas uma questão.

# Dica para estudo do código e debug

1. Tenha um Linux para evitar bugs (o primeiro autor do código usa Fedora, mas qualquer um serve).
2. Crie um excel teste com só uma pergunta (um excel com uma pergunta simples e outra com uma pergunta que pode-se maarcar varias alternativas)
3. Crie um python notebook no VSCode para facilidade (nome_do_arquivo.ipynb)
4. Cole as funções no notebook e rode célula a célula para ver o funcionamento, com prints e tudo.

# Para criar o executável .exe:

1. Esteja em ambiente Windows, com o Python instalado e como todas as bibliotecas tambem.
2. Instale o `pyinstaller`
3. Rode `pyinstaller --onefile .\src\index.py`
4. Link para saber mais: https://datatofish.com/executable-pyinstaller/

# Se tiver duvidas procure as soluções em:

1. Google
2. Stack OverFlow
3. Youtube
4. Com o último autor do código: (11) 99941-5221 (Walter -- Barueri T25)
