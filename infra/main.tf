#provider "docker" {
  #host = "unix:///var/run/docker.sock"
#}

#resource "docker_image" "build" {
  #name = "nom-de-votre-image"
  #build {
    #context = "${path.module}/../app"  # Chemin vers le Dockerfile
  #}
#}

#resource "docker_container" "container" {
  #name = "nom-de-votre-container"
  #image = docker_image.build.name
  #ports {
    #internal = 8000
  #}
#}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_image" "build" {
  name = "redis"
  build {
    context = "Terraform_Docker/app"  # Chemin vers le Dockerfile
  }
}

resource "docker_container" www {
  name = www
  image = redis.build.name
  ports {
    internal = 5000  # Port interne de votre application
  }

  # Vous pouvez ajouter d'autres paramètres ici, par exemple, si vous souhaitez utiliser les variables d'environnement.
  environment = {
    DEBUG = "1"
  }

  # Pour montrer comment utiliser un volume (votre Docker Compose a un volume "www")
  volumes {
    container_path = "/src"
    host_path      = "./www"
    read_only     = false
  }
}

