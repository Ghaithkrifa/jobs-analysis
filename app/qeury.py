
import psycopg2
import pandas as pd
import streamlit as st

hostname = "localhost"
database = "offre_emploi"
username = "postgres"
pwd = "ousama"
port_id = 5432

conn = psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=pwd,
    port=port_id)
cur = conn.cursor()


def viewalldata():
    query = """
  SELECT categorie.nom_categorie, sous_categorie.sous_categorie, offre_d_emploi.type_poste,offre_d_emploi.societe,villes.nom_ville, semaines.semaine, offre_d_emploi.statut
    FROM categorie, villes, sous_categorie, semaines, offre_d_emploi, pays
    WHERE categorie.id_categorie = sous_categorie.id_categorie
      AND sous_categorie.id_sous_categorie = offre_d_emploi.id_sous_categorie
      AND semaines.id_semaine = offre_d_emploi.id_semaine
      AND villes.id_ville = offre_d_emploi.id_ville
      AND villes.id_pays = pays.id_pays
      AND pays.nom_pays = 'Canada';
    """
    cur.execute(query)
    data = cur.fetchall()
    return data


def viewalldata_france():
    query = """
  SELECT categorie.nom_categorie, sous_categorie.sous_categorie, offre_d_emploi.type_poste,offre_d_emploi.societe,villes.nom_ville, semaines.semaine, offre_d_emploi.statut
    FROM categorie, villes, sous_categorie, semaines, offre_d_emploi, pays
    WHERE categorie.id_categorie = sous_categorie.id_categorie
      AND sous_categorie.id_sous_categorie = offre_d_emploi.id_sous_categorie
      AND semaines.id_semaine = offre_d_emploi.id_semaine
      AND villes.id_ville = offre_d_emploi.id_ville
      AND villes.id_pays = pays.id_pays
      AND pays.nom_pays = 'France';
    """
    cur.execute(query)
    data = cur.fetchall()
    return data


def view_categorie():
    query = """
  SELECT  nom_categorie
    FROM categorie

    """
    cur.execute(query)
    data = cur.fetchall()
    return data


def view_sous_categorie(categorie1):
    query = """
        SELECT DISTINCT sous_categorie
        FROM sous_categorie, categorie, mot_cles
        WHERE sous_categorie.id_categorie = categorie.id_categorie
        AND mot_cles.id_sous_categorie = sous_categorie.id_sous_categorie
        AND categorie.nom_categorie = %s
    """
    cur.execute(query, (categorie1,))
    data = cur.fetchall()
    return data


def mots_cle(categorie1, sous_categorie):
    query = """
        SELECT DISTINCT mots_cle, frequence
        FROM sous_categorie, categorie, mot_cles
        WHERE sous_categorie.id_categorie = categorie.id_categorie
        AND mot_cles.id_sous_categorie = sous_categorie.id_sous_categorie
        AND categorie.nom_categorie = %s
        AND sous_categorie.sous_categorie= %s
        ORDER BY frequence desc
    """

    cur.execute(query, (categorie1, sous_categorie))
    data = cur.fetchall()
    return data

def competence():
    query = """
  SELECT categorie.nom_categorie, sous_categorie.sous_categorie, offre_d_emploi1.type_poste,offre_d_emploi1.societe,villes.nom_ville, semaines.semaine, offre_d_emploi1.statut,pays.nom_pays,offre_d_emploi1.description
    FROM categorie, villes, sous_categorie, semaines, offre_d_emploi1, pays
    WHERE categorie.id_categorie = sous_categorie.id_categorie
      AND sous_categorie.id_sous_categorie = offre_d_emploi1.id_sous_categorie
      AND semaines.id_semaine = offre_d_emploi1.id_semaine
      AND villes.id_ville = offre_d_emploi1.id_ville
      AND villes.id_pays = pays.id_pays
    """

    cur.execute(query)
    data_competence = cur.fetchall()
    return data_competence
