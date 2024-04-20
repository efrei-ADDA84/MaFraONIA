variable "IDENTIFIANT_EFREI" {
  description = "Unique identifier for the VM"
  type        = string
}

variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
  default     = "ADDA84-CTP"
}

variable "location" {
  description = "Azure region for the deployment"
  type        = string
  default     = "westeurope"
}

variable "network_name" {
  description = "Name of the virtual network"
  type        = string
  default     = "network-tp4"
}

variable "subnet_name" {
  description = "Name of the subnet within the virtual network"
  type        = string
  default     = "internal"
}

variable "vm_size" {
  description = "Size of the Azure Virtual Machine"
  type        = string
  default     = "Standard_D2s_v3"
}

variable "ssh_public_key" {
  description = "Public SSH key for VM access"
  type        = string
  default     = "" # This will be replaced by the actual key content in runtime
}