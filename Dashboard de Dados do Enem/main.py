import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Dados fictícios
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [450, 230, 340, 780]
})

# Inicializar a aplicação Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout da aplicação
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Dashboard Exemplo", className="text-center"), className="mb-4 mt-4")
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar-graph', config={'displayModeBar': False}, className='dbc'),
        ], width=6),
        dbc.Col([
            dcc.Graph(id='pie-chart', config={'displayModeBar': False}, className='dbc'),
        ], width=6),
    ]),
    dbc.Row([
        dbc.Col([
            html.Label("Selecionar Categoria"),
            dcc.Dropdown(
                id='category-dropdown',
                options=[{'label': cat, 'value': cat} for cat in df['Category']],
                value='A',
                clearable=False,
                className='dropdown'
            ),
        ], width=6),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='line-chart', className='dbc'), width=12),
    ])
], fluid=True)

# Callback para atualizar o gráfico de barras
@app.callback(
    Output('bar-graph', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_bar_chart(selected_category):
    filtered_df = df[df['Category'] == selected_category]
    fig = px.bar(filtered_df, x='Category', y='Values', title=f'Valores para a Categoria {selected_category}')
    return fig

# Callback para atualizar o gráfico de pizza
@app.callback(
    Output('pie-chart', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_pie_chart(selected_category):
    filtered_df = df[df['Category'] == selected_category]
    fig = px.pie(filtered_df, names='Category', values='Values', title=f'Distribuição para a Categoria {selected_category}')
    return fig

# Callback para atualizar o gráfico de linha
@app.callback(
    Output('line-chart', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_line_chart(selected_category):
    filtered_df = df[df['Category'] == selected_category]
    fig = px.line(filtered_df, x='Category', y='Values', title=f'Tendência para a Categoria {selected_category}')
    return fig

# Rodar a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)
