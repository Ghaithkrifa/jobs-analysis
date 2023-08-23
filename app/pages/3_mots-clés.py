import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from qeury import view_categorie, view_sous_categorie, mots_cle
from apigeneral import systeme_recommendation

categorie = view_categorie()
df = pd.DataFrame(categorie, columns=["nom_categorie"])


col1, col2 = st.columns([0.5, 3])
with col1:
    st.image("images/key.png")
with col2:
    st.header(
        " :blue[_Explorez les mots-clés dans chaque domaine_]")


categorie1 = st.selectbox(
    'Choisir une catégorie', df, key='categorie')
sous_cateogrie = view_sous_categorie(categorie1)
df1 = pd.DataFrame(sous_cateogrie, columns=["sous_categorie"])
sous_categorie1 = st.selectbox(
    'Choisir une sous_catégorie', df1, key='sous.categorie')

keyword = mots_cle(categorie1, sous_categorie1)
df3 = pd.DataFrame(keyword, columns=["mots", "frequence"])
sns.set(rc={'figure.figsize': (13, 8)})
bbar = sns.barplot(y="mots", x="frequence", orient='h', data=df3)
plt.xticks(size=18)
bbar.set_yticklabels(bbar.get_yticklabels(), fontsize=20)
plt.tight_layout()

st.pyplot(plt.gcf())

st.header(
    " :blue[_Découvrez les offres d'emploi les mieux adaptées à vos compétences._]")
title = st.text_input(label='Veuillez entrer vos compétences')

if title:
    data1 = systeme_recommendation(title)
    res_data = data1[["statut", "sous_categorie",
                      "pays", "ville", "type_poste", "societe"]]
    st.dataframe(res_data)
