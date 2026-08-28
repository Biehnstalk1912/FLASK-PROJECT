import pandas as pd 
from sqlalchemy import create_engine
from flask import Flask, render_template
import dash 
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import json



server = Flask(__name__)
app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/')   

engine = create_engine("mysql+pymysql://root:@localhost/flask_project")
query = "SELECT * FROM orders_table"
df = pd.read_sql_query(query, engine)
df = df.iloc[1:]
df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='%m-%d-%y')

fig = px.bar(x=df['Order_Date'], y=df['Quantity'], labels={'x': 'Order Date', 'y': 'Quantity'}, title='Quantity by Order Date')

app.layout = html.Div([
    html.H1('Interactive Graph with Dash and Flask'),
    dcc.Graph(figure=fig)
])


@server.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    server.run(debug=True)