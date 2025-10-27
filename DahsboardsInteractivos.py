import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st
import dash
from dash import dcc, html
import plotly.express as px

#streamlit
#se ejecuta con el comando streamlit run <ubicacion archivo>, est corre un servidor con el dahsboard creado
'''
st.title('Interactive Dashboard - Streamlit')

st.sidebar.header('User Input Features')
num_points = st.sidebar.slider('Number of points', 10, 100, 50)

data = {'x': np.random.randn(num_points), 'y': np.random.randn(num_points)}
df = pd.DataFrame(data)

st.subheader('Scatter Plot')
plt.figure(figsize=(5, 3))
plt.scatter(df['x'], df['y'], color='red')
plt.title('Scatter Plot')
plt.grid()
st.pyplot(plt)
'''
#dash

#__name__ es una variable incoporada(built in) que establece elk modulo actual
app = dash.Dash(__name__)

np.random.seed(42)
df = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100),
    'category': np.random.choice(['A', 'B', 'C'], 100)
})

app.layout = html.Div([
    html.H1("Interactive Dashboard - Dash"),
    dcc.Dropdown(
        id='dropdown-category',
        options=[{'label': i, 'value': i} for i in df['category'].unique()],
        value='A',
        clearable=False
    ),
    dcc.Graph(id='scatter-plot')
])

#se ejecuta una funcion cada que se cambia un valor en en input definido
@app.callback(
    dash.dependencies.Output('scatter-plot', 'figure'),
    [dash.dependencies.Input('dropdown-category', 'value')]
)
#funcion que se ejcuta cada que cambia el valor en un input definido
def update_graph(selected_category):
    filtered_df = df[df['category'] == selected_category]
    fig = px.scatter(filtered_df, x='x', y='y', title=f"Category: {selected_category}")
    return fig

#__main__ hace referencia a ual ambiente de codigo de alto nivel, que indica la ejecucion de un script 
if __name__ == '__main__':
    app.run(debug=True)
