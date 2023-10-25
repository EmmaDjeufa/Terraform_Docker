# Utilisez l'image officielle Redis comme base
FROM redis:latest

# Facultatif : vous pouvez ajouter des métadonnées pour décrire l'image
LABEL maintainer="VotreNom <votre@email.com>"

# Exposez le port Redis (par défaut 6379)
EXPOSE 6379

# Commande pour exécuter Redis Server
CMD ["redis-server"]
RUN docker build -t mon-redis-image .
RUN docker run -d --name mon-redis-container -p 6379:6379 mon-redis-image

