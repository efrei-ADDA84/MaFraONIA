# DEVOPS_TP4

Ce projet se concentre sur l'utilisation de la gestion des machines virtuelles (VM) Azure à travers Terraform à des fins DevOps. L'objectif est d'automatiser la création, la configuration et la gestion d'une VM Azure, spécialement adaptée pour les applications DevOps, incluant la configuration de Docker et la sécurisation de l'accès SSH.

## Vue d'ensemble

DEVOPS_TP4 utilise Terraform pour l'Infrastructure en tant que Code (IaC) afin d'automatiser la mise en place des ressources Azure. Cela comprend la création d'un réseau virtuel, d'un sous-réseau dans ce réseau, et d'une VM configurée avec Ubuntu 22.04. Il démontre l'utilisation de Terraform pour automatiser les tâches d'infrastructure cloud, ce qui est crucial pour des pratiques DevOps scalables et efficaces.

L'architecture s'articule autour des services Azure, avec des scripts Terraform pour configurer et gérer ces services. Le projet est intégré avec GitHub pour le contrôle de version et utilise Azure CLI à des fins d'authentification.

## Fonctionnalités

- **Provisionnement Automatisé de VM :** Création d'une VM Standard_D2s_v3 dans la région 'ouest europe' avec Ubuntu 22.04.
- **Accès SSH :** Configuration SSH sécurisée utilisant des clés SSH générées pour accéder à la VM.
- **Installation de Docker :** Un script de démarrage est utilisé pour installer automatiquement Docker sur la VM, la préparant pour des applications basées sur des conteneurs.
- **Configuration Dynamique :** Les variables Terraform et les secrets GitHub permettent des déploiements personnalisables et reproductibles.

## Pour Commencer

### Prérequis

- Terraform
- Azure CLI
- Git

### Démarrage Rapide

1. Clonez le dépôt sur votre machine locale.
2. Naviguez vers le répertoire du projet et exécutez `terraform init` pour initialiser Terraform.
3. Générez une paire de clés SSH si vous n'en avez pas déjà une.
4. Exécutez `terraform apply` pour créer les ressources Azure. Fournissez un `IDENTIFIANT_EFREI` unique lorsqu'il vous sera demandé.
5. Connectez-vous à la VM en utilisant SSH avec la clé privée générée.

## Développement et Opérations

### Contrôle de Version

Les configurations Terraform pour ce projet sont contrôlées par version en utilisant Git, avec le dépôt hébergé sur GitHub. Pour contribuer ou modifier la configuration de l'infrastructure, suivez les étapes ci-dessous :

### Clonage du Dépôt

1. Assurez-vous que Git est installé sur votre machine.
2. Clonez le dépôt en utilisant la commande suivante :

```bash
git clone https://github.com/efrei-ADDA84/MaFraONIA.git
cd MaFraONIA
```

### Flux de Travail Terraform

1. **Initialisation de Terraform** - Avant d'appliquer des modifications, initialisez l'espace de travail Terraform en exécutant :

```bash
terraform init
```
2. **Formatage Terraform** - Formatez correctement le code Terraform en exécutant :

```bash
terraform fmt
```

2. **Application de la Configuration** - Pour créer ou mettre à jour l'infrastructure, exécutez :

```bash
terraform apply
```

Lorsqu'il vous sera demandé, entrez un `IDENTIFIANT_EFREI` unique avec `var.subscription_id` ou configurez-le comme variable d'environnement.

3. **Destruction de l'Infrastructure** - Pour supprimer toutes les ressources gérées par Terraform, exécutez :

```bash
terraform destroy
```

Assurez-vous de comprendre l'impact de cette commande car elle supprimera toutes les ressources cloud définies dans les configurations Terraform.

## Authentification Azure pour Terraform

Pour permettre à Terraform de gérer les ressources dans votre compte Azure, vous devez créer un principal de service et configurer Terraform avec ses identifiants.

### Création d'un Principal de Service

1. Installez Azure CLI sur votre machine.
2. Connectez-vous à Azure CLI en utilisant `az login`.
3. Créez un principal de service en utilisant la commande suivante :

```bash
az ad sp create-for-rbac --name "TerraformSP" --role="Contributor" --scopes="/subscriptions/VOTRE_ID_ABONNEMENT"
```

Remplacez `VOTRE_ID_ABONNEMENT` par votre véritable ID d'abonnement Azure.

### Configuration de Terraform

Ajoutez le bloc suivant à votre fichier `main.tf`, en remplaçant les espaces réservés par les valeurs réelles obtenues lors de la création du principal de service :

```hcl
provider "azurerm" {
  features {}
  skip_provider_registration = true

  subscription_id = "VOTRE_ID_ABONNEMENT" 

}
```

### Licence

Copyright (c) 2024.

---