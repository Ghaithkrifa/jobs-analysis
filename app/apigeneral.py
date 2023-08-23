from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from qeury import competence
import pandas as pd


data = competence()
df1 = pd.DataFrame(data, columns=["categorie", "sous_categorie",
                                  "type_poste", "societe", "ville", "date", "statut", "pays", "description"])


def systeme_recommendation(motscles):
    descriptions = df1["description"].tolist()
    vectorizer = TfidfVectorizer()
    matrice_tfidf = vectorizer.fit_transform(descriptions)
    nombre_affichages = 5
    mots_cles_utilisateur = motscles
    vecteur_mots_cles = vectorizer.transform([mots_cles_utilisateur])
    similarites = cosine_similarity(matrice_tfidf, vecteur_mots_cles)
    indices_tries = similarites.flatten().argsort()[::-1]
    indices_offres_choisies = indices_tries[:nombre_affichages]
    offres_choisies = df1.iloc[indices_offres_choisies]
    return offres_choisies
