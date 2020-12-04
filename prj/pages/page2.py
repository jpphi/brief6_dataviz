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
    dcc.Link('Retour à la page 1.', href='/pages/page1')
])


@app.callback(
    Output('app-2-display-value', 'children'),
    Input('app-2-dropdown', 'value'))
def display_value(value):
    if value== "Graph 1":
        return(dcc.Graph(src="coyote.png"))
        return "Graph1 à afficher"
    if value== "Graph 2":
        return "Graph 2 à afficher"
    if value== "Graph 3":
        return "Graph 3 à afficher"
    return 'Pas de graphe sélectionné.'
#    return 'Valeur sélectionnée "{}"'.format(value)

"""
@app.callback(
    Output('app-2-display-value', 'children'),
    Input('app-2-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)
"""