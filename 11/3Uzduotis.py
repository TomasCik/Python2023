



from tkinter import *

langas = Tk()
langas.geometry("300x300")
langas.title("Naudinga programa")
langas.iconbitmap(r"thunderstorm.ico")
paskutinis = StringVar()



def spausdinti():

    a = laukas1.get()
    paskutinis.set(a)
    rezultatas["text"] = "Labas, " + str(a)



def atkurti_paskutini():
    rezultatas["text"] = "Labas, " + paskutinis.get()


def isvalyti():
   laukas1.delete(0, END)
   rezultatas["text"] = ""


def iseiti():
    langas.destroy()




meniu = Menu(langas)
langas.config(menu = meniu)
submeniu = Menu(meniu, tearoff=0)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Išvalyti", command=isvalyti)
submeniu.add_command(label="Atkurti paskutinį", command=atkurti_paskutini)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=iseiti)




uzrasas1 = Label(langas, text="Įveskite vardą:")
laukas1 = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=spausdinti)
mygtukas["bg"] = "red"
langas.bind("<Return>", lambda event: spausdinti())
rezultatas = Label(langas, text="")

# statusbaras = Label(langas, text="nieko nedaro", bd=5, relief=SUNKEN, anchor=W)
# statusbaras.pack(side=BOTTOM, fill=X)

status = Label(langas, text="", bd=1, relief=SUNKEN, anchor=W)
status.pack()

uzrasas1.pack()
laukas1.pack()
mygtukas.pack()
rezultatas.pack()





langas.mainloop()


















