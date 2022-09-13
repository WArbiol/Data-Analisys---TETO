import pandas as pd
import glob
from booleanService import BooleanService as bool
from plotService import PlotService
from tkinter import *
from tkinter import messagebox


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


def main():
    excelPath = "./*.xlsx"
    xlsx = glob.glob(excelPath)
    print(xlsx)
    excel = pd.ExcelFile(xlsx[0])
    sheets = excel.sheet_names

    for sheet in sheets:
        makePlotsOfSheet(excel, sheet)


# main()

root = Tk()
root.title("Análise da pesquisa")
root.geometry("500x200")  # Size of the new screen
root.columnconfigure(0, weight=1)  # Placement settings


def myClick():
    messagebox.showinfo("ajuda", "[INSTRUÇÕES]")


e = Entry(root, width=70, borderwidth=5, bg="#D2CFCE")
e.grid(row=3, column=0)
e.get()  # This is the value recive from the input

myLabel1 = Label(root, text=" ", font="7", )
myLabel2 = Label(root, text="Pergunta:", font="7", )
myButton1 = Button(root, text="Gerar análise da pergunta",
                   fg="white", bg="blue", font="7", bd="5", padx="50")
myButton2 = Button(root, text="Gerar análise de todas as perguntas",
                   command=main, fg="white", bg="blue", font="7", bd="5", padx="14")
myButton3 = Button(root, text="ajuda", command=myClick)

myLabel1.grid(row=1, column=0)
myLabel2.grid(row=2, column=0)
myButton1.grid(row=4, column=0, padx="2", pady="2")
myButton2.grid(row=0, column=0, padx="2", pady="8")
myButton3.grid(row=5, column=1, padx="2", pady="2")

#grid(row=0, column=0)
root.mainloop()
