import pandas as pd
import os
from pathlib import Path
import glob
from booleanService import BooleanService as bool
from plotService import PlotService


def makePlotsOfCol(excel, sheet, col):
    df = pd.read_excel(excel, sheet)
    columns = df.columns
    columns = columns.tolist()
    for column in columns:
        if column == col:
            if bool.repeated(column, columns):
                continue
            if bool.hasMultipleOptions(column, columns):
                PlotService.makeOptionsPlot(df, column, columns)
                continue
            PlotService.makeSimplePlot(df, column)


def makeOnePlot(col):
    excelPath = Path().absolute()  
    excelPath= os.path.join(excelPath, '*.xlsx')
    xlsx = glob.glob(excelPath)
    excel = pd.ExcelFile(xlsx[0])
    sheets = excel.sheet_names

    for sheet in sheets:
        makePlotsOfCol(excel, sheet, col)
