provider "docker" {
  host = "tcp://localhost:2375" # Adresse de votre serveur Docker local
}

resource "docker_image" "build" {
  name         = "fastapi-app:latest"
  build        {
    context = "../app"
  }
}

resource "docker_container" "container" {
  name  = "fastapi-container"
  image = docker_image.build.name
  ports {
    internal = 80
    external = 8080
  }
}
