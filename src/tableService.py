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
    def saveSimpleTable(df, col, pathAndTitle, title):
        pathAndTitle = pathAndTitle.replace(
            'automaticPlots', 'automaticTables')
        respostas = df.groupby([col])[col].count().to_frame()
        if respostas.shape[0] < 50:
            respostas = renameColumns(respostas, title)
            respostas = addPorcent(respostas)
            # plot = respostas.plot()
            # fig = plot.get_figure()
            # fig.savefig(r"Diarreia_é_um_problema_recorrente_em_algum_membro_da_família.png")
            # pathAndTitle = 'automaticTables' + pathAndTitle.split('automaticTables')[-1]
            # pathAndTitle=pathAndTitle.replace("?", "")
            dfi.export(respostas, rf'{pathAndTitle}', fontsize=12, table_conversion='matplot')
            
    def saveOptionsTable(respostas, pathAndTitle, title):
        pathAndTitle = pathAndTitle.replace(
            'automaticPlots', 'automaticTables')

        if respostas.shape[0] < 99:
            respostas = renameColumns(respostas, title)
            respostas = addPorcent(respostas)
            dfi.export(respostas, pathAndTitle)
