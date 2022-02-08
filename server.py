import os
import sqlite3

import flask
from dotenv import load_dotenv
from flask import Flask, render_template, request, session

import init_database
import mod_database
import twilio_codes
from decorators import check_session
from flask_session import Session


# Creates users table if it doesn't exist
init_database.main()

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


@app.route("/")
@app.route("/home")
def home_route():
	# resets session (temporary)
	session["username"] = None
	return render_template("base.html")


@app.route("/register", methods=["GET"])
def register_route_get():
	return render_template("register.html")


@app.route("/register", methods=["POST"])
def register_route_post():
	# Get data from user input
	data = request.get_json()
	# Attempt to register a new user
	registration_success, mobile_number, error = mod_database.register(data["username"], data["password"], data["mobile_number"])
	if registration_success:
		session["username"] = data["username"]
		return {"success": registration_success, "error": error}
	else:
		return {"success": registration_success, "error": error}


@app.route("/login", methods=["GET", "POST"])
@check_session(page="login")
def login_route():
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
	session["verified"] = False  # should this be none?
	return flask.redirect("/")


app.run(host="localhost", port=port)
