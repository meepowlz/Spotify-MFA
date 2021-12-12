from flask import Flask, render_template, request

app = Flask(__name__)
port = 8080

@app.route("/")
def home_route():
	return render_template("base.html")

@app.route("/login", methods=["GET", "POST"])
def login_route():
	if request.method == "GET":
		return render_template("login.html")
	print(request.form["username"], request.form["password"])
	return "Cheese"

@app.route("/landing")
def landing_route():
	return render_template("landing.html")

app.run(host="localhost", port=port)

