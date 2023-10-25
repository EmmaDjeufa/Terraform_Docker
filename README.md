# Terraform_Docker
Dans ce projet, Nous avons construit un petit système qui va déployer un container Docker depuis Terraform.

Pour l'exécuter en local dans un terminal, il faut tout d'abord le coner en utilisant la commande :
git clone https://github.com/EmmaDjeufa/Terraform_Docker.git

Ensuite, il faut s'assurer d'avoir téléchargé les paquets neccessaire pour l'environnement Terraform. Cela peut se faire sur linux par la commande suivante : 

sudo apt-get update
sudo apt-get install terraform
terraform version  #Permet de verrifier la version.

Ensuite, on exécute :
terraform init
terraform applay  // Prendre l'option "yes"

L'infrastructure exécute alors le code counter.py qui permet d'ouvrir la page ShopifyShop.html



