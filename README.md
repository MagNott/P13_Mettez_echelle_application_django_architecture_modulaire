# Site web d'Orange County Lettings

Ce repository contient le code source du site web d'Orange County Lettings, un site de location immobilière fictif développé dans le cadre du parcours "Développeur d'application - Python" d'OpenClassrooms.

Ce site web permet aux utilisateurs de consulter des profils de propriétaires et des annonces de locations immobilières. Il est construit avec le framework web Django et utilise une base de données SQLite pour stocker les informations.

## Architecture du projet

Le projet est structuré de la manière suivante :

- `oc_lettings_site/` : Dossier principal du projet Django. Contient les fichiers de configuration principaux du projet Django.
- `lettings/` : Application Django gérant les annonces de locations.
- `profiles/` : Application Django gérant les profils des propriétaires.
- `static/` : Contient les fichiers statiques (CSS, JavaScript, images).
- `templates/` : Contient les templates HTML utilisés pour rendre les pages web (accueil sur le site et pages 404 et 500, les autres templates sont intégrés dans les apps correspondantes).
- `oc-lettings-site.sqlite3` : Fichier de base de données SQLite.

## Documentation complète

La documentation détaillée du projet (architecture modulaire, schémas, description des apps, guides techniques, CI/CD, Sentry, etc.) est disponible sur ReadTheDocs :

https://p13-mettez-echelle-application-django-architecture-modulaire.readthedocs.io/

Ce README contient :

- les informations essentielles pour installer, lancer et déployer le projet,
- un résumé de l’architecture,
- les liens vers la documentation complète
- Les explications sur le déploiement automatisé via GitHub Actions et Render.

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

`cd /path/to/put/project/in`
`git clone https://github.com/MagNott/P13_Mettez_echelle_application_django_architecture_modulaire`

### Créer l'environnement virtuel

- `cd /path/to/P13_Mettez_echelle_application_django_architecture_modulaire`
- `python -m venv venv`
- Activer l'environnement virtuel :
  - macOS / Linux :`source venv/bin/activate`
  - Windows : `.\venv\Scripts\Activate.ps1`
- Pour désactiver l'environnement, `deactivate`

### Installer les dépendances et lancer le site

- `pip install -r requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

### Linting

Pour vérifier le code avec flake8, utilisez la commande suivante après avoir activé l'environnement virtuel :

- `flake8`

### Tests unitaires

Pour exécuter les tests unitaires, utilisez la commande suivante après avoir activé l'environnement virtuel :

- `pytest --cov --cov-fail-under=80`

### Base de données

La base de données est un fichier SQLite, il est récupéré automatiquement lors du clonage du repository.

### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Configuration

Les variables d'environnement suivantes peuvent être configurées pour modifier le comportement du projet en local :

- `export DEBUG=True` : active le mode debug de Django.
- `export SECRET_KEY=<votre_clé_secrète>` : Clé secrète utilisée par Django. Par défaut, une clé de développement est utilisée.
- `export SENTRY_DSN=<votre_dsn_sentry>` : DSN pour Sentry. Par défaut, aucune valeur n'est définie.

## Déploiement

### Vue d'ensemble

Le projet utilise un pipeline CI/CD automatisé via **GitHub Actions** pour déployer l'application en production sur **Render** :

1. **Validation du code** : Exécution automatique des tests (pytest avec couverture ≥ 80%) et vérification de la qualité du code (flake8)
2. **Containerisation** : Construction de l'image Docker et publication sur DockerHub
3. **Déploiement automatique** : Render détecte la nouvelle image et redémarre l'application
4. **Monitoring** : Sentry surveille les erreurs et performances en production

**Schéma du pipeline CI/CD** :

![CI/CD Pipeline](static/images/Pipeline_CICD.png)

Le déploiement automatique se déclenche uniquement sur les pushs ou des merge vers la branche `master` après validation réussie des tests et du linting.

Pour chaque push sur des branches autres que `master`, une vérification des tests et du linting ainsi qu'un build Docker sont effectués et l'image est poussée sur DockerHub avec le tag du `sha du commit` + le tag `latest`, mais sans déploiement automatique.

---

### Prérequis

Pour effectuer un déploiement, les comptes et outils suivants sont nécessaires :

#### Comptes requis

- **GitHub** : Repository du projet avec GitHub Actions activé
- **DockerHub** : Registry pour stocker les images Docker
- **Render** : Plateforme d'hébergement pour l'application en production
- **Sentry** (optionnel) : Service de monitoring des erreurs

#### Conteneur local (pour tests manuels)

- Docker installé et configuré
- Accès SSH au repository GitHub
- CLI Docker connectée à DockerHub (pour pushs manuels d'images)

---

### Marche à suivre pour le déploiement initial

#### 1. Configuration DockerHub

1. Créer un compte sur [hub.docker.com](https://hub.docker.com)
2. Créer un repository public : `votre-username/oc-lettings-site`
3. Générer un Access Token :
   - Aller dans **Account Settings** → **Security** → **New Access Token**
   - Nom : `github-actions-token`
   - Permissions : **Read, Write, Delete**
   - Copier le token généré (il ne sera affiché qu'une seule fois)

#### 2. Configuration Render

1. Créer un compte sur [render.com](https://render.com)
2. Créer un nouveau **Web Service** :
   - **Type** : Docker
   - **Docker Image URL** : `votre-username/oc-lettings-site:latest`
   - **Region** : Choisir la région la plus proche
   - **Instance Type** : Free
3. Configurer les variables d'environnement dans Render :

   `SECRET_KEY`=<générer une clé secrète Django ou modifier celle du projet pour la production>
   `SENTRY_DSN`=<votre DSN Sentry>

   Note : DEBUG est automatiquement à False en production si non défini.

   **Génération de SECRET_KEY** :

   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

4. Récupérer le **Deploy Hook URL** :
   - Aller dans **Settings** → **Deploy Hook**
   - Copier l'URL (format : `https://api.render.com/deploy/srv-xxxxx?key=yyyyy`)

#### 3. Configuration des GitHub Secrets

Ajouter les secrets suivants dans le repository GitHub (**Settings** → **Secrets and variables** → **Actions** → **New repository secret**) :

- `DOCKERHUB_TOKEN` : Token d'accès DockerHub
- `DOCKERHUB_USERNAME` : Nom d'utilisateur DockerHub
- `RENDER_DEPLOY_HOOK_URL` : URL du webhook Render

#### 4. Configuration Sentry (optionnel mais recommandé)

1. Créer un compte sur [sentry.io](https://sentry.io)
2. Créer un nouveau projet Django
3. Copier le DSN fourni (format : `https://xxxxx@oXXXXX.ingest.sentry.io/XXXXXX`)
4. Ajouter le DSN en variable d'environnement local (`SENTRY_DSN`)

---

### Processus de déploiement

#### Déploiement automatique (recommandé)

Le déploiement est entièrement automatisé via GitHub Actions :

1. **Développer et tester localement** :
   Au préalable, tirer une branche depuis `master`, effectuer les modifications, puis exécuter les tests et le linting localement :

   ```bash
   pytest --cov --cov-fail-under=80
   flake8
   ```

2. **Pousser sur la branche actuelle** :

   ```bash
   git add .
   git commit -m "Description des modifications"
   git push
   ```

3. **Le pipeline s'exécute automatiquement** :

   - ✅ Tests unitaires (pytest avec couverture 80%)
   - ✅ Linting (flake8)

4. **Merge request sur la branche master** :

   Une fois fait, il faut merger la branche dans `master` via une pull request sur GitHub.

5. **Le pipeline s'exécute automatiquement** :
   Après le merge, le pipeline s'exécute automatiquement :

   - ✅ Tests unitaires (pytest avec couverture 80%)
   - ✅ Linting (flake8)
   - ✅ Build de l'image Docker
   - ✅ Push vers DockerHub (`latest` + tag avec SHA du commit)
   - ✅ Déclenchement du déploiement Render via webhook

6. **Vérifier le déploiement** :
   - Consulter les logs dans l'onglet **Actions** de GitHub
   - Vérifier le statut sur le dashboard Render
   - Accéder à l'application déployée : `https://votre-app.onrender.com`

---

### Déploiement continu complémentaire (VPS)

Le projet est prévu pour être également déployé sur un VPS personnel avec Apache/Docker. Cette configuration est documentée dans le workflow GitHub Actions (`.github/workflows/github-actions.yml`) et nécessite :

- Configuration Apache avec reverse proxy
- Certificats SSL (Let's Encrypt)
- Clés SSH pour l'authentification GitHub Actions
- Docker installé sur le VPS
- Docker compose installé sur le VPS

Ce déploiement complémentaire utilise Docker Compose pour orchestrer les conteneurs et Apache pour gérer les requêtes entrantes.

Ce docker compose contient la configuration suivante :

- Pull de l'image sur DockerHub (`votre-username/oc-lettings-site:latest`)
- Paramétrage du mapping de ports
- Paramétrage des variables d'environnement :
  - `SENTRY_DSN`
  - `SECRET_KEY`

Ce déploiement est déclenché via une étape additionnelle dans le workflow GitHub Actions après le push de l'image Docker, similaire au déploiement sur Render.

Pour qu'il puisse se produire normalement sans dévoiler de secrets, il est nécessaire de configurer les variables d'environnement et les clés SSH dans les secrets GitHub :

    - `PROJECT_VPS_PATH` : Chemin absolu du projet sur le VPS
    - `VPS_SSH_KEY` : Clé SSH pour l'authentification sur le VPS
    - `SSH_HOST` : Adresse IP ou nom d'hôte du VPS
    - `SSH_KNOWN_HOSTS` : Clé publique SSH connue du VPS
    - `SSH_PRIVATE_KEY` : Clé privée SSH pour l'authentification
    - `SSH_USER` : Nom d'utilisateur SSH pour se connecter au VPS

**Note** : Cette configuration a été faite en complément du déploiement principal sur Render à des fins d'apprentissage.

---
