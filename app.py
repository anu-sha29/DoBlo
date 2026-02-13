from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

# --- Database Setup ---
def init_db():
    conn = sqlite3.connect("donors.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS donors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    weight INTEGER,
                    blood_group TEXT,
                    phone TEXT,
                    last_donation TEXT
                )""")
    conn.commit()
    conn.close()

init_db()

# --- Choice screen ---
@app.route("/")
def index():
    return render_template("index.html")

# --- Donor registration ---
@app.route("/donor", methods=["GET", "POST"])
def donor():
    if request.method == "POST":
        name = request.form.get("name")
        age = int(request.form.get("age"))
        weight = int(request.form.get("weight"))
        blood_group = request.form.get("blood_group")
        phone = request.form.get("phone")
        last_donation = request.form.get("last_donation")

        recent_donation = request.form.get("recent_donation")
        medication = request.form.get("medication")
        chronic_illness = request.form.get("chronic_illness")
        recent_surgery = request.form.get("recent_surgery")
        infection = request.form.get("infection")
        pregnancy = request.form.get("pregnancy")

        # Eligibility logic
        eligible = True
        if age < 18 or weight < 50:
            eligible = False
        elif recent_donation == "yes":
            eligible = False
        elif medication == "yes" or chronic_illness == "yes":
            eligible = False
        elif recent_surgery == "yes" or infection == "yes":
            eligible = False
        elif pregnancy == "yes":
            eligible = False

        if eligible:
            # Save donor to database
            conn = sqlite3.connect("donors.db")
            c = conn.cursor()
            c.execute("INSERT INTO donors (name, age, weight, blood_group, phone, last_donation) VALUES (?, ?, ?, ?, ?, ?)",
                      (name, age, weight, blood_group, phone, last_donation))
            conn.commit()
            conn.close()
            return render_template("notify.html", message="✅ You are eligible and registered as a donor!")
        else:
            return render_template("notify.html", message="❌ Not eligible to donate.")

    return render_template("donor.html")

# --- Blood request ---
@app.route("/request", methods=["GET", "POST"])
def blood_request():
    if request.method == "POST":
        blood_group = request.form.get("blood_group")
        units = int(request.form.get("units"))
        urgency = request.form.get("urgency")

        conn = sqlite3.connect("donors.db")
        c = conn.cursor()
        c.execute("SELECT name, blood_group, phone, age, weight, last_donation FROM donors")
        donors = c.fetchall()
        conn.close()

        # Simple compatibility check (can be expanded)
        eligible_donors = [ {"name": d[0], "blood_group": d[1], "phone": d[2]} for d in donors if d[1] == blood_group ]

        return render_template("notify.html",
                               message=f"🚨 Matching donors for {blood_group}, {units} units ({urgency})",
                               donors=eligible_donors[:units*2])
    return render_template("request.html")

if __name__ == "__main__":
    app.run(debug=True)