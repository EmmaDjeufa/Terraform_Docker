provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_image" "build" {
  name = "nom-de-votre-image"
  build {
    context = "${path.module}/../app"  # Chemin vers le Dockerfile
  }
}

resource "docker_container" "container" {
  name = "nom-de-votre-container"
  image = docker_image.build.name
  ports {
    internal = 8000
  }
}
