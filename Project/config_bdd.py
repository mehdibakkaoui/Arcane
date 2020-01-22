import sys

# Importation des packages necessaires pour la configuration de la base de donnees
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()


# Creation de la table logement
class Logement(Base):
    __tablename__ = 'logement'

    id = Column(Integer, primary_key=True)
    nom = Column(String(250), nullable=False)
    description = Column(String(250))
    type = Column(String(250), nullable=False)
    ville = Column(String(250), nullable=False)
    pieces = Column(Integer, nullable=False)
    caracteristiques = Column(String(250))
    proprietaire = Column(String(250))
    id_utilisateur = Column(Integer, ForeignKey("utilisateur.id"))

    @property
    def serialize(self):
        return {
            'nom': self.nom,
            'description': self.description,
            'ville': self.ville,
            'type': self.type,
            'pieces': self.pieces,
            'caracteristiques': self.caracteristiques,
            'proprietaire': self.proprietaire,
            'id_utilisateur': self.id_utilisateur,
            'id': self.id,
        }

# Creation de la table utilisateur
class Utilisateur(Base):
    __tablename__ = 'utilisateur'

    id = Column(Integer, primary_key=True)
    nom = Column(String(250), nullable=False)
    prenom = Column(String(250), nullable=False)
    date_naissance = Column(String(250) , nullable=False)

    @property
    def serialize(self):
        return {
            'nom': self.nom,
            'prenom': self.prenom,
            'date_naissance': self.date_naissance,
            'id': self.id,
        }

# Creation de la base de donnees 'immobilier' avec SQLite
engine = create_engine('sqlite:///immobilier.db')
Base.metadata.create_all(engine)