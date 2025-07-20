from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Home route to confirm API is working
@app.route('/')
def home():
    return "✅ Mohammad Crane Service API is Live!"

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB = "cloud_data.db"

def connect():
    return sqlite3.connect(DB)

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO entries (name, phone, alt_phone, vehicles, pincode, district, area, transport) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (data["name"], data["phone"], data["alt_phone"], data["vehicles"], data["pincode"], data["district"], data["area"], data["transport"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Data saved!"})

@app.route("/entries", methods=["GET"])
def get_all():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM entries")
    rows = cur.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run()
