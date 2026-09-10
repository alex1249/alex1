import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("review.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db()
    subjects = conn.execute("SELECT * FROM subjects").fetchall()
    conn.close()
    return render_template("index.html", subjects=subjects)

@app.route("/subjects/<int:subject_id>")
def subject_detail(subject_id):
    conn = get_db()
    subject = conn.execute(
        "SELECT * FROM subjects WHERE id = ?", (subject_id,)
    ).fetchone()
    materials = conn.execute(
        "SELECT * FROM materials WHERE subject_id = ? ORDER BY date DESC",
        (subject_id,)
    ).fetchall()
    conn.close()
    return render_template("subject.html", subject=subject, materials=materials)

@app.route("/materials/<int:material_id>")
def material_detail(material_id):
    conn = get_db()
    material = conn.execute(
        "SELECT * FROM materials WHERE id = ?", (material_id,)
    ).fetchone()
    originals = conn.execute(
        "SELECT * FROM originals WHERE material_id = ?", (material_id,)
    ).fetchall()
    conn.close()
    return render_template("material.html", material=material, originals=originals)

if __name__ == "__main__":
    app.run(debug=True)