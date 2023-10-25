provider "docker" {
  host = "tcp://localhost:2375" # Adresse de votre serveur Docker local
}

resource "docker_image" "redis" {
  name = "redis:latest"
}

resource "docker_container" "redis" {
  name  = "redis-container"
  image = docker_image.redis.name
  ports {
    internal = 6379 # Port Redis interne dans le conteneur
    external = 6379 # Port Redis externe sur l'hôte
  }
}

