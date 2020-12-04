#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:44:54 2020

@author: jpphi
"""
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from pages import page1, page2


external_stylesheets = ['style.css']


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.H1(children='American pipotage about University rank between 2011 and 2016'),
    dcc.Link('Back to Main Menu', href='/'),
    html.Br(),
    dcc.Link('Page 1: Visualisation des données sous forme de tableau et de graphique.', 
             href='/pages/page1'),
    html.Br(),
    dcc.Link('Page 2: Analyse en composantes principales.', href='/pages/page2'),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/pages/page1':
        return page1.layout
    elif pathname == '/pages/page2':
        return page2.layout
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=True)
