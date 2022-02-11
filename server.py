import os

import flask
from dotenv import load_dotenv
from flask import Flask, render_template, request, session
from flask_session import Session

import init_database
import mod_database
import twilio_codes
from decorators import check_session

# Creates users table if it doesn't exist
init_database.main()

# Allows environment variables to be accessed
load_dotenv()


# Flask application

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Session(app)
port = 8080


# Flask routes

@app.route("/")
@app.route("/home")
def home_route():
	# Resets session for demonstration purposes
	session["username"] = None
	session["verified"] = False
	return render_template("base.html")


@app.route("/register", methods=["GET"])
@check_session(page="register")
def register_route_get():
	return render_template("register.html")


@app.route("/register", methods=["POST"])
@check_session(page="register")
def register_route_post():
	# Get data from user input
	data = request.get_json()
	# Attempt to register a new user
	registration_success, mobile_number, error = mod_database.register(
		data["username"],
		data["password"],
		data["mobile_number"]
	)
	# Checks if registration was successful
	if registration_success:
		# Set session
		session["username"] = data["username"]
		session["mobile_number"] = mobile_number
		print("Mobile num added")
		return {"success": registration_success, "error": error}
	else:
		# Display error
		return {"success": registration_success, "error": error}


@app.route("/login", methods=["GET"])
@check_session(page="login")
def login_route_get():
	return render_template("login.html")


@app.route("/login", methods=["POST"])
@check_session(page="login")
def login_route_post():
	# Get data from user input
	data = request.get_json()
	# Attempt to log in user
	login_success, mobile_number, error = mod_database.verify_credentials(data["username"], data["password"])
	# Checks if login was successful
	if login_success:
		# Set session
		session["username"] = data["username"]
		session["mobile_number"] = mobile_number
		return {"success": login_success, "error": error}
	else:
		# Display error
		return {"success": login_success, "error": error}


@app.route("/authenticate", methods=["GET"])
@check_session(page="authenticate")
def authenticate_route_get():
	twilio_codes.send_code(session["mobile_number"])
	return render_template("authenticate.html")


@app.route("/authenticate", methods=["POST"])
@check_session(page="authenticate")
def authenticate_route_post():
	# Attempts to verify code input
	verification_status = twilio_codes.check_code(request.form["code_textbox"])
	# Checks if verification was successful
	if verification_status:
		print("VERIFIED")
		session["verified"] = True
		return flask.redirect("/landing")
	else:
		return render_template("authenticate.html", error=True)


@app.route("/resend-code", methods=["POST"])
@check_session(page="resend")
def resend_route():
	if session["mobile_number"]:
		twilio_codes.send_code(session["mobile_number"])
		return {"success":  True, "error": None}
	else:
		return {"success": False, "error": "Code could not be sent."}


@app.route("/landing")
@check_session(page="landing")
def landing_route():
	return render_template("landing.html", username=session["username"])


@app.route("/logout")
@check_session(page="logout")
def logout_route():
	session["username"] = None
	session["mobile_number"] = None
	session["verified"] = False
	return flask.redirect("/")


# Runs the webserver
app.run(host="localhost", port=port)
