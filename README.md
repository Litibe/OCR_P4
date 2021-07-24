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
sauvegarde des différents renseignements intégrés au cours du jeu.

Sauvegarde des caractéristiques (= 1 Table SQL) des :
- Joueurs inscrits au Club d'échec (avec un ID de joueurs unique)
- Tournois
- Huits joueurs adversaires dans un tournoi 
- Tours de jeu d'un tournoi
- Matchs de jeu d'un tournoi

=> Un fichier "base_sql.db" sera généré, à la racine du dossier OCR_P4, 
au premier lancement du programme pour la gestion et la sauvegarde des données.

La base de données peut-être lu par un programme extérieur comme 
["DB Browser"](https://sqlitebrowser.org)

NB : Dans le menu "Base de données" choix 1 au menu principal, vous pouvez
en saisissant le choix 999 (code caché) ajouter six joueurs
fictifs à titre de démonstrations. Ainsi vous aurez que deux joueurs à créer 
pour le lancement d'un tournoi à huits joueurs.

### Export des données en PDF :
Le programme va créer dans le dossier "OCR_P4", 
un dossier "EXPORT_PDF" contenant la génération des différents fichiers PDF 
au cours de l'utilisation du programme. Cependant, si une même exécution est
de nouveau réalisé, cela "écrasera" le précédent fichier .PDF du même nom.


### Possible traduction du programme : 
Le présent programme a été rédigé en français, vous avez la possibilité de le
traduire intégralement en anglais.
Pour cela vous avez juste à modifier l'import de langue dans les fichiers
suivants en remplaçant "french" par "english".
Le choix de la langue sera déterminante pour la base de données.

```shell
# import pour langue française
from LANGUAGES import french as language
# import pour langue anglaise
from LANGUAGES import english as language
# à modifier dans les fichiers suivants :
/controllers/base.py line 13
/controllers/players.py line 4
/controllers/tournament.py line 6
/models/models.py line 1
/views/base.py line 4
```

 ###Génération Rapport Flake8

Après avoir activé l'environnement virtuel, entrez la commande suivante :
```shell
flake8 --format=html --htmldir=flake_rapport
```
Un rapport sera généré dans le dossier "flake_rapport", avec comme argument 
"max-line-length" défini par défaut à 79 caractères par ligne si non précisé.