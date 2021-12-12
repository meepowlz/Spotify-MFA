from flask import Flask, render_template

app = Flask(__name__)
port = 8080

@app.route("/")
def home_route():
	return render_template("base.html")

@app.route("/login")
def login_route():
	return render_template("login.html")

@app.route("/landing")
def landing_route():
	return render_template("landing.html")

app.run(host="localhost", port=port)

