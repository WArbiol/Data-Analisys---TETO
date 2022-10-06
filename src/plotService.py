from pathTitleService import PathTitleService
from tableService import TableService
from optionsService import OptionsService
import os, matplotlib


class PlotService:
    def makeSimplePlot(df, col):
        path, title = PathTitleService.getPathAndTitle(col)
        pathAndTitle = os.path.join(path,title+'.png')

        df = df[col].to_frame() #get lighter and faster
        df = df[col].dropna().to_frame()
        df = takeOutNoneAnswers(df, col) 
        df = df[col].rename('').to_frame()
        col = ''
        respostas = df.groupby([col])[col].count()

        if respostas.size > 0:
            TableService.saveSimpleTable(respostas, pathAndTitle, title)
            savePlot(respostas, pathAndTitle, title)

    def makeOptionsPlot(df, col, columns):
        path, title = PathTitleService.getPathAndTitle(col)
        columnsOptions = OptionsService.getTheColumnsWithOptions(col, columns)
        df = OptionsService.getAnswerOfTheOption(columnsOptions, df)
        df.rename(index=lambda s: s.split('/')[-1], inplace=True)
        pathAndTitle = os.path.join(path,title+'.png')
        
        TableService.saveOptionsTable(df, pathAndTitle, title)
        savePlot(df, pathAndTitle, title)

def takeOutNoneAnswers(df, col):
    df = df[(df[col] != 'Nenhuma') & (df[col] != 'Nenhum') & 
            (df[col] != 'Não sabe/Não respondeu') & (df[col] != 'Não sabe/ Não respondeu')]
    return df

def savePlot(respostas, pathAndTitle, title):
    plot = respostas.plot.bar(title=title, figsize=(7, 4))
    plot.figure.savefig(pathAndTitle, dpi=300,
                        bbox_inches='tight', facecolor='white')
    matplotlib.pyplot.close()