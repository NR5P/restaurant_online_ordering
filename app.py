from flask import Flask, render_template, url_for, session, redirect
from flask_moment import Moment
from datetime import datetime
from forms import SignUpForm

app = Flask(__name__)
#moment = Moment(app)
app.config["SECRET_KEY"] = "thisisasecretkey"

@app.route("/")
def index():
    return render_template("index.html", title="home", current_time=datetime.utcnow())

@app.route("/about/")
def about():
    return render_template("about.html", title="about")

@app.route("/menu/")
def menu():
    return render_template("menu.html", title="menu")

@app.route("/signup/", methods=["GET", "POST"])
def signup():
    name = None
    form = SignUpForm()
    if form.validate_on_submit():
        session["name"] = form.firstName.data
        return redirect(url_for("menu"))
    return render_template("signup.html", title ="signup", form=form, name=name)

@app.route("/admin/")
def admin():
    return render_template("admin.html", title="admin")

if __name__ == "__main__":
    app.run(debug=True)