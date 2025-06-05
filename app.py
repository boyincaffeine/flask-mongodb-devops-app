from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = "supersecretkey"

# MongoDB Atlas connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client['devops_db']
collection = db['data_collection']

# /api route - reads from JSON file
@app.route('/api')
def api_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    return jsonify(data)

# Form route - handles form submission
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        try:
            collection.insert_one({"name": name, "email": email})
            return redirect(url_for("success"))
        except Exception as e:
            flash(f"Error: {e}")
            return render_template("form.html")
    return render_template("form.html")

@app.route('/success')
def success():
    return "Data submitted successfully"

if __name__ == "__main__":
    app.run(debug=True)

