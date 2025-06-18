from datetime import *
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from validate_email import validate_email
from PIL import Image, ImageTk


class MenuAccueil:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu d'accueil")

        largeur_ecran = self.root.winfo_screenwidth()
        hauteur_ecran = self.root.winfo_screenheight()
        self.root.geometry('%dx%d' % (largeur_ecran, hauteur_ecran))
        self.root.configure(bg='#DADADA')

        self.arriere_plan = ImageTk.PhotoImage(file="images/yekolaBackground.png")
        arriere_plan = Label(self.root, image=self.arriere_plan)
        arriere_plan.place(x=0, y=0, relwidth=1, relheight=1)

        self.imgGaucheLabel = ImageTk.PhotoImage(file="images/yekolaBackground.png")
        imgGaucheLabel = Label(self.root, image=self.imgGaucheLabel)
        imgGaucheLabel.place(x=200, y=100,width=300, height=450)

        #frame bouton navigation
        frameMenu = Frame(self.root, bd=2,relief="groove", bg="blue")
        frameMenu.place(x=500,y=100, width=700, height=450)

        bouton1 = Button(frameMenu, text="GESTIONS DES ETUDIANTS", font=('Arial', 12, 'bold'), width=28, height=3, cursor="hand2", command= self.gestions_etudiants)
        bouton1.grid(row=0,column=1, padx = 30, pady=40    )

        bouton2 = Button(frameMenu, text="GESTIONS DES FORMATIONS", font=('Arial', 12, 'bold'), width=28, height=3, cursor="hand2", command= self.gestions_formations)
        bouton2.grid(row=0,column=2, padx = 30, pady=40    )

        bouton3 = Button(frameMenu, text="GESTIONS DES INSCRIPTIONS", font=('Arial', 12, 'bold'), width=28, height=3, cursor="hand2", command= self.gestions_inscriptions)
        bouton3.grid(row=1,column=1, padx = 25, pady=2   )

        bouton4 = Button(frameMenu, text="GESTIONS DES FORMATEURS", font=('Arial', 12, 'bold'), width=28, height=3, cursor="hand2", command= self.gestions_formateurs)
        bouton4.grid(row=1,column=2, padx = 25, pady=2   )

        """
        bouton5 = Button(frameMenu, text="Contact me", font=('Arial', 8, 'bold'), width=15, height=2, cursor="hand2", command= self.gestions_formateurs)
        bouton5.grid(row=2,column=1, padx = 80, pady=20, sticky="s")
        """

    def gestions_etudiants(self):
        e= compile(open('./GestionEtudiants.py').read(), './GestionEtudiants.py', 'exec')
        exec(e)
    def gestions_formations(self):
        e= compile(open('./GestionFormations.py').read(), './GestionFormations.py', 'exec')
        exec(e)
    def gestions_inscriptions(self):
        e= compile(open('./GestionInscriptions.py').read(), './GestionInscriptions.py', 'exec')
        exec(e)
    def gestions_formateurs(self):
        pass



if __name__== '__main__':
    root = Tk()
    app = MenuAccueil(root)
    root.mainloop()