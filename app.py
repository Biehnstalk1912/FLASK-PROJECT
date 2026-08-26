import pandas as pd 
from sqlalchemy import create_engine
from flask import Flask, render_template
import dash 
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px



server = Flask(__name__)
app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/')   

engine = create_engine("mysql+pymysql://root:@localhost/flask_project")
query = "SELECT * FROM orders_table"

df = pd.read_sql(query, engine)
print(df.head(20))
