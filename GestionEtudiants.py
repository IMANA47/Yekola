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
        self.root.configure(bg='gray')

        #========Titre de la fenetre gestion des etudiants=======================
        titre = Label(self.root, text='Gestion des étudiants',fg="white",bd=2, relief="groove", font=('ubuntu', 20, 'bold'),padx=20, bg='blue')
        titre.pack(side="top", fill="x")

        # ========Frame menu principale =======================
        menuFrame = Frame(self.root, bd=2, relief="groove", bg='blue')
        menuFrame.place(x=20, y=50, width=0.97*largeur_ecran, height=80)

        # ========Formulaire de saisi des données des etudiants =======================
        manageFrame = Frame(self.root, bd=2, relief="groove", bg='blue')
        manageFrame.place(x=20, y=130, width=0.32 * largeur_ecran, height=500)

        titleLabel = Label(manageFrame, text="Information sur l'etudiant",font=('ubuntu', 18, 'bold'),bg='blue',fg='white' )
        titleLabel.grid(row=0, columnspan=2, pady=15)

        # ========ajout du bouton d'action de etudiants  des etudiants =======================
        boutonFrame = Button(manageFrame, bd=2, relief="groove", bg='blue')
        boutonFrame.place(x=20, y=400, width=0.28  * largeur_ecran, height=70)

        # ========Frame affciche des données des etudiants =======================
        detailsFrame = Frame(self.root, bd=2, relief="groove", bg='blue')
        detailsFrame.place(x=0.34 * largeur_ecran, y=130, width=0.645  * largeur_ecran, height=500)


root = Tk()
yekola = GestionEtudiants(root)
root.mainloop()
