from tkinter import *
from tkinter import ttk, messagebox
from validate_email import validate_email
import sqlite3


class GestionEtudiants:
    def __init__(self, root):
        self.root = root
        self.root.title("Système de gestion d'un établissement de formations ")

        # Taille ecran
        largeur_ecran = self.root.winfo_screenwidth()
        hauteur_ecran = self.root.winfo_screenheight()
        self.root.geometry('%dx%d' % (largeur_ecran, hauteur_ecran))
        self.root.configure(bg='#DADADA')

        # ========Titre de la fenetre gestion des etudiants=======================
        titre = Label(self.root, text='Gestion des étudiants', fg="white", bd=2, relief="groove",
                      font=('ubuntu', 20, 'bold'), padx=20, bg='#1E02F2')
        titre.pack(side="top", fill="x")

        global ineLabelEtudiantText
        global nomLabelEtudiantText
        global prenomLabelEtudiantText
        global adresseLabelEtudiantText
        global emailLabelEtudiantText
        global villeLabelEtudiantText

        # ========Frame menu principale =======================
        menuFrame = Frame(self.root, bd=2, relief="groove", bg='#1E02F2')
        menuFrame.place(x=20, y=50, width=0.97 * largeur_ecran, height=80)

        # ========les bouton des differents menu principale =======================
        gestionFormationButon = Button(menuFrame, text="Gestion des Formations", font=('ubuntu', 16, 'bold'), width=23,
                                       cursor='hand2', command=self.gestionFormations)
        gestionFormationButon.grid(row=0, column=1, padx=10, pady=10)

        gestionInscriptionButon = Button(menuFrame, text="Gestion des inscriptions", font=('ubuntu', 16, 'bold'),
                                         width=23, cursor='hand2', command=self.gestionInscriptions)
        gestionInscriptionButon.grid(row=0, column=2, padx=10, pady=10)

        gestionFormateurButon = Button(menuFrame, text="Gestion des formateurs", font=('ubuntu', 16, 'bold'), width=23,
                                       cursor='hand2', command=self.gestionFormateur)
        gestionFormateurButon.grid(row=0, column=3, padx=10, pady=10)

        # ========Formulaire de saisi des données des etudiants =======================
        manageFrame = Frame(self.root, bd=2, relief="groove", bg='#1E02F2')
        manageFrame.place(x=20, y=130, width=0.32 * largeur_ecran, height=500)

        titleLabel = Label(manageFrame, text="Information sur l'etudiant", font=('ubuntu', 18, 'bold'), bg='#1E02F2',
                           fg='white')
        titleLabel.grid(row=0, columnspan=2, pady=15)

        # ========Champs de remplisage des infos sur formulaire de saisi des données des etudiants =======================
        ineLabelEtudiant = Label(manageFrame, text="INE:", font=('ubuntu', 12, 'bold'), bg='#1E02F2', fg='white')
        ineLabelEtudiant.grid(row=1, column=0, pady=10, sticky='w')
        ineLabelEtudiantText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove", width=30)
        ineLabelEtudiantText.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        nomLabelEtudiant = Label(manageFrame, text="Nom:", font=('ubuntu', 12, 'bold'), bg='#1E02F2', fg='white')
        nomLabelEtudiant.grid(row=2, column=0, pady=10, sticky='w')
        nomLabelEtudiantText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove", width=30)
        nomLabelEtudiantText.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        prenomLabelEtudiant = Label(manageFrame, text="Prénom:", font=('ubuntu', 12, 'bold'), bg='#1E02F2', fg='white')
        prenomLabelEtudiant.grid(row=3, column=0, pady=10, sticky='w')
        prenomLabelEtudiantText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove",
                                        width=30)
        prenomLabelEtudiantText.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        emailLabelEtudiant = Label(manageFrame, text="Adresse email:", font=('ubuntu', 12, 'bold'), bg='#1E02F2',
                                   fg='white')
        emailLabelEtudiant.grid(row=4, column=0, pady=10, sticky='w')
        emailLabelEtudiantText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove",
                                       width=30)
        emailLabelEtudiantText.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        adresseLabelEtudiant = Label(manageFrame, text="Adresse:", font=('ubuntu', 12, 'bold'), bg='#1E02F2',
                                     fg='white')
        adresseLabelEtudiant.grid(row=5, column=0, pady=10, sticky='w')
        adresseLabelEtudiantText = Text(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove",height=1.70,
                                         width=30)
        adresseLabelEtudiantText.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        villeLabelEtudiant = Label(manageFrame, text="Ville:", font=('ubuntu', 12, 'bold'), bg='#1E02F2', fg='white')
        villeLabelEtudiant.grid(row=6, column=0, pady=10, sticky='w')
        villeLabelEtudiantText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove",
                                       width=30)
        villeLabelEtudiantText.grid(row=6, column=1, padx=10, pady=10, sticky='w')

        # ========ajout du espace des boutons d'action de gestion  des etudiants =================
        boutonFrame = Button(manageFrame, bd=2, relief="groove", bg='#1E02F2')
        boutonFrame.place(x=20, y=400, width=0.28 * largeur_ecran, height=70)

        # ========ajout des boutons d'action de gestions des etudiants =================
        enregistreButton = Button(boutonFrame, text='Enregistrer', width=8, height=2, command=self.enregistrerEtudiant,
                                  cursor='hand2')
        enregistreButton.grid(row=0, column=0, padx=10, pady=10)

        modifierButton = Button(boutonFrame, text='Modifier', width=8, height=2, command=self.modifierEtudiant,
                                cursor='hand2')
        modifierButton.grid(row=0, column=1, padx=10, pady=10)

        supprimerButton = Button(boutonFrame, text='Supprimer', width=8, height=2, command=self.supprimerEtudiant,
                                 cursor='hand2')
        supprimerButton.grid(row=0, column=2, padx=10, pady=10)

        rafraichirButton = Button(boutonFrame, text='Rafraichir', width=8, height=2, command=self.rafraichirEtudiant,
                                  cursor='hand2')
        rafraichirButton.grid(row=0, column=3, padx=10, pady=10)

        # ========Frame affciche des données des etudiants =======================
        detailsFrame = Frame(self.root, bd=2, relief="groove", bg='#1E02F2')
        detailsFrame.place(x=0.34 * largeur_ecran, y=130, width=0.645 * largeur_ecran, height=500)

        # ========Affichage du champs de recherche =======================
        rechercheLabel = Label(detailsFrame, text='Recherhcer par nom ou par email : ', font=('ubuntu', 12, 'bold'),
                               bg='#1E02F2', fg='white')
        rechercheLabel.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        rechercheText = Entry(detailsFrame, font=('Times new roman', 14), bd=2, relief='groove', fg='white', width=30)
        rechercheText.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        rechercheButon = Button(detailsFrame, text='Rechercher', width=10, cursor='hand2', command=self.rechercherPar)
        rechercheButon.grid(row=0, column=2, padx=10, pady=10)

        AfficherTousButon = Button(detailsFrame, text='Afficher tous', width=10, cursor='hand2',
                                   command=self.afficherEtudiants)
        AfficherTousButon.grid(row=0, column=3, padx=10, pady=10)

        # ========Frame pour afficher les resultat entrer dans le formulaire =======================
        tableFrame =Frame(detailsFrame, bd=2, relief='groove', bg='#1E02F2')
        tableFrame.place(x=10, y=50, width=0.62 * largeur_ecran, height=440)

        defilement_x = Scrollbar(tableFrame, orient="horizontal")
        defilement_y = Scrollbar(tableFrame, orient="vertical")

        etudiantTable = ttk.Treeview(tableFrame, columns=("ine", "nom", "prenom", "email", "adresse", "ville")
                                     ,xscrollcommand = defilement_x.set, yscrollcommand=defilement_y.set)

        defilement_x.pack(side="bottom", fill="x")
        defilement_y.pack(side="right", fill="x")
        defilement_x.config(command=etudiantTable.xview)
        defilement_y.config(command=etudiantTable.yview)

        etudiantTable.heading("ine", text="INE")
        etudiantTable.heading("nom", text="Nom")
        etudiantTable.heading("prenom", text="Prénom")
        etudiantTable.heading("email", text="Email")
        etudiantTable.heading("adresse", text="Adresse")
        etudiantTable.heading("ville", text="Ville")

        etudiantTable['show']='headings'
        etudiantTable.column('ine', width=70)
        etudiantTable.column('nom', width=110)
        etudiantTable.column('prenom', width=110)
        etudiantTable.column('email', width=110)
        etudiantTable.column('adresse', width=230)
        etudiantTable.column('ville', width=110)

        etudiantTable.pack(fill="both", expand=True)

    # Les fonction d'action des buttons
    def enregistrerEtudiant(self):

        is_valid = validate_email(emailLabelEtudiantText.get())
        champs = []
        if ineLabelEtudiantText.get() == "":
            champs.append(ineLabelEtudiantText)

        if nomLabelEtudiantText.get() == "":
            champs.append(nomLabelEtudiantText)

        if prenomLabelEtudiantText.get() == "":
            champs.append(prenomLabelEtudiantText)

        if emailLabelEtudiantText.get() == "":
            champs.append(emailLabelEtudiantText)

        if len(adresseLabelEtudiantText.get(1.0, END +'-1c')) == 0:
            champs.append(adresseLabelEtudiantText)

        if villeLabelEtudiantText.get() == "":
            champs.append(villeLabelEtudiantText)

        if champs != []:
            for champ in champs:
                champ['bg'] = "#C60E0E"
            messagebox.showerror("Erreurs", "Veuillez remplir tous les champs requis !")
            champs.clear()

            return champs

        if not (is_valid):
            messagebox.showerror("Erreurs", "L'email que vous avez saisi n'est pas valide")
            emailLabelEtudiantText['bg'] = "#C60E0E"
        else:
            database = "database/data_base_yekola.db"
            connexion = sqlite3.connect(database)
            cursor = connexion.cursor()

            # Verification si l'identifiant est double
            n = ineLabelEtudiantText.get()
            requete = "SELECT* FROM etudiants WHERE ine = :ine"
            cursor.execute(requete, {'ine': n})
            result = cursor.fetchall()
            if len(result) > 0:
                messagebox.showerror("Erreurs", "L'identifiant de l'etudiant est déja enrégistrer !!!")

            # Verification si l'email n'est double
            em = emailLabelEtudiantText.get()
            requeteEmail = "SELECT* FROM etudiants WHERE email = :email"
            cursor.execute(requeteEmail, {'email': em})

            resultEmail = cursor.fetchall()
            if len(resultEmail) > 0:
                messagebox.showerror("Erreurs", "L'email de l'etudiant est déja enrégistrer !!!")

            else:
                data = (ineLabelEtudiantText.get(), nomLabelEtudiantText.get(), prenomLabelEtudiantText.get(),
                        emailLabelEtudiantText.get(), adresseLabelEtudiantText.get("1.0", END), villeLabelEtudiantText.get())
                req = "INSERT INTO etudiants(ine, nom_etudiant, prenom_etudiant, email, adresse, ville) VALUES (?,?,?,?,?,?)"
                cursor.execute(req, data)
                connexion.commit()
                cursor.close()
                connexion.close()

                messagebox.showinfo("Enregistrement d'un étudiant",
                                "L'enregistrement de l'etudiant " + nomLabelEtudiantText.get() + " " + prenomLabelEtudiantText.get() + " a été enregistré ")
                self.rafraichirEtudiant()

    def modifierEtudiant(self):
        pass

    def supprimerEtudiant(self):
        pass

    def rafraichirEtudiant(self):
        ineLabelEtudiantText.delete(0, END)
        nomLabelEtudiantText.delete(0, END)
        prenomLabelEtudiantText.delete(0, END)
        emailLabelEtudiantText.delete(0, END)
        adresseLabelEtudiantText.delete("1.0", END)
        villeLabelEtudiantText.delete(0, END)

        #Pour change la couleur des bg au momnent du rafraichir
        ineLabelEtudiantText['bg']= "white"
        nomLabelEtudiantText['bg']= "white"
        prenomLabelEtudiantText['bg']= "white"
        emailLabelEtudiantText['bg']= "white"
        adresseLabelEtudiantText['bg']= "white"
        villeLabelEtudiantText['bg']= "white"

    def rechercherPar(self):
        pass

    def afficherEtudiants(self):
        pass

    def gestionFormations(self):
        pass

    def gestionInscriptions(self):
        pass

    def gestionFormateur(self):
        pass


root = Tk()
yekola = GestionEtudiants(root)
root.mainloop()
