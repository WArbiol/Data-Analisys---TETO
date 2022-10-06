import dataframe_image as dfi
import matplotlib

class PieService:
    def saveSimplePie(respostas, pathAndTitle, title):
        pathAndTitle = pathAndTitle.replace('GraficosDeBarras', 'GraficosDePizza')

        plot = respostas.plot.pie(title=title, figsize=(7, 4))
        plot.figure.savefig(pathAndTitle, dpi=300,
                            bbox_inches='tight', facecolor='white')
        print(respostas)
        matplotlib.pyplot.close()
            
    def saveOptionsPie(df, pathAndTitle, title):
        pathAndTitle = pathAndTitle.replace(
            'GraficosDeBarras', 'GraficosDePizza')

        if df.shape[0] < 99:
            #df = renameColumns(df, title)
            print(df)

            plot = df.plot.pie(title=title, figsize=(7, 4))
            plot.figure.savefig(pathAndTitle, dpi=300,
                                bbox_inches='tight', facecolor='white')
            matplotlib.pyplot.close()

def renameColumns(df, col):
    df.index.name = col.split(".")[-1]
    df.columns = ['Respostas']
    return df