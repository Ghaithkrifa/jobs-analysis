import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
from plotly.subplots import make_subplots
import numpy as np

from apicanada import filter_data1, francefiltre, calculer_pourcentage_avancement, localisation, plot_bar_chart, grapheline1, plot_line_chart, societe, cambembertchart
import matplotlib.pyplot as plt
df1 = francefiltre()


st.set_page_config(layout='wide', initial_sidebar_state='expanded')
st.markdown(
    "### Différence du nombre d'offres d'emploi par rapport au mois dernier")
res = calculer_pourcentage_avancement(df1)

col1, col2, col3, col4 = st.columns(4)
col1.metric(res[0][0], res[0][2], res[0][1]+"%")
col2.metric(res[1][0], res[1][2], res[1][1]+"%")
col3.metric(res[2][0], res[2][2], res[2][1]+"%")
col4.metric(res[3][0], res[3][2], res[3][1]+"%")
st.markdown("### Explorez en détail les offres d'emploi")
filter_data1()


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.sidebar.image("images/france.png", width=280)
st.sidebar.header('Dashboard `France`')
st.sidebar.subheader("Visualiser les types d'offre d'emploi")
option_categorie = df1["categorie"].unique()
categorie = st.sidebar.selectbox(
    'Choisir une catégorie', option_categorie, key='categorie')

options_sous_categories = df1[df1['categorie']
                              == categorie]['sous_categorie'].unique()

sous_categorie = st.sidebar.selectbox(
    'Choisir une sous-catégorie', options_sous_categories, key='sous_categorie')

st.sidebar.subheader("Evolution de nombre d'offre d'emploi ")
option_categorie1 = df1["categorie"].unique()
categorie_grapheline = st.sidebar.selectbox(
    'Choisir une catégorie', option_categorie1, key='categorie1')

options_sous_categories1 = df1[df1['categorie']
                               == categorie_grapheline]['sous_categorie'].unique()
sous_categorie_grapheline = st.sidebar.multiselect(
    'Select data', options_sous_categories1, default=[options_sous_categories1[0]])

c1, c2 = st.columns((3, 3))

with c1:
    st.markdown('### Ville')
    filtered_df_ville = df1[(df1['sous_categorie'] == sous_categorie) & (
        df1['categorie'] == categorie)]
    res, ville = localisation(filtered_df_ville)
    plot_bar_chart(ville, res)


with c2:
    st.markdown("### les types d'offre d'emploi")
    filtered_df = df1[(df1['sous_categorie'] == sous_categorie)
                      & (df1['categorie'] == categorie)]
    category_counts = filtered_df['type_poste'].value_counts()
    donut_data = pd.DataFrame(
        {'Type Poste': category_counts.index, 'Count': category_counts.values})
    fig = px.pie(donut_data, values='Count', names='Type Poste', hole=0.5)
    st.plotly_chart(fig, use_container_width=True)

st.header("Société")
co1, co2, co3 = st.columns([1, 2, 1])
with co2:

    filtered_df_societe = df1[(df1['sous_categorie'] == sous_categorie) & (
        df1['categorie'] == categorie)]
    res1, entreprise = societe(filtered_df_societe)
    cambembertchart(res1, entreprise)


st.header("Evolution de nombre d'offre d'emploi ")
ddf = grapheline1(categorie_grapheline, sous_categorie_grapheline)
x_axis1 = ["1ère semaine", "2ème semaine", "3ème semaine", "4ème semaine"]
plot_line_chart(x_axis1, ddf, sous_categorie_grapheline)
