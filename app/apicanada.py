import streamlit as st
from qeury import viewalldata, viewalldata_france
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def canadafiltre():
    data = viewalldata()
    df = pd.DataFrame(data, columns=["categorie", "sous_categorie",
                                     "type_poste", "societe", "ville", "dates", "statut"])
    return df


def francefiltre():
    data = viewalldata_france()
    df = pd.DataFrame(data, columns=["categorie", "sous_categorie",
                                     "type_poste", "societe", "ville", "dates", "statut"])
    return df


def display_details_france():
    df1 = francefiltre()
    categories_uniques = df1.drop_duplicates(
        subset=["categorie", "sous_categorie"])
    result = categories_uniques.groupby(
        "categorie")["sous_categorie"].apply(list).reset_index()

    categories_list = [(row["categorie"], row["sous_categorie"])
                       for _, row in result.iterrows()]
    return categories_list


def display_details_canada():
    df1 = canadafiltre()
    categories_uniques = df1.drop_duplicates(
        subset=["categorie", "sous_categorie"])
    result = categories_uniques.groupby(
        "categorie")["sous_categorie"].apply(list).reset_index()

    categories_list = [(row["categorie"], row["sous_categorie"])
                       for _, row in result.iterrows()]
    return categories_list


def localisation(df):
    counts = df["ville"].value_counts()
    redondances = counts.tolist()
    villes = counts.index.tolist()[:3] + ["autres"]
    redondances_somme = sum(redondances[3:])
    hh = redondances[:3] + [redondances_somme]
    return hh, villes


def societe(df):
    counts = df["societe"].value_counts()
    redondances = counts.tolist()
    societee = counts.index.tolist()[:5] + ["autres"]
    redondances_somme = sum(redondances[5:])
    hhh = redondances[:5] + [redondances_somme]
    return hhh, societee


def cambembertchart(res1, entreprise):
    data = {'Category': entreprise,
            'Value': res1}

    df = pd.DataFrame(data)

    fig = px.pie(df, values='Value', names='Category',
                 color_discrete_sequence=px.colors.qualitative.Set3)
    fig.update_layout(width=600, height=500)
    st.plotly_chart(fig)


def get_counts(df_selection, cat):
    filtered_df = df_selection[(df_selection['sous_categorie'] == cat) & (
        df_selection['dates'] != 'il y a un mois')]

    counts = filtered_df['dates'].value_counts().sort_index().tolist()
    return counts


def grapheline(categorie_grapheline, sous_categorie_grapheline):
    df = canadafiltre()
    df_selection = df.query(
        "sous_categorie.isin(@sous_categorie_grapheline) & categorie.isin([@categorie_grapheline])")
    axe_y = []
    for cat in sous_categorie_grapheline:
        axe_y.append(get_counts(df_selection, cat))
    return axe_y


def grapheline1(categorie_grapheline, sous_categorie_grapheline):
    df = francefiltre()
    df_selection = df.query(
        "sous_categorie.isin(@sous_categorie_grapheline) & categorie.isin([@categorie_grapheline])")
    axe_y = []
    for cat in sous_categorie_grapheline:
        axe_y.append(get_counts(df_selection, cat))
    return axe_y


def plot_line_chart(x_axis, y_axis, legend):
    df = pd.DataFrame({'Semaines': x_axis})
    for i, data in enumerate(y_axis):
        df[legend[i]] = data
    df = df.melt('Semaines', var_name='Categorie', value_name='Values')
    fig = px.line(df, x='Semaines', y='Values',
                  color='Categorie', markers=True)
    fig.update_layout(
        width=1000,
        height=600,
        legend=dict(
            font=dict(
                size=12
            )
        )
    )
    for trace in fig.data:
        trace.line.width = 4
    st.plotly_chart(fig)


def filter_data():
    df = canadafiltre()
    options = st.multiselect(
        "Choisir une sous categorie",
        options=df["sous_categorie"].unique(),
    )

    option = st.multiselect(
        "Ville",
        options=df["ville"].unique(),

    )

    if options and option:
        df_selection = df.query(
            "sous_categorie.isin(@options) & ville.isin(@option)")
    else:
        df_selection = df

    st.dataframe(df_selection)


def filter_data1():
    df = francefiltre()
    options = st.multiselect(
        "Choisir une sous categorie",
        options=df["sous_categorie"].unique(),
    )

    option = st.multiselect(
        "Ville",
        options=df["ville"].unique(),

    )

    if options and option:
        df_selection = df.query(
            "sous_categorie.isin(@options) & ville.isin(@option)")
    else:
        df_selection = df

    st.dataframe(df_selection)


def calculer_pourcentage_avancement(df1):
    counts = df1.groupby(['categorie', 'dates']).size(
    ).reset_index(name='count_dates')

    def group_dates(date):
        if 'semaine' in date:
            return 'semaine'
        return date

    grouped_df = counts.groupby(['categorie', counts['dates'].apply(group_dates)])[
        'count_dates'].sum().reset_index()

    def calculer_pourcentage_avancement(group):
        valeur_mois = group.loc[group['dates'] ==
                                'il y a un mois', 'count_dates'].values[0]
        valeur_semaine = group.loc[group['dates']
                                   == 'semaine', 'count_dates'].values[0]
        difference = valeur_semaine - valeur_mois
        pourcentage_avancement = difference / 100
        signe = "+" if difference >= 0 else "-"
        somme_semaine = group.loc[group['dates']
                                  == 'semaine', 'count_dates'].sum()
        return (group['categorie'].iloc[0], f"{signe}{abs(pourcentage_avancement)}", somme_semaine)

    resultats = grouped_df.groupby('categorie').apply(
        calculer_pourcentage_avancement).tolist()
    return resultats


def plot_bar_chart(ville, res):
    y_saving = res
    x = ville

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=y_saving,
        y=x,
        marker=dict(
            color='rgba(50, 171, 96, 0.6)',
            line=dict(
                color='rgba(50, 171, 96, 1.0)',
                width=1),
        ),
        name='Household savings, percentage of household disposable income',
        orientation='h',
    ))

    fig.update_layout(
        title='Répartition des emplois par ville',
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=True,
        ),
        xaxis=dict(
            zeroline=False,
            showline=False,
            showticklabels=True,
            showgrid=True,
        ),
        annotations=[
            dict(
                x=y,
                y=country,
                text=str(y) + '%',
                font=dict(family='Arial', size=12, color='rgb(50, 171, 96)'),
                showarrow=False,
                xanchor='left',
                xshift=3
            ) for y, country in zip(y_saving, x)
        ],
        paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',
        height=400,  # Adjust the height of the chart
        width=400,  # Adjust the width of the chart
    )

    st.plotly_chart(fig)
