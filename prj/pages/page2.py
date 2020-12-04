#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:45:30 2020

@author: jpphi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:41:54 2020

@author: jpphi
Analyse en composante principal
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

import pandas as pd
import plotly.express as px

tableau_complet = pd.read_csv('../data/timesData.csv')
df2016 = tableau_complet [tableau_complet.year == 2016].iloc[:50,:]


layout = html.Div([
    html.H3('Analyse en composantes principales.'),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': 'Page 2 - {}'.format(i), 'value': i} for i in [
                'Graph 1', 'Graph 2', 'Graph 3'
            ]
        ]
    ),
    html.Div(id='app-2-display-value'),
    
    dcc.Graph(id='graph2'),

    
    dcc.Link('Retour à la page 1.', href='/pages/page1')
])

@app.callback(
    Output('graph2', 'figure'),
    Input('app-2-dropdown', 'value'))
#    Input('year-slider', 'value'))
def update_figure(value):
    if value== "Graph 1":
    #filtered_df = df[df.year == selected_year]
        fig2 = px.scatter(df2016, x="world_rank", y="research", color="country", hover_name="country")
        return fig2
    elif value== "Graph 2":
        fig2 = px.scatter(df2016, x="world_rank", y="income", color="country", hover_name="country")
        return fig2

    else :
        fig2 = px.scatter(df2016, x="world_rank", y="teaching", color="country", hover_name="country")
        return fig2
