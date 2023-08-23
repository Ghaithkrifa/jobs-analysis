import streamlit as st
import folium
from apicanada import display_details_france, display_details_canada
import pandas as pd
st.set_page_config(page_title="offre d'emploi", layout="wide",
                   page_icon="")

col1, col2 = st.columns([0.5, 3])
with col1:
    st.image("images/envast.png", caption='Envast')
with col2:
    st.header(
        " :blue[_Découvrez un aperçu complet et captivant du marché d'emploi_]")


col11, col22 = st.columns([1.9, 2])
with col11:
    st.write("<h2 style='color:#063970'>À propos de nous : </h2>",
             unsafe_allow_html=True)

    st.markdown("<p style='font-weight:550;'>Envast permet de fournir des informations précises et complètes sur le marché de l'emploi. Notre tableau de bord d'offres d'emploi vous permet de suivre les tendances du marché, d'explorer les offres d'emploi en détail, de découvrir les différents types d'opportunités, etc. Notre objectif est de simplifier votre recherche d'emploi et de vous aider à prendre des décisions éclairées pour votre carrière.</p>", unsafe_allow_html=True)
with col22:
    st.image("images/TB.png")
st.write("<h2 style='color:#063970'>Liste des pays disponibles : </h2>",
         unsafe_allow_html=True)


col111, col222, col333 = st.columns([2, 2, 2])
with col111:
    st.image("images/france.png", width=300)
    st.markdown("<h2 style='margin-left: 80px;'>France</h2>",
                unsafe_allow_html=True)
with col333:
    st.image("images/canada.png", width=350)
    st.markdown("<h2 style='margin-left: 90px;margin-top: 55px;'>Canada</h2>",
                unsafe_allow_html=True)

st.write("<h2 style='color:#063970'>Liste des emplois disponibles par categorie : </h2>",
         unsafe_allow_html=True)

tab1, tab2 = st.tabs(["France", "Canada"])

with tab1:
    def_france = display_details_france()
    col1, col2, col3, col4 = st.columns([0.5, 1.2, 1.2, 0.5])
    with col1:
        st.write(
            f"<h4 style='color:#063970'>{def_france[0][0]} </h4>", unsafe_allow_html=True)
        for digit in def_france[0][1]:
            st.markdown(
                f"<p style='font-weight:550;'>{digit}</p>", unsafe_allow_html=True)

    with col2:
        st.write(
            f"<h4 style='color:#063970'>{def_france[1][0]} </h4>", unsafe_allow_html=True)
        for digit in def_france[1][1]:
            st.markdown(
                f"<p style='font-weight:550;'>{digit}</p>", unsafe_allow_html=True)
    with col3:
        st.write(
            f"<h4 style='color:#063970'>{def_france[2][0]} </h4>", unsafe_allow_html=True)
        for digit in def_france[2][1]:
            st.markdown(
                f"<p style='font-weight:550;'>{digit}</p>", unsafe_allow_html=True)
    with col4:
        st.write(
            f"<h4 style='color:#063970'>{def_france[3][0]} </h4>", unsafe_allow_html=True)
        for digit in def_france[3][1]:
            st.markdown(
                f"<p style='font-weight:550;'>{digit}</p>", unsafe_allow_html=True)


with tab2:
    def_canada = display_details_canada()
    col1, col2, col3, col4 = st.columns([0.5, 1.2, 1.2, 0.5])
    with col1:
        st.write(
            f"<h4 style='color:#063970'>{def_canada[0][0]} </h4>", unsafe_allow_html=True)
        for digit in def_canada[0][1]:
            st.markdown(
                f"<p style='font-weight:550;'>{digit}</p>", unsafe_allow_html=True)

    with col2:
        st.write(
            f"<h4 style='color:#063970'>{def_canada[1][0]} </h4>", unsafe_allow_html=True)
        for digit in def_canada[1][1]:
            st.markdown(
                f"<p style='font-weight:550;'>{digit}</p>", unsafe_allow_html=True)
    with col3:
        st.write(
            f"<h4 style='color:#063970'>{def_canada[2][0]} </h4>", unsafe_allow_html=True)
        for digit in def_canada[2][1]:
            st.markdown(
                f"<p style='font-weight:550;'>{digit}</p>", unsafe_allow_html=True)
    with col4:
        st.write(
            f"<h4 style='color:#063970'>{def_canada[3][0]} </h4>", unsafe_allow_html=True)
        for digit in def_canada[3][1]:
            st.markdown(
                f"<p style='font-weight:550;'>{digit}</p>", unsafe_allow_html=True)
