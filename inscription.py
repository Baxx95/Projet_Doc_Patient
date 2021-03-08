#coding:utf-8
import tkinter.tix

def fen_inscription():
    fen3 = tkinter.tix.Tk()
    fen3.geometry("340x680")
    fen3.title("Fenetre d'inscription")
    #-------------------------------------------------------------------------------------
    lab3_1 = tkinter.Label(fen3, text="Nom")
    entr3_1 = tkinter.Entry(fen3)

    lab3_2 = tkinter.Label(fen3, text="Prénom")
    entr3_2 = tkinter.Entry(fen3)

    Label_Frame = tkinter.LabelFrame(fen3, text="Date et lieu de naissance",width=100, height=200, borderwidth=1)
    lab3_3 = tkinter.Label(Label_Frame, text="Jour")
    spin_w_1 = tkinter.Spinbox(Label_Frame, from_ = 1, to = 31, width=10)
    lab3_4 = tkinter.Label(Label_Frame, text="Mois")
    spin_w_2 = tkinter.Spinbox(Label_Frame, from_ = 1, to = 12, width=10)
    lab3_5 = tkinter.Label(Label_Frame, text="Année")
    spin_w_3 = tkinter.Spinbox(Label_Frame, from_ = 1940, to = 2019, width=10)
    lab = tkinter.Label(Label_Frame)
    """     dernier label du cadre Label_Frame : 
            il joue juste un role de séparation entre la bordure 
            inférieur du cadre et l'avant dernier widget
    """

    lab3_6 = tkinter.Label(fen3, text="Numéro de téléphone")
    entr3_3 = tkinter.Entry(fen3)

    lab3_7 = tkinter.Label(fen3, text="Numéro de Carte d'Identité")
    ent3_4 = tkinter.Entry(fen3)

    lab3_8 = tkinter.Label(fen3, text="E-mail")
    ent3_5 = tkinter.Entry(fen3)

    rad3 = tkinter.Radiobutton(fen3, text="Médecin", value=0)
    rad4 = tkinter.Radiobutton(fen3, text="Patient", value=1)
    
    lab3_9 = tkinter.Label(fen3, text="Specialité")
    varcombo = tkinter.tix.StringVar() 
    combo = tkinter.tix.ComboBox(fen3, editable=1, dropdown=1, variable=varcombo)
    combo.entry.config(state='readonly')  ## met la zone de texte en lecture seule
    combo.insert(0, 'Généraliste') 
    combo.insert(1, 'Cardiologue')
    combo.insert(2, 'Neurologue')
    combo.insert(3, 'Gynécologue')
    combo.insert(4, 'Dentiste')
    combo.insert(5, 'Sages-Femme')
    combo.insert(6, 'Ophtalmologue')
    combo.insert(7, 'Urologue')
    combo.insert(8, 'Dermatologue')
    combo.insert(9, 'Diététicien')
    combo.insert(10, 'Allergologue')
    combo.insert(11, 'Pédiatre')
    combo.insert(12, 'Radiologue')
    combo.insert(13, 'Chirurgien')
    combo.insert(14, 'Ostéopathe')
    combo.insert(15, 'Prothésiste Dentaire')
    combo.insert(16, 'Dentiste-Chirurgien Dentiste')
    combo.insert(17, 'Infirmier-Infirmière')
    combo.insert(18, 'Orthopédiste')
    combo.insert(19, 'Pharmacien')
    combo.insert(20, 'Nutritioniste')
    combo.insert(21, 'Pédopsychiatre')
    combo.insert(22, 'Diabétologue')
    combo.insert(23, 'Oto-Rhino-Laryngologiste')
    combo.insert(24, 'Pneumologue')
    combo.insert(25, 'Phytothérapeute')
    combo.insert(26, 'Kinésithérapeute')
    combo.insert(27, 'Rhumatologue')
    combo.insert(28, 'Vétérinaire')
    combo.insert(29, 'Psychologue')
    combo.insert(30, 'Sophrologue')
    combo.insert(31, 'Etiopathe')
    combo.insert(32, 'Biologiste')
    combo.insert(33, 'Néphrologue')
    combo.insert(34, 'Neuro-Chirurgien')
    combo.insert(35, 'Sexologue')
    combo.insert(36, 'Médecine Physique et Réadaptation')
    combo.insert(37, 'Urgentiste-Urgentologue')
    combo.insert(38, 'Laborantin')

    Label_Frame1 = tkinter.LabelFrame(fen3, text="Renseignement-Diplome",width=150, height=250, borderwidth=1)
    lab3_10 = tkinter.Label(Label_Frame1, text="Faculté/Ecole")
    ent3_6 = tkinter.Entry(Label_Frame1, width=20)
    lab3_11 = tkinter.Label(Label_Frame1, text="Lieu d'Obtention")
    ent3_7 = tkinter.Entry(Label_Frame1, width=20)
    lab3_12 = tkinter.Label(Label_Frame1, text="Diplome Obtenu")
    # à uploader ...
    lab3_13 = tkinter.Label(Label_Frame1, text="Année d'Obtention")
    spin_w_4 = tkinter.Spinbox(Label_Frame1, from_ = 1970, to = 2019, width=10)
    lab1 = tkinter.Label(Label_Frame1)
    """     dernier label du cadre Label_Frame : 
            il joue juste un role de séparation entre la bordure 
            inférieur du cadre et l'avant dernier widget
    """
    lab3_14 = tkinter.Label(fen3, text="Nombre d'année d'epérience")
    spin_w_5 = tkinter.Spinbox(fen3, from_ = 0, to = 40, width=10)
    
    btn = tkinter.Button(fen3, text="Enregistrer", command=validation_inscription)
    #-------------------------------------------------------------------------------------
    fen3.grid()
    lab3_1.grid(padx=90, pady=1)
    entr3_1.grid()
    lab3_2.grid()
    entr3_2.grid()
    Label_Frame.grid()
    lab3_3.grid(padx=30, pady=1)
    spin_w_1.grid(padx=30)
    lab3_4.grid(padx=30)
    spin_w_2.grid(padx=30)
    lab3_5.grid(padx=30)
    spin_w_3.grid(padx=30)
    lab.grid()
    lab3_6.grid()
    entr3_3.grid()
    lab3_7.grid()
    ent3_4.grid()
    lab3_8.grid()
    ent3_5.grid()
    rad3.grid()
    rad4.grid()
    lab3_9.grid()
    combo.grid()
    Label_Frame1.grid()
    lab3_10.grid(padx=30, pady=1)
    ent3_6.grid()
    lab3_11.grid()
    ent3_7.grid()
    lab3_12.grid()

    lab3_13.grid()
    spin_w_4.grid()
    lab1.grid()
    lab3_14.grid()
    spin_w_5.grid()
    
    btn.grid()

    #-------------------------------------------------------------------------------------
    fen3.mainloop()
#-------------------------------------------------------------------------------------
def validation_inscription():
    fen4 = tkinter.Tk()
    fen4.geometry("280x180")
    fen4.title("Fenetre de validation d'Inscription")
    
    lab = tkinter.Label(fen4, text="Saisissez le code envoyé au numero de téléphone \nque vous avez entré, puis allez cliquer sur \nle lien envoyé à l'adresse mail que vous avez \nsaisi pour valider votre inscription")
    btn = tkinter.Button(fen4, text="Valider", command=fen4.destroy)
    ent = tkinter.Entry(fen4)

    lab.grid()
    ent.grid()
    btn.grid()
    #-------------------------------------------------------------------------------------
    fen4.mainloop()
#-------------------------------------------------------------------------------------
