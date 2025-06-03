from tkinter import *
from tkinter import ttk
class GestionEtudiants:
    def __init__(self,root):
        self.root=root
        self.root.title("Système de gestion d'un établissement de formations ")

        #Taille ecran
        largeur_ecran = self.root.winfo_screenwidth()
        hauteur_ecran = self.root.winfo_screenheight()
        self.root.geometry('%dx%d' % (largeur_ecran, hauteur_ecran))
        self.root.configure(bg='#DADADA')

        #========Titre de la fenetre gestion des etudiants=======================
        titre = Label(self.root, text='Gestion des étudiants',fg="white",bd=2, relief="groove", font=('ubuntu', 20, 'bold'),padx=20, bg='#1E02F2')
        titre.pack(side="top", fill="x")

        # ========Frame menu principale =======================
        menuFrame = Frame(self.root, bd=2, relief="groove", bg='#1E02F2')
        menuFrame.place(x=20, y=50, width=0.97*largeur_ecran, height=80)

        # ========Formulaire de saisi des données des etudiants =======================
        manageFrame = Frame(self.root, bd=2, relief="groove", bg='#1E02F2')
        manageFrame.place(x=20, y=130, width=0.32 * largeur_ecran, height=500)

        titleLabel = Label(manageFrame, text="Information sur l'etudiant",font=('ubuntu', 18, 'bold'),bg='#1E02F2',fg='white' )
        titleLabel.grid(row=0, columnspan=2, pady=15)

        # ========Champs de remplisage des infos sur formulaire de saisi des données des etudiants =======================
        ineLabelEtudiant = Label(manageFrame, text="INE:",font=('ubuntu', 12, 'bold'),bg='#1E02F2',fg='white')
        ineLabelEtudiant.grid(row=1, column=0, pady=10, sticky='w')
        ineLabelEtudiantText = Entry(manageFrame,font=('Times new roman', 12, 'bold'),bd=2,relief="groove", width=30)
        ineLabelEtudiantText.grid(row=1, column=1, padx=10, pady=10, sticky='w' )

        nomLabelEtudiant = Label(manageFrame, text="Nom:",font=('ubuntu', 12, 'bold'),bg='#1E02F2',fg='white')
        nomLabelEtudiant.grid(row=2, column=0, pady=10, sticky='w')
        nomLabelEtudiantText = Entry(manageFrame,font=('Times new roman', 12, 'bold'),bd=2,relief="groove", width=30)
        nomLabelEtudiantText.grid(row=2, column=1, padx=10, pady=10, sticky='w' )

        prenomLabelEtudiant = Label(manageFrame, text="Prénom:", font=('ubuntu', 12, 'bold'), bg='#1E02F2', fg='white')
        prenomLabelEtudiant.grid(row=3, column=0, pady=10, sticky='w')
        prenomLabelEtudiantText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove", width=30)
        prenomLabelEtudiantText.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        emailLabelEtudiant = Label(manageFrame, text="Adresse email:", font=('ubuntu', 12, 'bold'), bg='#1E02F2', fg='white')
        emailLabelEtudiant.grid(row=4, column=0, pady=10, sticky='w')
        emailLabelEtudiantText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove", width=30)
        emailLabelEtudiantText.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        adresseLabelEtudiant = Label(manageFrame, text="Adresse:", font=('ubuntu', 12, 'bold'), bg='#1E02F2', fg='white')
        adresseLabelEtudiant.grid(row=5, column=0, pady=10, sticky='w')
        adresseLabelEtudiantText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove", width=30)
        adresseLabelEtudiantText.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        villeLabelEtudiant = Label(manageFrame, text="Ville:", font=('ubuntu', 12, 'bold'), bg='#1E02F2', fg='white')
        villeLabelEtudiant.grid(row=6, column=0, pady=10, sticky='w')
        villeLabelEtudiantText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove", width=30)
        villeLabelEtudiantText.grid(row=6, column=1, padx=10, pady=10, sticky='w')



        # ========ajout du bouton d'action de etudiants  des etudiants =================
        boutonFrame = Button(manageFrame, bd=2, relief="groove", bg='#1E02F2')
        boutonFrame.place(x=20, y=400, width=0.28  * largeur_ecran, height=70)

        # ========Frame affciche des données des etudiants =======================
        detailsFrame = Frame(self.root, bd=2, relief="groove", bg='#1E02F2')
        detailsFrame.place(x=0.34 * largeur_ecran, y=130, width=0.645  * largeur_ecran, height=500)


root = Tk()
yekola = GestionEtudiants(root)
root.mainloop()
