import flask
from flask import Flask, render_template, request, session
from flask_session import Session
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Allows environment variables to be accessed
load_dotenv()


# Twilio

# Sets up Twilio client object(?) for sending verification codes
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)


# code snippet from https://www.twilio.com/docs/verify/api/verification
# sends a verification code to the receiving number
def send_code(receiving_num):
	verification = client.verify \
		.services(os.getenv("VERIFICATION_SID")) \
		.verifications \
		.create(to=receiving_num, channel="sms")

	print(verification.sid)


# code snippet from https://www.twilio.com/docs/verify/api/verification-check
# checks sms verification
def check_code(code_input):
	verification_check = client.verify \
		.services(os.getenv("VERIFICATION_SID")) \
		.verification_checks \
		.create(to=os.getenv("RECEIVING_NUM"), code=code_input)

	print(verification_check.status)
	if verification_check.status == "approved":
		return True
	else:
		return False


# code snippet from https://www.twilio.com/docs/sms/send-messages
# sends an sms message
# just for testing !!
def send_message(message_text):
	message = client.messages.create(
		to=os.getenv("RECEIVING_NUM"),
		from_=os.getenv("TWILIO_NUM"),
		body=message_text)

	print(message.sid)


# Flask application

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
port = 8080


# Checks if a user is logged in or authenticated at each page
# Fix: needs to stop if on the correct page
# Fix: needs to actually redirect
def check_session(page):
	print(session["username"])
	print(session["verified"])
	if not session.get("username") and page != "login":
		print("Redirected to login")
		return flask.redirect("/login")
	elif not session.get("verified") and page != "authenticate":
		print("Redirected to authenticate")
		return flask.redirect("/authenticate")
	elif page != "landing":
		print("Redirected to landing")
		return flask.redirect("/landing")


@app.route("/")
def home_route():
	return check_session("home")


@app.route("/login", methods=["GET", "POST"])
def login_route():
	check_session("login")
	if request.method == "POST":
		# Saves username
		session["username"] = request.form.get("username")
		# Sends 6-digit verification code
		send_code(request.form["mobile_number"])
		return flask.redirect("/authenticate")
	return render_template("login.html")


@app.route("/authenticate", methods=["GET", "POST"])
def authenticate_route():
	check_session("authenticate")
	if request.method == "POST":
		verification_status = check_code(request.form["code_textbox"])
		if verification_status:
			session["verified"] = True
			return flask.redirect("/landing")
		else:
			return render_template("authenticate.html", auth_status="Authentication failed")
	return render_template("authenticate.html")


@app.route("/landing")
def landing_route():
	check_session("landing")
	return render_template("landing.html")


@app.route("/logout")
def logout_route():
	session["username"] = None
	session["password"] = None
	session["verified"] = False  # should this be none?
	return flask.redirect("/")


app.run(host="localhost", port=port)

