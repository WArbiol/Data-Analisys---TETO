import pandas as pd
import glob
from booleanService import BooleanService as bool
from plotService import PlotService


def makePlotsOfSheet(excel, sheet):
    df = pd.read_excel(excel, sheet)
    columns = df.columns
    columns = columns.tolist()
    for column in columns:
        if not bool.isQuestion(column) or bool.repeated(column, columns):
            continue
        if bool.hasMultipleOptions(column, columns):
            PlotService.makeOptionsPlot(df, column, columns)
            continue

        PlotService.makeSimplePlot(df, column)


def makeAllPlots():
    excelPath = "./*.xlsx"
    xlsx = glob.glob(excelPath)
    print(xlsx)
    excel = pd.ExcelFile(xlsx[0])
    sheets = excel.sheet_names

    for sheet in sheets:
        makePlotsOfSheet(excel, sheet)
