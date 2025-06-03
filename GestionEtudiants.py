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

root = Tk()
yekola = GestionEtudiants(root)
root.mainloop()
