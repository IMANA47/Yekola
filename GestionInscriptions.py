from datetime import *
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3




class GestionInscriptions:
    def __init__(self, root):
        self.root = root
        self.root.title("Système de gestion d'un établissement de formations ")

        # Taille ecran
        largeur_ecran = self.root.winfo_screenwidth()
        hauteur_ecran = self.root.winfo_screenheight()
        self.root.geometry('%dx%d' % (largeur_ecran, hauteur_ecran))
        self.root.configure(bg='#DADADA')

        # ========Titre de la fenetre gestion des etudiants=======================
        titre = Label(self.root, text='Gestion des inscriptions', fg="white", bd=2, relief="groove",
                      font=('ubuntu', 20, 'bold'), padx=20, bg='#1E02F1')
        titre.pack(side="top", fill="x")

        global ineLabelEtudiantText
        global nomLabelEtudiantText
        global prenomLabelEtudiantText
        global adresseLabelEtudiantText
        global emailLabelEtudiantText
        global villeLabelEtudiantText
        global  rechercheText
        global rechercheFormationDeroulantText
        global formationsEtudiantTable
        global formationDeroulant

        # ========Frame menu principale =======================
        menuFrame = Frame(self.root, bd=2, relief="groove", bg='#1E02F2')
        menuFrame.place(x=20, y=50, width=0.97 * largeur_ecran, height=80)

        # ========les bouton des differents menu principale =======================
        gestionFormationButon = Button(menuFrame, text="Gestion des Formations", font=('ubuntu', 16, 'bold'), width=23,
                                       cursor='hand2', command=self.gestionFormations)
        gestionFormationButon.grid(row=0, column=1, padx=10, pady=10)

        gestionInscriptionButon = Button(menuFrame, text="Gestion des étudiants", font=('ubuntu', 16, 'bold'),
                                         width=23, cursor='hand2', command=self.gestionEtudiants)
        gestionInscriptionButon.grid(row=0, column=2, padx=10, pady=10)

        gestionFormateurButon = Button(menuFrame, text="Gestion des formateurs", font=('ubuntu', 16, 'bold'), width=23,
                                       cursor='hand2', command=self.gestionFormateur)
        gestionFormateurButon.grid(row=0, column=3, padx=10, pady=10)

        # ========Formulaire de saisi des données des etudiants =======================
        manageFrame = Frame(self.root, bd=2, relief="groove", bg='#1E02F2')
        manageFrame.place(x=20, y=128, width=0.32 * largeur_ecran, height=310)

        titleLabel = Label(manageFrame, text="Inscription à une formation", font=('ubuntu', 14, 'bold'), bg='#1E02F2',
                           fg='white')
        titleLabel.grid(row=0, columnspan=2, pady=10)

        # ========Champs de remplisage des infos sur formulaire de saisi des données des etudiants =======================
        ineLabelEtudiant = Label(manageFrame, text="INE:", font=('ubuntu', 12, 'bold'), bg='#1E02F2', fg='white')
        ineLabelEtudiant.grid(row=1, column=0, pady=2, sticky='w')
        ineLabelEtudiantText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove", width=30)
        ineLabelEtudiantText.grid(row=1, column=1, padx=10, pady=2, sticky='w')

        nomLabelEtudiant = Label(manageFrame, text="Nom:", font=('ubuntu', 12, 'bold'), bg='#1E02F2', fg='white')
        nomLabelEtudiant.grid(row=2, column=0, pady=4, sticky='w')
        nomLabelEtudiantText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove", width=30)
        nomLabelEtudiantText.grid(row=2, column=1, padx=10, pady=4, sticky='w')

        prenomLabelEtudiant = Label(manageFrame, text="Prénom:", font=('ubuntu', 12, 'bold'), bg='#1E02F2', fg='white')
        prenomLabelEtudiant.grid(row=3, column=0, pady=4, sticky='w')
        prenomLabelEtudiantText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove",
                                        width=30)
        prenomLabelEtudiantText.grid(row=3, column=1, padx=10, pady=4, sticky='w')

        emailLabelEtudiant = Label(manageFrame, text="Adresse email:", font=('ubuntu', 12, 'bold'), bg='#1E02F2',
                                   fg='white')
        emailLabelEtudiant.grid(row=4, column=0, pady=4, sticky='w')
        emailLabelEtudiantText = Entry(manageFrame, font=('Times new roman', 12, 'bold'), bd=2, relief="groove",
                                       width=30)
        emailLabelEtudiantText.grid(row=4, column=1, padx=10, pady=4, sticky='w')

        formationLabel = Label(manageFrame,text="Formations ", font=('ubuntu', 12, 'bold'), bg='#1E02F2',
                                   fg='white')
        formationLabel.grid(row=5, column=0, pady=4, sticky='w')

        formationDeroulant = ttk.Combobox(manageFrame, font=('Times new roman', 12))
        formationDeroulant['values'] = (self.recupererFormations())
        formationDeroulant.grid(row=5, column=1, padx=10, pady=4, sticky='w')


        # ========ajout du espace des boutons d'action de gestion  des etudiants =================
        boutonFrame = Button(manageFrame, bd=2, relief="groove", bg='#1E02F2')
        boutonFrame.place(x=150, y=220, width=0.18 * largeur_ecran, height=70)

        # ========ajout des boutons d'action de gestions des etudiants =================
        inscrireButton = Button(boutonFrame, text='Inscrire', width=8, height=2, command=self.inscrireEtudiant,
                                  cursor='hand2')
        inscrireButton.grid(row=0, column=1, padx=30, pady=5)

        desinscrireButton = Button(boutonFrame, text='desinscrire', width=8, height=2,cursor='hand2', command=self.desinscrireEtudiant
                                )
        desinscrireButton.grid(row=0, column=2, padx=10, pady=10)

        #=======Frame pour affichage des formations auxquelles est inscrit un etudiant =========
        formationsEtudiantFrame = Frame(self.root, bd=2, relief="groove", bg='#1E02F2')
        formationsEtudiantFrame.place(x=20, y=445, width=0.32 * largeur_ecran, height=205)

        formationEtudiantLabel = Label(formationsEtudiantFrame, text="Formations auxquelles est inscrit : "+ nomLabelEtudiantText.get(),fg="white",font=('ubuntu', 12, 'bold'), bg='#1E02F2')
        formationEtudiantLabel.grid(row=0, column=0, pady=5, padx=5, sticky='w')

        formationsTableFrame = Frame(formationsEtudiantFrame, bd=2, relief='groove', bg='#1E02F2')
        formationsTableFrame.place( x=3, y=35, width=0.32 * largeur_ecran, height=165)

        defilement_x = Scrollbar(formationsTableFrame, orient="horizontal")
        defilement_y = Scrollbar(formationsTableFrame, orient="vertical")

        formationsEtudiantTable = ttk.Treeview(formationsTableFrame, columns=("code", "intitulé", "date_inscription")
                                               , xscrollcommand=defilement_x.set, yscrollcommand=defilement_y.set)

        defilement_x.pack(side="bottom", fill="x")
        defilement_y.pack(side="right", fill="x")
        defilement_x.config(command=formationsEtudiantTable.xview)
        defilement_y.config(command=formationsEtudiantTable.yview)

        formationsEtudiantTable.heading("code", text="Code")
        formationsEtudiantTable.heading("intitulé", text="Intitulé")
        formationsEtudiantTable.heading("date_inscription", text="Date d'inscription")

        formationsEtudiantTable['show'] = 'headings'
        formationsEtudiantTable.column('code', width=10)
        formationsEtudiantTable.column('intitulé', width=45)
        formationsEtudiantTable.column('date_inscription', width=45)

        formationsEtudiantTable.pack(fill="both", expand=True)


        # ========Frame affciche des données des etudiants =======================
        detailsFrame = Frame(self.root, bd=2, relief="groove", bg='#1E02F2')
        detailsFrame.place(x=0.34 * largeur_ecran, y=130, width=0.645 * largeur_ecran, height=520)


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

        # ========Affichage du champs de recherche des formations =======================
        formationRechercheLabel = Label(detailsFrame, text='Selectionner une formation : ', font=('ubuntu', 12, 'bold'),
                               bg='#1E02F2', fg='white')
        formationRechercheLabel.grid(row=1, column=0, padx=10, pady=2, sticky='w')

        rechercheFormationDeroulantText = ttk.Combobox(detailsFrame, font=('ubuntu', 12, 'bold'))
        rechercheFormationDeroulantText['values'] = (self.recupererFormations())
        rechercheFormationDeroulantText.grid(row=1, column=1, pady=4, padx=5, sticky ='w')

        rechercheFormationButon = Button(detailsFrame, command=self.rechercherParFormation, text="Rechercher", width=10)
        rechercheFormationButon.grid(row=1, column=2, pady=4, padx=5)

        # ========Frame pour afficher les resultat entrer dans le formulaire =======================
        tableFrame =Frame(detailsFrame, bd=2, relief='groove', bg='#1E02F2')
        tableFrame.place(x=10, y=96, width=0.62 * largeur_ecran, height=420)

        defilement_x = Scrollbar(tableFrame, orient="horizontal")
        defilement_y = Scrollbar(tableFrame, orient="vertical")

        formationsEtudiantTable = ttk.Treeview(tableFrame, columns=("ine", "nom", "prenom", "email", "adresse", "ville")
                                               , xscrollcommand = defilement_x.set, yscrollcommand=defilement_y.set)

        defilement_x.pack(side="bottom", fill="x")
        defilement_y.pack(side="right", fill="x")
        defilement_x.config(command=formationsEtudiantTable.xview)
        defilement_y.config(command=formationsEtudiantTable.yview)

        formationsEtudiantTable.heading("ine", text="INE")
        formationsEtudiantTable.heading("nom", text="Nom")
        formationsEtudiantTable.heading("prenom", text="Prénom")
        formationsEtudiantTable.heading("email", text="Email")
        formationsEtudiantTable.heading("adresse", text="Adresse")
        formationsEtudiantTable.heading("ville", text="Ville")

        formationsEtudiantTable['show']= 'headings'
        formationsEtudiantTable.column('ine', width=70)
        formationsEtudiantTable.column('nom', width=110)
        formationsEtudiantTable.column('prenom', width=110)
        formationsEtudiantTable.column('email', width=110)
        formationsEtudiantTable.column('adresse', width=230)
        formationsEtudiantTable.column('ville', width=110)

        formationsEtudiantTable.pack(fill="both", expand=True)

        self.afficherEtudiants()
        formationsEtudiantTable.bind("<ButtonRelease-1>", self.recupererDonneesSelectionnees)

    # Methode pour inscrire un etudiant a une formation
    def inscrireEtudiant(self):
        database = "database/data_base_yekola.db"
        connexion = sqlite3.connect(database)
        cursor = connexion.cursor()

        if formationDeroulant.get() == "":
            messagebox.showerror("Erreurs", "Veuillez choisir une formation")
        else:
            data1 = (ineLabelEtudiantText.get(), formationDeroulant.get())
            req1 = "SELECT * FROM inscriptions WHERE ine_etudiant = ? AND code_formation=?"
            cursor.execute(req1, data1)
            result1 = cursor.fetchall()

            if len(result1) != 0:
                messagebox.showerror("Erreur", "L'étudiant ayant l'INE : " + ineLabelEtudiantText.get()+" est déja "
                                                                                    "inscrit à la formation choisie")
            else:
                ma_date = date.today()
                date_actuelle = ma_date.strftime("%d/%m/%y")
                data2 = (ineLabelEtudiantText.get(), formationDeroulant.get(), date_actuelle)
                req2 = "INSERT INTO inscriptions(ine_etudiant, code_formation,date_inscription) VALUES(?,?,?)"
                cursor.execute(req2, data2)
                connexion.commit()

                messagebox.showinfo("Inscription à une formation ","L'inscription de l'etudiant " +
                                    nomLabelEtudiantText.get() + " à la formation ayant le code : " +
                                    formationDeroulant.get()+ " a été faite avec succès !!")

                self.afficherEtudiants()
                self.afficher_formations_etudiant()
        cursor.close()
        connexion.close()

    # Methode pour desinscrire un etudiant a une formation
    def desinscrireEtudiant(self):
        database = "database/data_base_yekola.db"
        connexion = sqlite3.connect(database)
        cursor = connexion.cursor()

        if formationDeroulant.get() == "":
            messagebox.showerror("Erreur", "Veuillez choisir une formation !")
        else:
            data = (ineLabelEtudiantText.get(), formationDeroulant.get())
            req = "SELECT * FROM inscriptions WHERE ine_etudiant = ? AND code_formation=?"
            cursor.execute(req, data)
            result1 = cursor.fetchall()
            if len(result1) == 0:
                messagebox.showerror("Erreur", "Veuillez choisir une formation  à laquelle est inscrit l'etudiant !")
            else:
                supp = messagebox.askyesno("Désinscription", "Vous le vous désinscrire l'etudiant ")
                if supp>0:
                    req1 = "DELETE FROM inscriptions WHERE ine_etudiant = ? AND code_formation = ?"

                    cursor.execute(req1, data)
                    connexion.commit()

                    messagebox.showinfo("Désinscription", "La désinscription de l'étudiant "+ nomLabelEtudiantText.get() +" été effectué")

            self.afficher_formations_etudiant()
        cursor.close()
        connexion.close()


    #Methode pour afficher la formation dans le quelle un etudiant sélectionné est inscrit
    def afficher_formations_etudiant(self):
        database = "database/data_base_yekola.db"
        connexion = sqlite3.connect(database)
        cursor = connexion.cursor()

        data = (ineLabelEtudiantText.get(),)
        req = """SELECT formations.code_formations, formations.intitule_formation, inscriptions.date_inscription FROM
        formations JOIN inscriptions ON formations.code_formations = inscriptions.code_formation
        JOIN etudiants ON ine = inscriptions.ine_etudiant AND inscriptions.ine_etudiant = ?"""

        cursor.execute(req, data)
        results = cursor.fetchall()

        if len(results) > 0:
            self.formationsEtudiantTable.delete(*self.formationsEtudiantTable.get_children())
            for ligne in results:
                self.formationsEtudiantTable.insert('', END, values = ligne)

        cursor.close()
        connexion.close()




    def rechercherPar(self):

        database = "database/data_base_yekola.db"
        connexion = sqlite3.connect(database)
        cursor = connexion.cursor()

        b = rechercheText.get()

        req = "SELECT * FROM etudiants WHERE nom_etudiant = :nom or email = :email"
        cursor.execute(req, {'nom': b, 'email': b})
        result = cursor.fetchall()

        if len(result) > 0:
            formationsEtudiantTable.delete(*formationsEtudiantTable.get_children())
            for row in result:
                formationsEtudiantTable.insert('', END, values = row)
        else:
            messagebox.showinfo("Recherche", "L'etudiant rechercher n'existe pas")
        cursor.close()
        connexion.close()

    #Methode afficher etudiant
    def afficherEtudiants(self):
        database = "database/data_base_yekola.db"
        connexion = sqlite3.connect(database)
        cursor = connexion.cursor()

        req = "SELECT * FROM etudiants"
        cursor.execute(req)
        result = cursor.fetchall()

        if len(result) > 0:
            formationsEtudiantTable.delete(*formationsEtudiantTable.get_children())
            for row in result:
                formationsEtudiantTable.insert('', END, values=row)
        cursor.close()
        connexion.close()

    def recupererFormations(self):
        database = "database/data_base_yekola.db"
        connexion = sqlite3.connect(database)
        cursor = connexion.cursor()

        req = "SELECT * FROM formations"
        cursor.execute(req)

        print(cursor)

        result = []
        for data in cursor :
            result.append(data[0])
        cursor.close()
        connexion.close()
        return result

    def rechercherParFormation(self):
        database = "database/data_base_yekola.db"
        connexion = sqlite3.connect(database)
        cursor = connexion.cursor()

        if rechercheFormationDeroulantText.get() == "":
            messagebox.showerror("Erreurs", "Veuillez choisir une formation")
        else :
            data = (rechercheFormationDeroulantText.get(),)

            req = """SELECT etudiants.ine, etudiants.nom_etudiant, etudiants.prenom_etudiant, etudiants.email,
            etudiants.adresse,etudiants.ville FROM etudiants
            JOIN inscriptions ON  etudiants.ine =  inscriptions.ine_etudiant
            AND
            inscriptions.code_formation = ?
            """
        cursor.execute(req, data)
        results = cursor.fetchall()

        if len(results) > 0:
            formationsEtudiantTable.delete(*self.formationsEtudiantTable.get_children())
            for row in results:
                formationsEtudiantTable.insert('', END, values = row)
        else:
            messagebox.showinfo("Information", "Il n'existe aucun étudiant inscrit à la formation")

        cursor.close()
        connexion.close()



    #Methode pour recuperer donnees selectionné
    def recupererDonneesSelectionnees(self, evenement):
        #Pour l'etat des champs
        ineLabelEtudiantText['state'] = 'normal'
        nomLabelEtudiantText['state'] = 'normal'
        prenomLabelEtudiantText['state'] = 'normal'
        emailLabelEtudiantText['state'] = 'normal'

        ligne_selectionnee = formationsEtudiantTable.focus()
        contenu = formationsEtudiantTable.item(ligne_selectionnee)
        # Pour recuperer les valeurs
        ligne = contenu['values']

        ineLabelEtudiantText.delete(0, END)
        nomLabelEtudiantText.delete(0, END)
        prenomLabelEtudiantText.delete(0, END)
        emailLabelEtudiantText.delete(0, END)

        ineLabelEtudiantText.insert(END, ligne[0])
        nomLabelEtudiantText.insert(END, ligne[1])
        prenomLabelEtudiantText.insert(END, ligne[2])
        emailLabelEtudiantText.insert(END, ligne[3])

        # Pour rendre le INE verrouiller non modifiable
        ineLabelEtudiantText['state'] = 'disabled'
        nomLabelEtudiantText['state'] = 'disabled'
        prenomLabelEtudiantText['state'] = 'disabled'
        emailLabelEtudiantText['state'] = 'disabled'

        self.fromationsEtudiantTable.delete(*self.fromationsEtudiantTable.get_children())
        self.afficher_formations_etudiant()



    def gestionFormations(self):
        pass
    def gestionEtudiants(self):
        pass
    def gestionFormateur(self):
        pass








root = Tk()
yekola = GestionInscriptions(root)
root.mainloop()