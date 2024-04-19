"# DEVOPS_TP3

DEVOPS_TP3 est conçu pour automatiser les processus DevOps d'une application, en utilisant les technologies Docker, GitHub et Azure. Ce projet se concentre sur l'amélioration des configurations d'environnement, la gestion des images Docker, le déploiement automatisé des conteneurs et l'intégration des flux de travail de l'intégration continue et du déploiement continu avec GitHub Actions. De plus, il inclut Prometheus pour surveiller les requêtes API, offrant une solution complète pour le déploiement d'applications et l'observabilité.

## Aperçu

L'application utilise une pile basée sur Python, intégrant Flask pour la gestion des requêtes Web, Docker pour la conteneurisation, GitHub pour la gestion du contrôle de source et CI/CD, et les instances de conteneurs Azure pour le déploiement. L'intégration de Prometheus est utilisée pour la surveillance, fournissant des informations sur les métriques des requêtes API.

## Fonctionnalités

- **Mise à jour de la configuration de l'environnement :** Simplifie les configurations d'environnement de l'application.
- **Gestion des images Docker :** Facilite l'automatisation de la création et de la mise à jour des images Docker.
- **Déploiement automatisé des conteneurs :** Utilise GitHub Actions pour un déploiement efficace des conteneurs vers les instances de conteneurs Azure.
- **Intégration continue et déploiement :** Implémente GitHub Actions pour rationaliser les flux de travail de développement.
- **Surveillance des requêtes API :** Intègre Prometheus pour suivre les métriques des requêtes API, améliorant les capacités de surveillance.

## Pour commencer

### Exigences

- Docker
- Python 3.8 ou supérieur
- Flask
- Une clé API OpenWeather
- Compte GitHub
- Accès au registre de conteneurs Azure et aux instances de conteneurs Azure

### Démarrage rapide

1. **Clonez le dépôt** et naviguez vers le répertoire du projet.
2. **Construisez l'image Docker** : Exécutez `docker build -t devops_tp3:latest .` pour créer une image Docker nommée `devops_tp3:latest`.
3. **Exécutez le conteneur Docker** : Utilisez `docker run --network host -e OPENWEATHER_API_KEY=VOTRE_CLÉ_API devops_tp3:latest` pour démarrer l'application. Remplacez `VOTRE_CLÉ_API` par votre véritable clé API OpenWeather.
4. **Exécutez API App** : Utilisez cette commande `python app.py`
5. **Configuration de GitHub Actions** : Configurez GitHub Actions en mettant en place des flux de travail dans `.github/workflows/ci_cd.yml` pour automatiser les processus CI/CD. Cela inclut le linting, les tests, la construction et le déploiement de l'application.
6. **Intégration continue et déploiement** : Le pipeline CI/CD automatise le processus d'intégration des changements, de construction de l'image Docker et de son déploiement sur les instances de conteneurs Azure (ACI).
    ```
   python git_commit_push.py
    ```
7. **Surveillance avec Prometheus** : Accédez au point de terminaison `/metrics` pour voir les métriques de Prometheus, qui suivent entre autres les comptages des requêtes API.
    ```
   http://localhost/metrics
    ```

### Déploiement sur les instances de conteneurs Azure (ACI)

- **Configuration Azure** : Assurez-vous d'avoir un compte Azure et un accès au registre de conteneurs Azure (ACR) et aux instances de conteneurs Azure (ACI).
- **Secrets GitHub** : Configurez les secrets GitHub avec les informations d'identification Azure, les détails ACR et la clé API OpenWeather pour un accès sécurisé pendant les processus CI/CD.
- **Déploiement ACI** : Le flux de travail GitHub Actions inclut des étapes pour déployer le conteneur Docker sur ACI, en utilisant l'interface de ligne de commande Azure pour les tâches de déploiement.

### Surveillance et journalisation

- **Intégration de Prometheus** : L'application expose un point de terminaison `/metrics` pour que Prometheus puisse récupérer les métriques de l'application,
    ```
   http://localhost/metrics
    ```