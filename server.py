import flask
import sqlite3
from flask import Flask, render_template, request, session
import twilio_codes
from flask_session import Session
import os
from dotenv import load_dotenv
from decorators import check_session


# Allows environment variables to be accessed
load_dotenv()


# Flask application
# Add secret key?

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Session(app)
port = 8080

db = sqlite3.connect("database.db")


@app.route("/")
@check_session(page="home")
def home_route():
	# resets session (temporary)
	session["username"] = None
	return render_template("base.html")


@app.route("/login", methods=["GET", "POST"])
@check_session(page="login")
def login_route():
	if request.method == "POST":
		data = request.get_json()
		# Saves username
		session["username"] = data["username"]
		# Sends 6-digit verification code
		twilio_codes.send_code(data["mobile_number"])
		return flask.redirect("/authenticate")
	return render_template("login.html")


@app.route("/authenticate", methods=["GET", "POST"])
@check_session(page="authenticate")
def authenticate_route():
	if request.method == "POST":
		# Attempts to verify code input
		verification_status = twilio_codes.check_code(request.form["code_textbox"])
		if verification_status:
			session["verified"] = True
			return flask.redirect("/landing")
		else:
			return render_template("authenticate.html", auth_status="Authentication failed")
	return render_template("authenticate.html")


@app.route("/landing")
@check_session(page="landing")
def landing_route():
	return render_template("landing.html")


@app.route("/logout")
@check_session(page="logout")
def logout_route():
	session["username"] = None
	session["password"] = None
	session["verified"] = False  # should this be none?
	return flask.redirect("/")


app.run(host="localhost", port=port)
