output "private_key_path" {
  value       = "${path.module}/ssh/id_rsa"
  description = "The path to the generated private SSH key"
  sensitive   = true
}

output "public_key_path" {
  value       = "${path.module}/ssh/id_rsa.pub"
  description = "The path to the generated public SSH key"
}