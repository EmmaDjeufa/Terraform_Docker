provider docker {
  source = "kreuzwerker/docker"
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

