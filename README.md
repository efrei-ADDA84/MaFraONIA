# Projet DEVOPS_TP2

Ce projet, DEVOPS_TP2, est une solution complète que je fais pour récupérer et afficher les données météorologiques en utilisant l'API OpenWeather. Il encapsule une application Python, utilisant Flask comme framework web, et est conteneurisé avec Docker pour faciliter le déploiement et assurer la cohérence à travers différents environnements.

## 0. Vue d'ensemble

J'utilise Python 3.8 et Flask comme technologies de base, avec Docker pour la conteneurisation. La structure de l'application comprend un fichier `.gitignore` pour le contrôle de version, un `Dockerfile` pour les configurations Docker, `weather_api_wrapper.py` pour l'interface avec l'API OpenWeather, et `app.py` pour l'application web Flask. Je gère la configuration à travers des variables d'environnement, permettant des options de déploiement flexibles.

## 1. Fonctionnalités

- Je récupère les données météorologiques basées sur la latitude et la longitude via l'API OpenWeather.
- J'ai créé une application web Flask pour une interface facile et accessible.
- J'ai conteneurisé avec Docker pour un déploiement cohérent et une scalabilité.
- J'ai utilisé des variables d'environnement pour une configuration sécurisée et flexible.
- J'ai mis en place une pipeline CI/CD automatisée avec GitHub Actions pour un développement et déploiement rationalisés.

## 2. Pour commencer

### 2.1. Prérequis

- Docker
- Python 3.8
- Une clé API OpenWeather
- Flask

### 2.2. Démarrage rapide

1. Cloner le dépôt sur ma machine locale.
2. Naviguer jusqu'au répertoire du projet.
3. Avant de construire l'image Docker, assurez-vous de définir la variable d'environnement `OPENWEATHER_API_KEY` avec votre clé API OpenWeather. Ceci peut être fait en suivant ces étapes :
   - Copier le fichier `.env.devopstp2` à `.env` dans le répertoire du projet.
   - Ouvrer le fichier `.env` et remplacez `YOUR_API_KEY` par votre véritable clé API OpenWeather. INPUT_REQUIRED {Remplacez YOUR_API_KEY par votre clé API OpenWeather}
   Pour les utilisateurs de Unix/Linux/MacOS, vous pouvez aussi exécuter la commande suivante dans votre terminal :
    ```
   export OPENWEATHER_API_KEY=YOUR_API_KEY
    ```
    Ou pour les utilisateurs de Windows, utilisez :
    ```
   set OPENWEATHER_API_KEY=YOUR_API_KEY
    ```
4. Construire l'image Docker avec la commande suivante :
   ```
   docker build -t devops_tp2:latest .
   ```
5. Lancer le conteneur Docker en passant la clé API comme variable d'environnement :
   ```
   docker run --network host -e OPENWEATHER_API_KEY=YOUR_API_KEY devops_tp2:latest
   ```

## 3. Pratiques de sécurité

Pour garantir la sécurité de l'application, je ne stocke pas de données sensibles telles que la clé API OpenWeather et les identifiants Docker Hub dans le code de l'application ou dans les images Docker. À la place, je recommande de les transmettre comme variables d'environnement lors de l'exécution du conteneur Docker. Cela permet de garder les informations sensibles hors du contrôle de version et des images Docker, assurant une meilleure sécurité.

## 4. Configuration de l'environnement de test

Pour configurer l'environnement de test sans exposer votre clé API OpenWeather, suivez les instructions de la section 2.2 pour définir la variable d'environnement `OPENWEATHER_API_KEY` avant d'exécuter les tests. Cela garantit que vos tests peuvent s'exécuter avec les données réelles sans compromettre la sécurité de vos informations d'identification.

## Licence

Copyright (c) 2024.
