from flask import Flask, render_template, request
import pandas as pd
# Import Scripts
from scripts.create_csv import get_all_contracts_to_csv as get_all_contracts_to_csv
from scripts.connect_to_db import db_connect as db_connect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        
        # Get needed info from form
        start_date = request.form["contract-start"]
        end_date = request.form["contract-end"]
        
        # Format information for SQL query
        start_date_formatted = start_date + " 00:00:00.000"
        end_date_formatted = end_date + " 00:00:00.000"

        # Call function to create the file and store the name in a variable to download
        file = get_all_contracts_to_csv(start_date_formatted, end_date_formatted)
        df = pd.read_csv(file)
        df.to_csv(file, index=None)
        
        file = str(file)

        return render_template("download.html", file=file, datas = [df.to_html()], titles=[''])
    else:
        return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)