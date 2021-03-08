
#-------------------------------------------------------------------------------------
def fen_connexion():
    fen1 = tkinter.Tk()
    fen1.geometry("240x300")
    fen1.title("Fenetre de connexion")
    #-------------------------------------------------------------------------------------
    lab1 = tkinter.Label(fen1, text="Nom d'utilisateur")
    ent1 = tkinter.Entry(fen1)
    lab2 = tkinter.Label(fen1, text="Mot de passe")
    ent2 = tkinter.Entry(fen1, show = "*", exportselection=0)
    rad1 = tkinter.Radiobutton(fen1, text="Medcin", value=0)
    rad2 = tkinter.Radiobutton(fen1, text="Patient", value=1)
    but1 = tkinter.Button(fen1, text="Connexion", command=fen_validation_conx)
    #-------------------------------------------------------------------------------------
    fen1.grid()
    lab1.grid(padx=60,pady=10)
    ent1.grid()
    lab2.grid()
    ent2.grid()
    rad1.grid()
    rad2.grid()
    but1.grid()
    #-------------------------------------------------------------------------------------
    fen1.mainloop()
#-------------------------------------------------------------------------------------
def fen_validation_conx():
    fen2 = tkinter.Tk()
    fen2.geometry("150x180")
    fen2.title("Fenetre de validation connexion")
    #-------------------------------------------------------------------------------------
    lab2_1 = tkinter.Label(fen2, text="code de validation")
    ent2_1 = tkinter.Entry(fen2)
    but_2_1 = tkinter.Button(fen2, text="Valider")
    #-------------------------------------------------------------------------------------
    fen2.grid()
    lab2_1.grid(padx=20, pady=10)
    ent2_1.grid()
    but_2_1.grid()
    #-------------------------------------------------------------------------------------
    fen2.mainloop()
#-------------------------------------------------------------------------------------