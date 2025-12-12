from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="meenakshi"
)

cursor = db.cursor()


@app.route("/")
def home():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    return render_template("index.html", students=data)


@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        classes = request.form["classes"]
        marks = request.form["marks"]

        query = "INSERT INTO students (name, age, classes, marks) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, age, classes, marks))
        db.commit()

        return redirect("/")
    return render_template("add.html")


@app.route("/update/<name>", methods=["GET", "POST"])
def update_student(name):
    if request.method == "POST":
        age = request.form["age"]
        classes = request.form["classes"]
        marks = request.form["marks"]

        query = "UPDATE students SET age=%s, classes=%s, marks=%s WHERE name=%s"
        cursor.execute(query, (age, classes, marks, name))
        db.commit()

        return redirect("/")

    cursor.execute("SELECT * FROM students WHERE name=%s", (name,))
    data = cursor.fetchone()
    return render_template("update.html", student=data)


@app.route("/delete/<name>")
def delete_student(name):
    cursor.execute("DELETE FROM students WHERE name=%s", (name,))
    db.commit()
    return redirect("/")


@app.route("/search", methods=["GET", "POST"])
def search_student():
    if request.method == "POST":
        name = request.form["name"]
        cursor.execute("SELECT * FROM students WHERE name=%s", (name,))
        data = cursor.fetchone()
        return render_template("search.html", student=data)
    return render_template("search.html", student=None)


if __name__ == "__main__":
    app.run(debug=True)
