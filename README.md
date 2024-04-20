# DEVOPS_TP4

DEVOPS_TP4 automates the creation and management of an Azure Virtual Machine (VM) for DevOps tasks, utilizing Infrastructure as Code (IaC) practices through Terraform. This project emphasizes on provisioning a secure, accessible, and Docker-equipped VM within Azure, simplifying DevOps workflows.

## Overview

The architecture leverages Azure services, managed by Terraform configurations to ensure repeatability and scalability. The codebase includes definitions for Azure resources like VMs, network configurations, and security settings, all geared towards a DevOps setup. Technologies used include Terraform for IaC, Azure CLI for authentication, and GitHub for source control and secrets management.

## Features

- **Azure VM Creation**: Provisioning of a VM named 'devops-<IDENTIFIANT_EFREI>', tailored for DevOps tasks.
- **Public IP Assignment**: Ensures the VM is accessible over the internet.
- **SSH Access**: Secure SSH setup for remote access.
- **Docker Installation**: Automated Docker setup using a startup script.
- **Terraform and GitHub Integration**: Utilizes Terraform for infrastructure management and GitHub for code hosting and secrets management.

## Getting started

### Requirements

- Azure CLI installed and configured
- Terraform installed
- GitHub account

### Quickstart

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Initialize Terraform using `terraform init`.
4. Apply the Terraform configuration with `terraform apply`, ensuring you have set up the necessary Azure credentials.
5. SSH into the VM using the generated SSH keys for any further configurations or checks.

### License

Copyright (c) 2024. All rights reserved.