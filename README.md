# P13_Foodplaner
Dans le cadre des mes fin d'étude chez openclassrooms nous devions réaliser un projet de notre choix.\
Je suis donc parti sur un planificateur de repas le but est simple vous vous inscrivez et vous connectez \
et vous pouvez créer votre menu pour la semaine ainsi que consulter les recettes des plats choisis

## Installation
- Cloner le projet : ``git clone https://github.com/Blankxx420/P13_Foodplaner.git`` 
- Créer un environnement virtuel : ``python3 -m venv /path/to/new/virtual/environment`` 
- Activer votre environnement : ``source venv/bin/activate`` 
- Installation des modules nécessaires : ``pip install -r requirements.txt``  
- créez votre base de données postgresql : ``CREATE DATABASE nom;``
- Modifier le fichier .env avec les informations de connexion pour la base de données
- Déplacer vous de le repertoire static : ``cd static``
- Installation des packages nodes : ``npm install ``
- Exécuter la commande : `` npm run build ``
- Retourner dans le repertoire racine: ``cd ..``
- Faire les migrations pour la base de données: ``python3  manage.py makemigrations`` et ``python3  manage.py migrate``
- Ajout des plats en base de données : `` python3  manage.py pulldish ``
- Lancer le serveur local `` python3 manage.py runserver``

## Fonctionnalités
- Creation de compte
- modification de compte
- Création de menu
- Suppression de menu
- modification de menu
- consultation de recettes

