from pathTitleService import PathTitleService
from tableService import TableService
from optionsService import OptionsService


class PlotService:
    def makeSimplePlot(df, col):
        path, title = PathTitleService.getPathAndTitle(col)

        tablePathAndTitle = path+title+'.png'
        TableService.saveSimpleTable(df, col, tablePathAndTitle, title)

        try:
            nomeCol = 'Nome completo do/a morador/a que responderá e assinará a enquete:'
            df = df[(df[nomeCol] != 'Teste app') & (df[nomeCol] != 'Teste 2') & (df[nomeCol] != 'Teste') & (df[col] != 'Nenhuma') & (
                df[col] != 'Nenhum') & (df[col] != 'Não sabe/Não respondeu') & (df[col] != 'Não sabe/ Não respondeu')][col].to_frame()
        except:
            df = df[(df[col] != 'Nenhuma') & (df[col] != 'Nenhum') & (
                df[col] != 'Não sabe/Não respondeu') & (df[col] != 'Não sabe/ Não respondeu')][col].to_frame()
        df = df[col].rename('').to_frame()
        col = ''
        respostas = df.groupby([col])[col].count()
        if respostas.size > 0:
            plot = respostas.plot.bar(title=title, figsize=(7, 4))
            plot.figure.savefig(path+title, dpi=300,
                                bbox_inches='tight', facecolor='white')

    def makeOptionsPlot(df, col, columns):
        path, title = PathTitleService.getPathAndTitle(col)
        columnsOptions = OptionsService.getTheColumnsWithOptions(col, columns)
        df = OptionsService.getAnswerOfTheOption(columnsOptions, df)
        df.rename(index=lambda s: s.split('/')[-1], inplace=True)

        tablePathAndTitle = path+title+'.png'
        TableService.saveOptionsTable(df, tablePathAndTitle, title)

        plot = df.plot.bar(title=title, figsize=(7, 4), legend=False)
        plot.figure.savefig(path+title, dpi=300,
                            bbox_inches='tight', facecolor='white')
