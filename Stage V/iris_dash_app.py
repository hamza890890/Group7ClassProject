import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load the Iris dataset
df = px.data.iris()

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Iris Flower Scatter Plot Dashboard"),
    
    # Dropdown for selecting species
    html.Label("Select Species:"),
    dcc.Dropdown(
        id='species-dropdown',
        options=[{'label': species, 'value': species} for species in df['species'].unique()],
        value='setosa',
        clearable=False,
        style={'width': '50%'}
    ),

    # Graph to display scatter plot
    dcc.Graph(id='scatter-plot')
])

# Callback to update the scatter plot based on dropdown selection
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('species-dropdown', 'value')]
)
def update_scatter(selected_species):
    # Filter dataframe based on the selected species
    filtered_df = df[df['species'] == selected_species]
    # Create the scatter plot
    fig = px.scatter(filtered_df, x='sepal_width', y='sepal_length', color='species',
                     title=f"Scatter Plot for {selected_species.capitalize()} Species",
                     labels={'sepal_width': 'Sepal Width', 'sepal_length': 'Sepal Length'})
    return fig

# Run the server
# To run server, open your terminal and make sure you're inside the Stage V folder.
# Then type the command: 'python iris_dash_app.py'
# Then open your web broser and go to http://127.0.0.1:8050/

if __name__ == '__main__':
    app.run_server(debug=True)
