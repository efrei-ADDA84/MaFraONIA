variable "IDENTIFIANT_EFREI" {
  type        = string
  description = "Unique identifier for the DevOps VM"
}

variable "resource_group_name" {
  type        = string
  description = "Name of the Azure resource group"
  default     = "ADDA84-CTP"
}

variable "network_name" {
  type        = string
  description = "Name of the virtual network"
  default     = "network-tp4"
}

variable "subnet_name" {
  type        = string
  description = "Name of the subnet within the virtual network"
  default     = "internal"
}

variable "address_space" {
  type        = list(string)
  description = "Address space for the virtual network"
  default     = ["10.0.0.0/16"]
}

variable "subnet_prefixes" {
  type        = list(string)
  description = "Address range for the subnet"
  default     = ["10.0.1.0/24"]
}

variable "vm_size" {
  type        = string
  description = "The size of the Azure Virtual Machine"
  default     = "Standard_D2s_v3"
}

variable "vm_publisher" {
  type        = string
  description = "Publisher of the VM image"
  default     = "Canonical"
}

variable "vm_offer" {
  type        = string
  description = "Offer of the VM image"
  default     = "UbuntuServer"
}

variable "vm_sku" {
  type        = string
  description = "SKU of the VM image"
  default     = "18.04-LTS"
}

variable "vm_version" {
  type        = string
  description = "Version of the VM image"
  default     = "latest"
}

variable "subscription_id" {
  type        = string
  description = "Azure subscription ID"
}