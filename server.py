from flask import Flask

app = Flask(__name__)
port = 8080

@app.route("/")
def home_route():
	return "Home page"

@app.route("/login")
def login_route():
	return "Login page"

@app.route("/landing")
def landing_route():
	return "Login Successful. Landing page"

# @app.route("/404")
# def error_route():
# 	return "Page not found"

app.run(host="localhost", port=port)

