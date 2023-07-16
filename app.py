from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config["SECRET_KEY"] = "1qwerty"


def create_db():
    db = sqlite3.connect(
        r"C:\Users\Prajwal\Desktop\mini Proj\New folder\data.db")
    return db


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        loc = request.form.get("loc")
        db = create_db()
        db.execute(f"insert into user (name,loc) values('{name}','{loc}')")
        db.commit()
        return redirect(url_for("home"))
    else:
        db = create_db()
        cur = db.execute("select * from user ")
        data = cur.fetchall()

        return render_template("home.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
