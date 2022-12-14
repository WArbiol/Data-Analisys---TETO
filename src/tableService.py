import dataframe_image as dfi
import matplotlib


def renameColumns(df, col):
    df.index.name = col.split(".")[-1]
    df.columns = ['Respostas']
    return df


def addPorcent(df):
    respostas = df['Respostas'].sum()
    df[f'Porcentagem ({respostas} respostas)'] = (
        (df['Respostas']/respostas)*100).round(2).astype(str) + '%'
    return df


class TableService:
    def saveSimpleTable(respostas, pathAndTitle, title):
        pathAndTitle = pathAndTitle.replace('GraficosDeBarras', 'Tabelas')
        respostas = respostas.to_frame()
        
        if respostas.shape[0] < 50:
            respostas = renameColumns(respostas, title)
            respostas = addPorcent(respostas)
            dfi.export(respostas, pathAndTitle, fontsize=10, table_conversion='matplot')
            
    def saveOptionsTable(respostas, pathAndTitle, title):
        pathAndTitle = pathAndTitle.replace(
            'GraficosDeBarras', 'Tabelas')

        if respostas.shape[0] < 99:
            respostas = renameColumns(respostas, title)
            respostas = addPorcent(respostas)
            dfi.export(respostas, pathAndTitle, fontsize=10, table_conversion='matplot')
