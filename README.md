# Site web d'Orange County Lettings

Ce repository contient le code source du site web d'Orange County Lettings, un site de location immobilière fictif développé dans le cadre du parcours "Développeur d'application - Python" d'OpenClassrooms.

Ce site web permet aux utilisateurs de consulter des profils de propriétaires et des annonces de locations immobilières. Il est construit avec le framework web Django et utilise une base de données SQLite pour stocker les informations.

## Architecture du projet
Le projet est structuré de la manière suivante :
- `lettings/` : Application Django gérant les annonces de locations.
- `oc_lettings_site/` : Dossier principal du projet Django. Contient les fichiers de configuration principaux du projet Django.
- `profiles/` : Application Django gérant les profils des propriétaires.
- `static/` : Contient les fichiers statiques (CSS, JavaScript, images).
- `templates/` : Contient les templates HTML utilisés pour rendre les pages web (accueil sur le site et pages 404 et 500, les autres templates sont intégrés dans les apps correspondantes).
- `oc-lettings-site.sqlite3` : Fichier de base de données SQLite.

## Documentation complète
La documentation détaillée du projet (architecture modulaire, schémas, description des apps, guides techniques, CI/CD, Sentry, etc.) est disponible sur ReadTheDocs :

https://p13-mettez-echelle-application-django-architecture-modulaire.readthedocs.io/

Ce README contient uniquement :
- les informations essentielles pour installer, lancer et déployer le projet,
- un résumé de l’architecture,
- les liens vers la documentation complète.


## Installation et exécution en local

### Prérequis

- Python 3.10 ou supérieur
- Pip
- Git (pour cloner le dépôt)
- Le module `venv` pour créer des environnements virtuels
- Connexion Internet pour télécharger les dépendances
- Docker (optionnel, pour le déploiement local en conteneurs)


Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).


### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/MagNott/P13_Mettez_echelle_application_django_architecture_modulaire`

### Créer l'environnement virtuel

- `cd /path/to/P13_Mettez_echelle_application_django_architecture_modulaire`
- `python -m venv venv`
- Activer l'environnement virutel : 
    - macOS / Linux :`source venv/bin/activate`
    - Windows : `.\venv\Scripts\Activate.ps1`
- Vérifier que l’environnement est actif : la commande `python --version` doit afficher une version ≥ 3.10.
- Pour désactiver l'environnement, `deactivate`

### Exécuter le site

- `cd /path/to/P13_Mettez_echelle_application_django_architecture_modulaire`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

### Linting

Pour vérifier le code avec flake8, utilisez la commande suivante après avoir activé l'environnement virtuel :
```bash
cd /path/to/P13_Mettez_echelle_application_django_architecture_modulaire
```
```bash
source venv/bin/activate
```
```bash
flake8
```

### Tests unitaires

Pour exécuter les tests unitaires, utilisez la commande suivante après avoir activé l'environnement virtuel :
- `cd /path/to/P13_Mettez_echelle_application_django_architecture_modulaire`
- `source venv/bin/activate`
```bash
pytest --cov --cov-fail-under=80
```


### Base de données

Le projet utilise une base SQLite par défaut.  
Aucune action manuelle n'est nécessaire : la base est automatiquement créée et migrée lors du premier lancement du serveur Django.


### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`


## Configuration 
Les variables d'environnement suivantes peuvent être configurées pour modifier le comportement du projet :

- `DEBUG` : Si défini à `1`, active le mode debug de Django. Par défaut, `0`.
- `SECRET_KEY` : Clé secrète utilisée par Django. Par défaut, une clé de développement est utilisée.
- `SENTRY_DSN` : DSN pour Sentry. Par défaut, aucune valeur n'est définie.


## Déploiement avec Docker
Un pipeline CI/CD est configuré pour déployer automatiquement le projet sur render à chaque push sur la branche `main` qui :
    - lance les tests
    - construit l'image Docker
    - pousse le code
    - déploie automatiquement sur render.com

### Configuration requise 
- Variables d'environnement sur render.com :
  - `DEBUG` : `0`
  - `SECRET_KEY` : une clé secrète sécurisée
  - `SENTRY_DSN` : (optionnel) DSN pour Sentry





