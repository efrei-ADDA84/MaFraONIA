# DEVOPS_TP4

This project focuses on leveraging Azure Virtual Machine (VM) management through Terraform for DevOps purposes. The goal is to automate the creation, configuration, and management of an Azure VM, specifically tailored for DevOps applications, including setting up Docker and ensuring secure SSH access.

## Overview

DEVOPS_TP4 utilizes Terraform for Infrastructure as Code (IaC) to automate the provisioning of Azure resources. This includes the creation of a virtual network, a subnet within this network, and a VM configured with Ubuntu 22.04. It showcases the use of Terraform to automate cloud infrastructure tasks, which is crucial for scalable and efficient DevOps practices.

The architecture revolves around Azure services, with Terraform scripts to set up and manage these services. The project is integrated with GitHub for version control and utilizes Azure CLI for authentication purposes.

## Features

- **Automated VM Provisioning:** Create a Standard_D2s_v3 VM in the 'west europe' region with Ubuntu 22.04.
- **SSH Access:** Secure SSH configuration using generated SSH keys for accessing the VM.
- **Docker Installation:** A startup script is employed to automatically install Docker on the VM, readying it for container-based applications.
- **Dynamic Configuration:** Terraform variables and GitHub secrets allow for customizable and repeatable deployments.

## Getting Started

### Requirements

- Terraform
- Azure CLI
- Git

### Quickstart

1. Clone the repository to your local machine.
2. Navigate to the project directory and run `terraform init` to initialize Terraform.
3. Generate an SSH key pair if you haven't already.
4. Execute `terraform apply` to create the Azure resources. Provide a unique `IDENTIFIANT_EFREI` when prompted.
5. Connect to the VM using SSH with the generated private key.

## Development and Operations

### Version Control

The Terraform configurations for this project are version-controlled using Git with the repository hosted on GitHub. To contribute or modify the infrastructure setup, follow the steps below:

### Cloning the Repository

1. Ensure you have Git installed on your machine.
2. Clone the repository using the following command:

```bash
git clone https://github.com/efrei-ADDA84/MaFraONIA.git
cd MaFraONIA
```

### Terraform Workflow

1. **Terraform Initialization** - Before applying any changes, initialize the Terraform workspace by running:

```bash
terraform init
```

2. **Applying Configuration** - To create or update the infrastructure, execute:

```bash
terraform apply
```

When prompted, enter a unique `IDENTIFIANT_EFREI` or configure it as an environment variable.

3. **Destroying Infrastructure** - To remove all resources managed by Terraform, run:

```bash
terraform destroy
```

Ensure you understand the impact of this command as it will remove all cloud resources defined in the Terraform configurations.

## Azure Authentication for Terraform

To allow Terraform to manage resources in your Azure account, you need to authenticate using environment variables. This method ensures that sensitive credentials are not hardcoded in your project files.

### Setting Environment Variables for Authentication

Before running Terraform commands, set the following environment variables with your Azure account details:

- `ARM_SUBSCRIPTION_ID`: Your Azure Subscription ID.
- `ARM_CLIENT_ID`: Your Azure Service Principal Client ID.
- `ARM_CLIENT_SECRET`: Your Azure Service Principal Client Secret.
- `ARM_TENANT_ID`: Your Azure Tenant ID.

You can set these variables in your terminal session or configure them in a `.env` file that you source before running Terraform commands.

### Creating a Service Principal

1. Install Azure CLI on your machine.
2. Login to Azure CLI using `az login`.
3. Create a service principal using the following command:

```bash
az ad sp create-for-rbac --name "TerraformSP" --role="Contributor" --scopes="/subscriptions/YOUR_SUBSCRIPTION_ID"
```

Replace `YOUR_SUBSCRIPTION_ID` with your actual Azure subscription ID.

### Configuring Terraform with Environment Variables

Ensure that the environment variables mentioned above are set before running `terraform init` or `terraform apply`. Terraform will automatically use these variables for authentication.

### Finding Your Tenant ID

To find your Azure tenant ID, follow these steps:

1. Log in to the Azure portal.
2. Navigate to Azure Active Directory.
3. Look for the Directory ID under the Properties section. This is your tenant ID.

Ensure that the service principal has permissions to the subscription and resources you intend to manage with Terraform.

### License

Copyright (c) 2024.