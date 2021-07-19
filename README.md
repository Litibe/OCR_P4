# OCR_P4 - Projet P4 - Développez un programme logiciel en Python
### Création d'un logiciel pour le tournoi d'un club d'échec
***
## Présentation
[![Generic badge](https://img.shields.io/badge/Statut-Stable-<COLOR>.svg)](
https://shields.io/)

A été demandé, la réalisation d'un logiciel permettant de réaliser un tournoi,
dans un club d'échec, entre huits joueurs avec la réalisation de quatres tours
de jeu pour déterminer le gagnant du tournoi.
L'utilisateur peut inscrire les joueurs dans une base de données, générer les
quatres tours de jeu, et exporter différents résultats dans la console ainsi
qu'en version PDF.
***
## Prérequis : 
[![made-with-python](
https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](
https://www.python.org/)
[![Python badge](https://img.shields.io/badge/Python->=3.9-blue.svg)](
https://www.python.org/)
***
## Clonage du Repository :
````shell
git clone https://github.com/Litibe/OCR_P4.git
````
***
## Environnement Virtuel :
création de l'environnement virtuel
```shell
python3 -m venv [nom_de_votre_environnement_virtuel] 
```
activation de l'environnement virtuel
### Mac/Linux
````shell
source [nom_de_votre_environnement_virtuel]/bin/activate
````
### Windows
````shell
source .\[nom_de_votre_environnement_virtuel]\Scripts\activate
````

Aller dans le dossier OCR_P4 contenant les fichiers
```shell
cd OCR_P4 
```
***
## Installation des packages nécessaires
````shell
pip install -r requirements.txt 
````
***
## Lancement du programme : 
Exécution du Programme via le fichier principal : main.py présent dans le 
dossier OCR_P4
````shell
python3 main.py 
````
Cette commande produit le resultat suivant : 
en effet, le programme dispose d'une interface dans le terminal. 

```shell
---------------------------------------------------------------
♖♖♖ Bienvenue sur le programme de tournoi du Club d'Echec ! ♖♖♖ 
    Au Sommaire : 
            Choix 1 : Accès au Menu BASE DE DONNEES :
                        - Gestion des joueurs
            Choix 2 : Accès au Menu TOURNOI ♖
            Choix 3 : Accès au Menu RAPPORTS
            
            Choix 0 : Sortie du programme
-------------------------------------------------------------
```


***
## Résultats du programme : 
### Interruption du programme : 
Le programme a été conçu pour enregistrer, en temps réel, les différentes 
actions de l'utilisateur. Le programme peut être fermé par accident
(coupure électricité ou panne ordinateur) et il reprendra au N° du dernier tour
du dernier Tournoi présent en base de données.

### Base de Données : 
Le présent programme utilise une base SQL géré par SQLAlchemy pour la 
sauvegarde des différents renseignements intégrés au cours du jeu .

Sauvegarde des caractéristiques des :
- Tournois
- Listes de Joueurs associées à un Tournoi
- Liste des Joueurs du Club (ID de joueurs Unique)
- Liste des Tours de jeu
- Liste des différents matchs de jeu

=> Un fichier "base_sql.db" sera généré au premier lancement du programme
pour la gestion et la sauvegarde des données.

### Export des données en PDF :
Le programme va créer dans le dossier "OCR_P4", 
un dossier "EXPORT_PDF" contenant la génération des différents fichiers PDF 
au cours de l'utilisation du programme. Cependant, si une même exécution est
de nouveau réalisé, cela "écrasera" le précédent fichier .PDF


### Possible traduction du programme : 
Le présent programme a été rédigé en français, vous avez la possibilité de le
traduire intégralement dans la langue de votre choix, en remplaçant les textes
présents dans le fichier "french.py" présent dans le dossier "LANGUAGUES".
Ce fichier contient tous les prints de console.

 ###Génération Rapport Flake8

Après avoir activé l'environnement virtuel, entrez la commande suivante :
```shell
flake8 --format=html --htmldir=flake_rapport
```
Un rapport sera généré dans le dossier "flake_rapport", avec comme argument 
"max-line-length" défini par défaut à 79 caractères par ligne si non précisé.