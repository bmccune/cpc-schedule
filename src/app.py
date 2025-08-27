from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output
from utils.time_utils import get_current_time, get_current_day
import pandas as pd
import json

app = Dash(__name__)

regular = pd.read_csv('https://raw.githubusercontent.com/bmccune/SchoolScheduleCPC/refs/heads/main/regularSchedule.csv')
early = pd.read_csv('https://raw.githubusercontent.com/bmccune/SchoolScheduleCPC/refs/heads/main/earlySchedule.csv')
aSchedule = pd.read_csv('https://raw.githubusercontent.com/bmccune/SchoolScheduleCPC/refs/heads/main/a_schedule.csv')

app.layout = html.Div([
    dcc.Interval(id='interval-componentD', interval=1000, n_intervals=0),
    html.Div(id='live-day', style={'fontSize': 24, 'marginTop': 20}),
    html.H1("School Schedule Dashboard"),
    dcc.Dropdown(['Regular', 'Early', 'Schedule A', 'Schedule B', 'Schedule C', 'Schedule D', 'Combined'], 'Regular', id='demo-dropdown'),
    dcc.Interval(id='interval-component', interval=1000, n_intervals=0),
    html.Div(id='live-time', style={'fontSize': 24, 'marginTop': 20}),
    html.Div(id='dd-output-container'),
    dash_table.DataTable(
        id='regular',
        columns=[{"name": i, "id": i} for i in regular.columns],
        data=regular.to_dict('records')
        ),
    dash_table.DataTable(
        id='early',
        columns=[{"name": i, "id": i} for i in early.columns],
        data=early.to_dict('records'),
        style_table={'display': 'none'}  # Initially hide the early schedule table  
        ),
    dash_table.DataTable(
        id='aSchedule',
        columns=[{"name": i, "id": i} for i in aSchedule.columns],
        data=aSchedule.to_dict('records'),
        style_table={'display': 'none'}  # Initially hide the early schedule table  
        )
])
@app.callback(
    Output('live-day', 'children'),
    Input('interval-componentD', 'n_intervals')
)
def update_day(n):
    return get_current_day()

@app.callback(
    Output('live-time', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_time(n):
    return get_current_time()

@app.callback(
    Output('regular', 'style_table'),
    Output('early', 'style_table'),
    Output('aSchedule', 'style_table'),
    Input('demo-dropdown', 'value')
)
def toggle_tables(selected):
    if selected == 'Regular':
        return {'display': 'block'}, {'display': 'none'}, {'display': 'none'}
    elif selected == 'Early':
        return {'display': 'none'}, {'display': 'block'}, {'display': 'none'}
    elif selected == 'Schedule A':
        return {'display': 'none'}, {'display': 'none'}, {'display': 'block'}
    else:
        return {'display': 'none'}, {'display': 'none'}, {'display': 'none'}


if __name__ == '__main__':
    app.run(debug=True)