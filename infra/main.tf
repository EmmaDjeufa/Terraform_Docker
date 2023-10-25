provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_image" "build" {
  name = "redis"
  build {
    context = "Terraform_Docker/app"  
  }
}

resource "docker_container" www {
  name = www
  image = redis.build.name
  ports {
    internal = 5000  # Port interne de votre application
  }

  
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
