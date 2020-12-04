#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:30:16 2020

@author: jpphi
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output,State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    #html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic')
])


@app.callback(
    Output('container-button-basic','children'),
    Input('submit-val', 'n_clicks'),
    #State('input-on-submit', 'value')
    )
def update_output(n_clicks):
    return 'The button has been clicked {} times'.format(n_clicks)


"""
@app.callback(
    dash.dependencies.Output('container-button-basic', 'children'),
    [dash.dependencies.Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('input-on-submit', 'value')])
def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )
"""



if __name__ == '__main__':
    app.run_server(debug=True)
