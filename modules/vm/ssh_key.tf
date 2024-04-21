resource "tls_private_key" "ssh_key" {
  algorithm = "RSA"
  rsa_bits  = 2048
}

resource "local_file" "private_key" {
  content  = tls_private_key.ssh_key.private_key_pem
  filename = "${path.module}/ssh/id_rsa"
}

resource "local_file" "public_key" {
  content  = tls_private_key.ssh_key.public_key_openssh
  filename = "${path.module}/ssh/id_rsa.pub"
}

output "private_key_path" {
  value       = "${path.module}/ssh/id_rsa"
  description = "The path to the generated private SSH key"
  sensitive   = true
}

output "public_key_path" {
  value       = "${path.module}/ssh/id_rsa.pub"
  description = "The path to the generated public SSH key"
}