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


def takeOutSideBars(string):
    try:
        string = string.replace('/', '-')
        return string
    except:
        return string


def createDir(path):
    path = path[0:-1]  # take out the last "/"
    if not os.path.isdir(f'./{path}'):
        currentPath = Path().absolute()  # tentar './'
        dirPath = str(currentPath) + path
        os.makedirs(path)
    return


class PathTitleService:
    def getPathAndTitle(col):
        path = 'automaticPlots/'
        identifier = col.split(' ')[0]
        numbers = identifier.split('.')
        for number in numbers[0:-2]:
            path = path + f'{number}/'

        createDir(path)
        createDir(path.replace('automaticPlots', 'automaticTables'))

        title = takeOutVar(col)
        title = takeOutNumber(title)
        title = takeOutSideBars(title)

        return path, title
