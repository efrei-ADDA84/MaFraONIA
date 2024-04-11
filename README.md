# DEVOPS_TP1 Project

## 1. Construction de l'image Docker
Pour conteneuriser l'application Python, j'ai suivi ces étapes suivnates :

1. Je m'assure que Docker est installé sur mon système.
2. Je vais au répertoire racine du projet.
3. Je construis l'image Docker avec la commande suivante :
```
docker build -t devops_tp1:latest .
```

## 2. Exécution de l'image Docker
Après avoir construit l'image, je peux exécuter l'application à l'aide de Docker avec la commande suivante :
```
docker run devops_tp1:latest
```

## 3. Publication sur DockerHub
Pour partager mon image Docker, je suis ces étapes :
1. Je me connecte à DockerHub à partir de la ligne de commande :
```
docker login
```
2. J'étiquette mon image Docker pour correspondre au nom de mon référentiel DockerHub :
```
docker tag devops_tp1:latest mafraonia/devops_tp1:latest  

```
3. Je pousse l'image Docker vers DockerHub :
```
docker push mafraonia/devops_tp1:latest  

```

## 4. Disponibilité sur GitHub
Pour partager mon code, je peux le pousser vers un dépôt GitHub :
1. J'initialise un dépôt Git dans le répertoire du projet :
```
git init
```
2. J'ajoute mes fichiers au dépôt :
```
git add .
```
3. Je valide les modifications :
```
git commit -m "Commit initial avec wrapper Python, Dockerfile et .gitignore"

```
4. Je crée un dépôt sur GitHub et je pousse mon code :
```
git remote add origin https://github.com/efrei-ADDA84/MaFraONIA  

git push -u origin master

```

## Dépendances
- Python 3
- La bibliothèque `requests` pour effectuer des requêtes API. Je l'installe avec `pip install requests`.
- Docker pour la conteneurisation.

