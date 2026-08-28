import pandas as pd 
from sqlalchemy import create_engine
from flask import Flask, render_template
import dash 
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.utils
import json



app = Flask(__name__)
engine = create_engine("mysql+pymysql://root:@localhost/flask_project")
query = "SELECT * FROM orders_table"
df = pd.read_sql_query(query, engine)
df = df.iloc[1:]
df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='%m-%d-%y')




@app.route("/")
def index():
    fig = px.bar(x=df['Order_Date'], y=df['Quantity'], 
                 labels={'x': 'Order Date', 'y': 'Quantity'}, 
                 title='Quantity by Order Date')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", graphJSON = graphJSON)



if __name__ == "__main__":
    app.run(debug=True)