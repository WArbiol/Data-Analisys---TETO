import os
from pathlib import Path


def takeOutNumber(string):
    try:
        withOutNumbers = string.split('. ')[1]
        return withOutNumbers
    except:
        return string


def takeOutVar(string):
    try:
        withOutVarPar1 = string.split(' ${')[0]
        withOutVarPar2 = string.split('}')[1]
        withOutVar = withOutVarPar1 + withOutVarPar2
        return withOutVar
    except:
        return string


def takeOutForbiddenCharacters(string):
    if string.__contains__('/'):
        string = string.replace('/', '-')
    if string.__contains__('?'):
        string = string.replace('?', '')

    return string


def createDir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

class PathTitleService:
    def getPathAndTitle(col):
        path = Path().absolute()
        path = os.path.join(path, 'GraficosDeBarras')
        print(col)       
        identifier = col.split(' ')[0]
        numbers = identifier.split('.')
        for number in numbers[0:-2]:
            path = os.path.join(path, f'{number}')

        createDir(path)
        createDir(path.replace('GraficosDeBarras', 'Tabelas'))
        createDir(path.replace('GraficosDeBarras', 'GraficosDePizza'))

        title = takeOutVar(col)
        title = takeOutNumber(title)
        title = takeOutForbiddenCharacters(title)

        return path, title