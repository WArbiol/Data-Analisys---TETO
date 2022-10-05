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
    if not os.path.isdir(path):
        os.makedirs(path)

class PathTitleService:
    def getPathAndTitle(col):
        path = Path().absolute()  
        path = os.path.join(path, 'automaticPlots')
        numbers = col.split('. ')[0]
        for number in numbers[0:-2]:
            path = os.path.join(path, f'{number}')

        createDir(path)
        createDir(path.replace('automaticPlots', 'automaticTables'))

        title = takeOutVar(col)
        title = takeOutNumber(title)
        title = takeOutSideBars(title)

        return path, title