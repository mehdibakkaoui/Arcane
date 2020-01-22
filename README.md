# Arcane
Etude de cas

## Contenu du dossier
- *Schema_BDD.pdf* : Schéma initial de la base de données *Projet/immobilier.db*
- */Projet* :  
  - *immobilier.db* : Base de données de l'API
  - *config_BDD.py* : Script de configuration de la base de données
  - *app.py* : Exécutable de l'API

## Mode d'emploi
Exécuter le fichier **app.py**

Pour utiliser l'API et vérifier que tout fontionne comme voulu, il est plus simple d'utiliser Postman (https://www.getpostman.com/).
Cette plateforme est dédiée au developpment d'APIs et facilite l'écriture des requêtes envoyées au serveur.

Voici l'architecture et les méthodes permises de l'API :
- http://localhost:5000/API
   - GET : Consulter les utilisateurs de la BDD
   - POST : Créer des utilisateurs dans BDD
- http://localhost:5000/API/Paris (par exemple ville = Paris)
   - GET : Consulter les logements situés à *Paris*
- http://localhost:5000/API/1 (par exemple id_user = 1)
   - GET : Consulter les logements de l'utilisateur 1
   - POST : Créer un logement pour l'utilisateur 1
   - DELETE : Supprimer l'utilisateur 1
- http://localhost:5000/API/1/3 (par exemple id_user = 1, id_logement = 3) 
**Ces fonctions existent seulement si l'utilisateur 1 posséde le logement 3 !**
   - PUT : Modifier les proprietés du logement 3
   - DELETE : Supprimer le logement 3
- http://localhost:5000/API/1/profil (par exemple id_user = 1)
   - GET : Consulter le profil de l'utilisateur 1
   - PUT : Modifier les données de l'utilisateur 1
