from tkinter import *
from tkinter import ttk, messagebox
from validate_email import validate_email
import sqlite3


class GestionFormations:
    def __init__(self, root):
        self.root = root
        self.root.title("Système de gestion d'un établissement de formations ")

        # Taille ecran
        largeur_ecran = self.root.winfo_screenwidth()
        hauteur_ecran = self.root.winfo_screenheight()
        self.root.geometry('%dx%d' % (largeur_ecran, hauteur_ecran))
        self.root.configure(bg='#DADADA')

        # ========Titre de la fenetre gestion des formations=======================
        titre = Label(self.root, text='Gestion des formations', fg="white", bd=2, relief="groove",
                      font=('ubuntu', 20, 'bold'), padx=20, bg='#1E02F2')
        titre.pack(side="top", fill="x")

        global codeLabelFormationText
        global intituleLabelFormationText
        global langueLabelFormationText
        global adresseLabelEtudiantText
        global emailLabelEtudiantText
        global  rechercheText

        global etudiantTable

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

        titleLabel = Label(manageFrame, text="Information des formations", font=('ubuntu', 18, 'bold'), bg='#1E02F2',
                           fg='white')
        titleLabel.grid(row=0, columnspan=2, pady=15)

        # ========Champs de remplisage des infos sur formulaire de saisi des données des etudiants =======================
        codeLabelFormation = Label(manageFrame, text="Code:", font=('ubuntu', 12, 'bold'), bg='#1E02F2', fg='white')
        codeLabelFormation.grid(row=1, column=0, pady=10, sticky='w')
        codeLabelFormationText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove", width=30)
        codeLabelFormationText.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        intituléLabelFormation = Label(manageFrame, text="Intitulé:", font=('ubuntu', 12, 'bold'), bg='#1E02F2', fg='white')
        intituléLabelFormation.grid(row=2, column=0, pady=10, sticky='w')
        intituleLabelFormationText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove", width=30)
        intituleLabelFormationText.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        prenomLabelEtudiant = Label(manageFrame, text="Langue:", font=('ubuntu', 12, 'bold'), bg='#1E02F2', fg='white')
        prenomLabelEtudiant.grid(row=3, column=0, pady=10, sticky='w')
        langueLabelFormationText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove",
                                         width=30)
        langueLabelFormationText.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        emailLabelEtudiant = Label(manageFrame, text="Niveau:", font=('ubuntu', 12, 'bold'), bg='#1E02F2',
                                   fg='white')
        emailLabelEtudiant.grid(row=4, column=0, pady=10, sticky='w')
        emailLabelEtudiantText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove",
                                       width=30)
        emailLabelEtudiantText.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        adresseLabelEtudiant = Label(manageFrame, text="Objectif:", font=('ubuntu', 12, 'bold'), bg='#1E02F2',
                                     fg='white')
        adresseLabelEtudiant.grid(row=5, column=0, pady=10, sticky='w')
        adresseLabelEtudiantText = Text(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove",height=1.70,
                                         width=30)
        adresseLabelEtudiantText.grid(row=5, column=1, padx=10, pady=10, sticky='w')



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

        rechercheText = Entry(detailsFrame, font=('Times new roman', 14), bd=2, relief='groove', fg='black', width=30)
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

        etudiantTable = ttk.Treeview(tableFrame, columns=("code", "intitulé", "langue", "niveau", "objectif",)
                                     ,xscrollcommand = defilement_x.set, yscrollcommand=defilement_y.set)

        defilement_x.pack(side="bottom", fill="x")
        defilement_y.pack(side="right", fill="x")
        defilement_x.config(command=etudiantTable.xview)
        defilement_y.config(command=etudiantTable.yview)

        etudiantTable.heading("code", text="Code")
        etudiantTable.heading("intitulé", text="Nom")
        etudiantTable.heading("langue", text="Langue")
        etudiantTable.heading("niveau", text="Niveau")
        etudiantTable.heading("objectif", text="Objectif")


        etudiantTable['show']='headings'
        etudiantTable.column('code', width=70)
        etudiantTable.column('intitulé', width=110)
        etudiantTable.column('langue', width=110)
        etudiantTable.column('niveau', width=110)
        etudiantTable.column('objectif', width=230)


        etudiantTable.pack(fill="both", expand=True)

        self.afficherEtudiants()
        etudiantTable.bind("<ButtonRelease-1>", self.recupererDonneesSelectionnees)


    # Les fonction d'action des buttons
    def enregistrerEtudiant(self):

        is_valid = validate_email(emailLabelEtudiantText.get())
        champs = []
        if codeLabelFormationText.get() == "":
            champs.append(codeLabelFormationText)

        if intituleLabelFormationText.get() == "":
            champs.append(intituleLabelFormationText)

        if langueLabelFormationText.get() == "":
            champs.append(langueLabelFormationText)

        if emailLabelEtudiantText.get() == "":
            champs.append(emailLabelEtudiantText)

        if len(adresseLabelEtudiantText.get(1.0, END +'-1c')) == 0:
            champs.append(adresseLabelEtudiantText)

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
            n = codeLabelFormationText.get()
            requete = "SELECT* FROM formations WHERE code_formations = :code"
            cursor.execute(requete, {'code_formations': n})
            result = cursor.fetchall()
            if len(result) > 0:
                messagebox.showerror("Erreurs", "L'identifiant de l'etudiant est déja enrégistrer !!!")

            else:
                data = (codeLabelFormationText.get(), intituleLabelFormationText.get(), langueLabelFormationText.get(),
                        emailLabelEtudiantText.get(), adresseLabelEtudiantText.get("1.0", END),)
                req = "INSERT INTO formations(code_formations, intitule_formation, langue_formation, niveau_formation, objectif,) VALUES (?,?,?,?,?,)"
                cursor.execute(req, data)
                connexion.commit()
                cursor.close()
                connexion.close()

                messagebox.showinfo("Enregistrement de formations",
                                "L'enregistrement de la formations " + intituleLabelFormationText.get() + " " + langueLabelFormationText.get() + " a été enregistré ")
                self.rafraichirEtudiant()
                self.afficherEtudiants()


    def recupererDonneesSelectionnees(self, evenement):
        codeLabelFormationText['state']= 'normal'
        ligne_selectionnee = etudiantTable.focus()
        contenu = etudiantTable.item(ligne_selectionnee)
        #Pour recuperer les valeurs
        ligne = contenu['values']

        codeLabelFormationText.delete(0, END)
        intituleLabelFormationText.delete(0, END)
        langueLabelFormationText.delete(0, END)
        emailLabelEtudiantText.delete(0, END)
        adresseLabelEtudiantText.delete('1.0', END)



        codeLabelFormationText.insert(END, ligne[0])
        intituleLabelFormationText.insert(END, ligne[1])
        langueLabelFormationText.insert(END, ligne[2])
        emailLabelEtudiantText.insert(END, ligne[3])
        adresseLabelEtudiantText.insert(END, ligne[4])

        #Pour rendre le INE verrouiller non modifiable
        codeLabelFormationText['state']= 'disabled'


    def modifierEtudiant(self):


        is_valid = validate_email(emailLabelEtudiantText.get())
        champs = []
        if intituleLabelFormationText.get() == "":
            champs.append(intituleLabelFormationText)

        if langueLabelFormationText.get() == "":
            champs.append(langueLabelFormationText)

        if emailLabelEtudiantText.get() == "":
            champs.append(emailLabelEtudiantText)

        if len(adresseLabelEtudiantText.get(1.0, END +'-1c')) == 0:
            champs.append(adresseLabelEtudiantText)

        if champs != []:
            for champ in champs:
                champ['bg'] = "#C60E0E"
            messagebox.showerror("Erreurs", "Veuillez remplir tous les champs requis !")
            champs.clear()

            return champs

        else:
            database = "database/data_base_yekola.db"
            connexion = sqlite3.connect(database)
            cursor = connexion.cursor()

            # Verification si l'identifiant est double
            n = codeLabelFormationText.get()
            m = emailLabelEtudiantText.get()
            requete = "SELECT* FROM etudiants WHERE ine != :ine AND email = :email"
            cursor.execute(requete, {'ine': n, 'email': m})
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
                data = (intituleLabelFormationText.get(), langueLabelFormationText.get(),
                        emailLabelEtudiantText.get(), adresseLabelEtudiantText.get("1.0", END), villeLabelEtudiantText.get(), ineLabelEtudiantText.get())
                req = "UPDATE  etudiants SET nom_etudiant= ?, prenom_etudiant= ?, email= ?, adresse= ?, ville= ? WHERE ine = ?"
                cursor.execute(req, data)
                connexion.commit()
                cursor.close()
                connexion.close()

                messagebox.showinfo("Modification d'un étudiant",
                                "Modification de l'etudiant " + intituleLabelFormationText.get() + " " + langueLabelFormationText.get() + " a été effectuez ")
                self.rafraichirEtudiant()
                self.afficherEtudiants()
    #Methode pour suppresion
    def supprimerEtudiant(self):
        if codeLabelFormationText.get() != "":
            supp = messagebox.askyesno("Supprimer", "Voulez vous supprimer cet étudiant ?")
            if supp<=0:
                self.afficherEtudiants()
            else:
                database = "database/data_base_yekola.db"
                connexion = sqlite3.connect(database)
                cursor = connexion.cursor()

                data = (codeLabelFormationText.get(),)
                req = "DELETE FROM etudiants WHERE ine=?"
                cursor.execute(req, data)

                connexion.commit()
                cursor.close()
                connexion.close()

                messagebox.showinfo("Confirmation de suppression", "L'etudiant a bien été supprimé")


                self.rafraichirEtudiant()
                self.afficherEtudiants()
        else:
            messagebox.showerror("Selection", "Veuillez selectionner un étudiant à supprimer")

    def rafraichirEtudiant(self):
        codeLabelFormationText['state']= 'normal'

        codeLabelFormationText.delete(0, END)
        intituleLabelFormationText.delete(0, END)
        langueLabelFormationText.delete(0, END)
        emailLabelEtudiantText.delete(0, END)
        adresseLabelEtudiantText.delete("1.0", END)

        #Pour change la couleur des bg au momnent du rafraichir
        codeLabelFormationText['bg']= "white"
        intituleLabelFormationText['bg']= "white"
        langueLabelFormationText['bg']= "white"
        emailLabelEtudiantText['bg']= "white"
        adresseLabelEtudiantText['bg']= "white"

    def rechercherPar(self):
        database = "database/data_base_yekola.db"
        connexion = sqlite3.connect(database)
        cursor = connexion.cursor()

        b = rechercheText.get()

        req = "SELECT * FROM etudiants WHERE nom_etudiant = :nom or email = :email"
        cursor.execute(req, {'nom': b, 'email': b})
        result = cursor.fetchall()

        if len(result) > 0:
            etudiantTable.delete(*etudiantTable.get_children())
            for row in result:
                etudiantTable.insert('', END, values = row)
        else:
            messagebox.showinfo("Recherche", "L'etudiant rechercher n'existe pas")
        cursor.close()
        connexion.close()


    def afficherEtudiants(self):
        database = "database/data_base_yekola.db"
        connexion = sqlite3.connect(database)
        cursor = connexion.cursor()

        req = "SELECT * FROM etudiants"
        cursor.execute(req)
        result = cursor.fetchall()

        if len(result) > 0:
            etudiantTable.delete(*etudiantTable.get_children())
            for row in result:
                etudiantTable.insert('', END, values = row)
        cursor.close()
        connexion.close()

    def gestionFormations(self):
        pass

    def gestionInscriptions(self):
        pass

    def gestionFormateur(self):
        pass


root = Tk()
yekola = GestionFormations(root)
root.mainloop()
