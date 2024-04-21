provider "azurerm" {
  features {}
  subscription_id            = var.subscription_id
  skip_provider_registration = true
}

data "azurerm_resource_group" "existing_rg" {
  name = var.resource_group_name
}

data "azurerm_virtual_network" "existing_vnet" {
  name                = var.network_name
  resource_group_name = data.azurerm_resource_group.existing_rg.name
}

data "azurerm_subnet" "existing_subnet" {
  name                 = var.subnet_name
  virtual_network_name = data.azurerm_virtual_network.existing_vnet.name
  resource_group_name  = data.azurerm_resource_group.existing_rg.name
}

resource "azurerm_public_ip" "vm_public_ip" {
  name                = "devops-${var.IDENTIFIANT_EFREI}-public-ip"
  location            = data.azurerm_resource_group.existing_rg.location
  resource_group_name = data.azurerm_resource_group.existing_rg.name
  allocation_method   = "Dynamic"
}

resource "azurerm_network_interface" "vm_nic" {
  name                = "devops-${var.IDENTIFIANT_EFREI}-nic"
  location            = data.azurerm_resource_group.existing_rg.location
  resource_group_name = data.azurerm_resource_group.existing_rg.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = data.azurerm_subnet.existing_subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.vm_public_ip.id
  }
}

resource "azurerm_linux_virtual_machine" "devops_vm" {
  name                  = "devops-${var.IDENTIFIANT_EFREI}"
  resource_group_name   = data.azurerm_resource_group.existing_rg.name
  location              = data.azurerm_resource_group.existing_rg.location
  size                  = var.vm_size
  admin_username        = "devops"
  network_interface_ids = [azurerm_network_interface.vm_nic.id]

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = var.vm_publisher
    offer     = var.vm_offer
    sku       = var.vm_sku
    version   = var.vm_version
  }

  computer_name = "devops-${var.IDENTIFIANT_EFREI}"
  admin_ssh_key {
    username   = "devops"
    public_key = file("${path.module}/id_rsa.pub")
  }

  disable_password_authentication = true

  custom_data = filebase64("${path.module}/docker_install.sh")
}
