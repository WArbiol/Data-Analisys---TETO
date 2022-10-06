from allPlots import makeAllPlots
from onePlot import makeOnePlot
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Análise da pesquisa")
root.geometry("500x200")  # Size of the new screen
root.columnconfigure(0, weight=1)  # Placement settings


def myClick():
    messagebox.showinfo("ajuda", "[INSTRUÇÕES]")


one_analysis_input = Entry(root, width=70, borderwidth=5, bg="#D2CFCE")
one_analysis_input.grid(row=3, column=0)

myLabel1 = Label(root, text=" ", font="7", )
one_analysis_label = Label(root, text="Pergunta:", font="7", )
one_analysis_button = Button(root, text="Gerar análise da pergunta",
                   fg="white", bg="blue", font="7", bd="5", padx="50",
                   command=lambda: makeOnePlot(one_analysis_input.get()))
all_analysis_button = Button(root, text="Gerar análise de todas as perguntas",
                   command=makeAllPlots, fg="white", bg="blue", font="7", bd="5", padx="14")
help_button = Button(root, text="ajuda", command=myClick)

myLabel1.grid(row=1, column=0)
one_analysis_label.grid(row=2, column=0)
one_analysis_button.grid(row=4, column=0, padx="2", pady="2")
all_analysis_button.grid(row=0, column=0, padx="2", pady="8")
help_button.grid(row=5, column=1, padx="2", pady="2")

root.mainloop()
