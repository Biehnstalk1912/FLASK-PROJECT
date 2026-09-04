from flask import Flask, render_template
import pymysql
import time
import json


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Data connects
def get_latest_mysql_date():
    with pymysql.connect(host='localhost', user='root', password='', database='flask_project') as conn:
        with conn.cursor() as cursor:  
            cursor.execute("SELECT State, Quantity FROM orders_table ORDER BY Order_Date DESC LIMIT 50")
            rows = cursor.fetchall()
            return rows
        
        
@app.route('/stream')
def stream():
    def generate():
        while True:
            rows = get_latest_mysql_date()
            data = []
            json_data = [{"State": row[0], "Quantity": row[1]} for row in rows]
            data.append(json_data)
            yield f"data: {json.dumps(data)}\n\n"
            time.sleep(3)
    return app.response_class(generate(), mimetype='text/event-stream')





if __name__ == "__main__":
    app.run(debug=True)