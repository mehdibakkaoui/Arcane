# Importation des packages necessaires pour notre API
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config_bdd import Base, Logement, Utilisateur

app = Flask(__name__)

# Connexion à la base de donnees et creation d'une session
engine = create_engine('sqlite:///immobilier.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



## Fonctions d'edition

def get_logements_ville(ville):
    '''
    Affiche tout les logements de la ville contenus dans notre base de donnees
    '''
    logements = session.query(Logement).filter_by(ville=ville).all()
    return jsonify(logements=[l.serialize for l in logements])

def get_logements(id_user):
    '''
    Affiche tout les logements de l'utilisateur id_user contenus dans notre base de donnees
    '''
    logements = session.query(Logement).filter_by(id_utilisateur=id_user).all()
    return jsonify(logements=[l.serialize for l in logements])

def get_utilisateurs():
    '''
    Affiche tout les utilisateurs de la base de donnees
    '''
    utilisateurs = session.query(Utilisateur).all()
    return jsonify(utilisateurs=[user.serialize for user in utilisateurs])

def get_utilisateur_id(id_user):
    '''
    Affiche le profil de l'utilisateur id_user contenus dans notre base de donnees
    '''
    utilisateur = session.query(Utilisateur).filter_by(id=id_user).one()
    return jsonify(utilisateurs=utilisateur.serialize)

def nouvelUtilisateur(nom, prenom, date_naissance):
    '''
    Cree un nouvel utilisateur dans notre base de donnees
    '''
    newuser = Utilisateur(nom=nom, prenom=prenom, date_naissance=date_naissance)
    session.add(newuser)
    session.commit()
    return jsonify(Utilisateur=newuser.serialize)

def nouveauLogement(nom, description, type, ville, pieces, caracteristiques, proprietaire, id_user):
    '''
    Cree un nouveau logement pour l'utilisateur id_user dans notre base de donnees
    '''
    newlogement = Logement(nom=nom, description=description, type=type, ville=ville, pieces=pieces, caracteristiques=caracteristiques, proprietaire=proprietaire, id_utilisateur=id_user)
    session.add(newlogement)
    session.commit()
    return jsonify(Logement=newlogement.serialize)

def majLogement(id, nom, description, type, ville, pieces, caracteristiques, proprietaire, id_user):
    '''
    Met à jour les proprietes du logement id dans notre base de donnees
    '''
    updatedLogement = session.query(Logement).filter_by(id=id).one()
    if nom:
        updatedLogement.nom = nom
    if description:
        updatedLogement.description = description
    if type:
        updatedLogement.type = type
    if ville:
        updatedLogement.ville = ville
    if caracteristiques:
        updatedLogement.caracteristiques = caracteristiques
    if pieces:
        updatedLogement.pieces = pieces
    if proprietaire:
        updatedLogement.proprietaire = proprietaire
    session.add(updatedLogement)
    session.commit()
    return 'Mise à jour du logement n° %s' % id

def majProfil(id_user, nom, prenom, date_naissance):
    '''
    Met à jour le profil de l'utilisateur id_user dans notre base de donnees
    '''
    updatedprofil = session.query(Utilisateur).filter_by(id=id_user).one()
    if nom:
        updatedprofil.nom = nom
    if prenom:
        updatedprofil.prenom = prenom
    if date_naissance:
        updatedprofil.date_naissance = date_naissance
    session.add(updatedprofil)
    session.commit()
    return 'Mise à jour du profil utilisateur n° %s' % id_user

def supprimerLogement(id):
    '''
    Supprime le logement id de notre base de donnees
    '''
    logementSuppr = session.query(Logement).filter_by(id=id).one()
    session.delete(logementSuppr)
    session.commit()
    return 'Le logement n° %s a été supprimé' % id

def supprimerUtilisateur(id_user):
    '''
    Supprime l'utilisateur id_user de notre base de donnees
    '''
    utilisateurSuppr = session.query(Utilisateur).filter_by(id=id_user).one()
    session.delete(utilisateurSuppr)
    session.commit()
    return 'Utilisateur n° %s A été supprimé' % id_user




@app.route('/')

# Consulter et creer des utilisateurs
@app.route('/API', methods=['GET', 'POST'])
def UtilisateursFonction():
    if request.method == 'GET':
        return get_utilisateurs()

    elif request.method == 'POST':
        nom = request.args.get('nom', '')
        prenom = request.args.get('prenom', '')
        date_naissance = request.args.get('date_naissance', '')
        return nouvelUtilisateur(nom, prenom, date_naissance)




# Consulter les biens immobiliers pour une ville
@app.route('/API/<string:ville>', methods=['GET'])
def LogementsFonctionVille(ville):
    if request.method == 'GET':
        return get_logements_ville(ville)




# Consulter, creer et supprimer les biens immobiliers pour un utilisateur
@app.route('/API/<int:id_user>', methods=['GET', 'POST', 'DELETE'])
def logementsFonctionIdUser(id_user):
    if request.method == 'GET':
        return get_logements(id_user)

    elif request.method == 'POST':
        nom = request.args.get('nom', '')
        description = request.args.get('description', '')
        type = request.args.get('type', '')
        ville = request.args.get('ville', '')
        pieces = request.args.get('pieces', '')
        caracteristiques = request.args.get('caracteristiques', '')
        proprietaire = request.args.get('proprietaire', '')
        return nouveauLogement(nom, description, type, ville, pieces, caracteristiques, proprietaire, id_user)

    elif request.method == 'DELETE':
        return supprimerUtilisateur(id_user)



# Modifier et supprimer les biens immobiliers pour un utilisateur
@app.route('/API/<int:id_user>/<int:id>', methods=['PUT', 'DELETE'])
def FonctionModifLogement(id_user,id):
    if request.method == 'PUT':
        nom = request.args.get('nom', '')
        description = request.args.get('description', '')
        type = request.args.get('type', '')
        ville = request.args.get('ville', '')
        pieces = request.args.get('pieces', '')
        caracteristiques = request.args.get('caracteristiques', '')
        proprietaire = request.args.get('proprietaire', '')
        return majLogement(id, nom, description, type, ville, pieces, caracteristiques, proprietaire, id_user)

    elif request.method == 'DELETE':
        return supprimerLogement(id)



# Consulter et modifier le profil d'un utilisateur
@app.route('/API/<int:id_user>/profil', methods=['GET', 'PUT'])
def FonctionProfil(id_user):
    if request.method == 'GET':
        return get_utilisateur_id(id_user)

    elif request.method == 'PUT':
        nom = request.args.get('nom', '')
        prenom = request.args.get('prenom', '')
        date_naissance = request.args.get('date_naissance', '')
        return majProfil(id_user, nom, prenom, date_naissance)

if __name__ == '__main__':
    app.debug = True
    app.run()