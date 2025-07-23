
# Application de Gestion des Formations (Desktop)

##  Présentation

Cette application desktop Windows est un **système de gestion des formations** développé en **Python** avec **Tkinter** pour l'interface graphique et **SQLite** pour la gestion de la base de données.

Elle a été conçue dans le cadre de mon **apprentissage du langage Python et de tkinter** et a pour vocation d'évoluer vers une application complète et professionnelle.

---

##  Fonctionnalités principales

*  Gestion des formations (ajout, modification, suppression, affichage)
*  Gestion des étudiants
*  Gestion des inscriptions

*  Gestion des formateurs
*  Gestion des sessions de formation
*  Recherche et filtrage des données
*  Sauvegarde locale avec base de données **SQLite**
*  Interface utilisateur simple et fonctionnelle avec **Tkinter**

---

##  Technologies utilisées

| Technologie           | Rôle                                           |
| --------------------- | ---------------------------------------------- |
| Python                | Langage principal de développement             |
| Tkinter               | Création de l'interface graphique              |
| SQLite                | Base de données locale                         |
| DB Browser for SQLite | Visualisation et gestion de la base de données |
| PYCharm 2025.1.1.1    | IDE developpement |

---

##  Aperçu de l'application

*(Ajoute ici quelques captures d'écran de l’interface si possible)*

---

##  Structure du projet

```
gestion_formations/
│
├── main.py                  # Point d’entrée de l’application
├── images/                      # Interfaces Tkinter (fenêtres, formulaires)
├── database/                      # Fichiers liés à la base SQLite
│   └── yekola.db         # Base de données SQLite
├──              # Logique métier et interaction avec la base
├── README.md                # Fichier de présentation du projet
```

---

##  Pré-requis

* Python 3.x installé
* DB Browser for SQLite (optionnel, pour visualiser la base de données)

---

##  Lancer l’application

1. Cloner ce dépôt ou copier les fichiers sources
2. Exécuter le fichier principal :

```bash
python main.py
```

---

##  Objectifs futurs

*  Refactorisation du code pour meilleure maintenabilité
*  Amélioration de l’interface utilisateur (Tkinter avancé ou migration vers PyQt/PySide)
*  Migration potentielle vers une version Web ou Mobile (Flutter)
*  Ajout d’un système d’authentification utilisateur
*  Génération de rapports/export en PDF ou Excel

---

##  Auteur

Développé par **NSENGIMANA François** dans le cadre d’un projet d’apprentissage Python.
Ce projet est en constante évolution et a vocation à devenir une application complète de gestion des formations.

---


##  Démo

Voici une courte démonstration de l’application de gestion des formations en action :

 *(Ajoute ici un lien vers une vidéo ou un GIF animé si tu en as un)*

Exemples de fonctionnalités montrées :

* Accueil et navigation dans l'application
* Ajout d'une nouvelle formation
* Affichage et modification des données
* Recherche dans les enregistrements
* Interaction avec la base SQLite
