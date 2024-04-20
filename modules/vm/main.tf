resource "azurerm_virtual_machine" "devops_vm" {
  name                  = "devops-${var.IDENTIFIANT_EFREI}"
  location              = var.location
  resource_group_name   = var.resource_group_name
  network_interface_ids = [azurerm_network_interface.devops_nic.id]
  vm_size               = var.vm_size

  storage_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "22.04-LTS"
    version   = "latest"
  }

  storage_os_disk {
    name              = "osdisk"
    caching           = "ReadWrite"
    create_option     = "FromImage"
    managed_disk_type = "Standard_LRS"
  }

  os_profile {
    computer_name  = "devops-${var.IDENTIFIANT_EFREI}"
    admin_username = "adminuser"
    custom_data    = file("${path.module}/cloud-init.yaml")
  }

  os_profile_linux_config {
    disable_password_authentication = true
    ssh_keys {
      path     = "/home/adminuser/.ssh/authorized_keys"
      key_data = file("${path.module}/ssh/id_rsa.pub")
    }
  }

  tags = {
    environment = "devops"
  }
}

resource "azurerm_network_interface" "devops_nic" {
  name                = "devops-${var.IDENTIFIANT_EFREI}-nic"
  location            = var.location
  resource_group_name = var.resource_group_name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.internal.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.devops_public_ip.id
  }

  tags = {
    environment = "devops"
  }
}

resource "azurerm_public_ip" "devops_public_ip" {
  name                = "devops-${var.IDENTIFIANT_EFREI}-ip"
  location            = var.location
  resource_group_name = var.resource_group_name
  allocation_method   = "Dynamic"

  tags = {
    environment = "devops"
  }
}

resource "azurerm_subnet" "internal" {
  name                 = var.subnet_name
  resource_group_name  = var.resource_group_name
  virtual_network_name = var.network_name
  address_prefixes     = ["10.0.2.0/24"]

  tags = {
    environment = "devops"
  }
}