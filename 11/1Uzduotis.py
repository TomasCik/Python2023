from tkinter import *

langas = Tk()
langas.geometry("300x300")

def spausdinti():
    ivesta = laukas1.get()
    rezultatas["text"] = "Labas, " + ivesta


uzrasas1 = Label(langas, text="Įveskite vardą:")
laukas1 = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=spausdinti)
langas.bind("<Return>", lambda event: spausdinti())
rezultatas = Label(langas, text="")

uzrasas1.grid(row=0, column=1)
laukas1.grid(row=0, column=2)
mygtukas.grid(row=0, column=3)
rezultatas.grid(row=1, column=2)

langas.mainloop()








