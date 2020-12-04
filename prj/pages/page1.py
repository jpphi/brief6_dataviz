#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:41:54 2020

@author: jpphi
"""
import pandas as pd

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

tableau_complet = pd.read_csv('../data/timesData.csv')
df2016 = tableau_complet [tableau_complet.year == 2016].iloc[:50,:]



layout = html.Div([
    html.H3(children='Visualisation des données sous forme de tableau et de graphique.'),
    html.Button('Chargement', id='chargement_val', n_clicks=0),

    html.Button('Visualisation des données', id='visu01', n_clicks=0),

    dcc.Dropdown(
        id='app-1-dropdown',
        options=[
            {'label': 'Page 1 - {}'.format(i), 'value': i} for i in [
                'Graph 1', 'Graph 2', 'Graph 3'
            ]
        ]),
    html.Div(id='app-1-display-value'),

    html.Div("Chargement demandée",id='container-button-visu'),
    html.Div("Chargement demandée",id='container-button-basic'),

    dcc.Link('Go to App 2', href='/pages/page2')
    #,    classement(df2016)
])

@app.callback(
    Output('container-button-visu','children'),
    Input('visu01', 'n_clicks'),
    #State('input-on-submit', 'value')
    )
def visu_output(n_clicks):
    return 'Zone de visualisation des données'
#    return 'The button has been clicked {} times'.format(n_clicks)


@app.callback(
    Output('container-button-basic','children'),
    Input('chargement_val', 'n_clicks'),
    #State('input-on-submit', 'value')
    )
def classement(n_clicks):
    if n_clicks== 0:return 'Zone de chargement du fichier.'
    
    # récupérer le timesData.csv dans le répertoire Data
    max_rows= len(df2016)
    n_clicks= 0
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df2016.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df2016.iloc[i][col]) for col in df2016.columns
            ]) for i in range(0, max_rows)
        ])
    ])


@app.callback(
    Output('app-1-display-value', 'children'),
    Input('app-1-dropdown', 'value'))
def display_value(value):
    if value== "Graph 1":
        return "Graph1 à afficher"
    if value== "Graph 2":
        return "Graph 2 à afficher"
    if value== "Graph 3":
        return "Graph 3 à afficher"
    return 'Pas de graphe sélectionné.'
#    return 'Valeur sélectionnée "{}"'.format(value)

