import streamlit as st
from qeury import viewalldata
import pandas as pd
import plotly.express as px


def filter_data():
    data = viewalldata()
    df = pd.DataFrame(data, columns=["categorie", "sous_categorie",
                                     "type_poste", "societe", "ville", "dates", "statut"])

    options = st.multiselect(
        "Choisir une sous categorie",
        options=df["sous_categorie"].unique(),
        # default=df["type_poste"].unique()
    )

    option = st.multiselect(
        "Ville",
        options=df["ville"].unique(),
        # default=df["ville"].unique()
    )

    if options and option:
        df_selection = df.query(
            "sous_categorie.isin(@options) & ville.isin(@option)")
    else:
        df_selection = df

    st.dataframe(df_selection)
