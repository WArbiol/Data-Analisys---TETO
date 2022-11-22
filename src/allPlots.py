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

    df = take_out_tests(df)

    for column in columns:
        if not bool.isQuestion(column) or bool.repeated(column, columns):
            continue
        if bool.hasMultipleOptions(column, columns):
            PlotService.makeOptionsPlot(df, column, columns)
            continue
        
        PlotService.makeSimplePlot(df, column)


def makeAllPlots():
    excelPath = Path().absolute()  
    excelPath= os.path.join(excelPath, '*.xlsx')
    xlsx = glob.glob(excelPath)
    excel = pd.ExcelFile(xlsx[0])
    sheets = excel.sheet_names

    for sheet in sheets:
        makePlotsOfSheet(excel, sheet)


def take_out_tests(df):
    firstColumn = df.columns[0]
    if firstColumn != 'start':
        col_with_names = firstColumn
    else:
        col_with_names = 'Nome completo do/a morador/a que responderá e assinará a enquete:'
    try:
        df = df[df[col_with_names].str.contains('Teste') == False ]
        return df
    except:
        return df
