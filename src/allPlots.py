import pandas as pd
import os
from pathlib import Path
import glob
from booleanService import BooleanService as bool
from plotService import PlotService
import matplotlib


def makePlotsOfSheet(excel, sheet):
    df = pd.read_excel(excel, sheet)
    columns = df.columns
    columns = columns.tolist()

    for column in columns:
        if not bool.isQuestion(column) or bool.repeated(column, columns):
            continue
        if bool.hasMultipleOptions(column, columns):
            if column=='Qual outra condição?': print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            PlotService.makeOptionsPlot(df, column, columns)
            continue
        
        if column=='Qual outra condição?': print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
        PlotService.makeSimplePlot(df, column)


def makeAllPlots():
    excelPath = Path().absolute()  
    excelPath= os.path.join(excelPath, '*.xlsx')
    xlsx = glob.glob(excelPath)
    excel = pd.ExcelFile(xlsx[0])
    sheets = excel.sheet_names

    for sheet in sheets:
        makePlotsOfSheet(excel, sheet)
