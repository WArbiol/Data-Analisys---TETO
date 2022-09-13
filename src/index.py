from allPlots import makeAllPlots
from tkinter import *
from tkinter import messagebox

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
                   command=makeAllPlots, fg="white", bg="blue", font="7", bd="5", padx="14")
myButton3 = Button(root, text="ajuda", command=myClick)

myLabel1.grid(row=1, column=0)
myLabel2.grid(row=2, column=0)
myButton1.grid(row=4, column=0, padx="2", pady="2")
myButton2.grid(row=0, column=0, padx="2", pady="8")
myButton3.grid(row=5, column=1, padx="2", pady="2")

#grid(row=0, column=0)
root.mainloop()
