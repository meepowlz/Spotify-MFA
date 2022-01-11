import flask
from flask import Flask, render_template, request
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)


# code snippet from https://www.twilio.com/docs/verify/api/verification
# sends a verification code to the receiving number
def send_code():
	verification = client.verify \
		.services(os.getenv("VERIFICATION_SID")) \
		.verifications \
		.create(to=os.getenv("RECEIVING_NUM"), channel="sms")

	print(verification.sid)


# code snippet from https://www.twilio.com/docs/verify/api/verification-check
# checks sms verification
def check_code(code_input):
	verification_check = client.verify \
		.services(os.getenv("VERIFICATION_SID")) \
		.verification_checks \
		.create(to=os.getenv("RECEIVING_NUM"), code=code_input)

	print(verification_check.status)


# code snippet from https://www.twilio.com/docs/sms/send-messages
# sends an sms message
def send_message(message_text):
	message = client.messages.create(
		to=os.getenv("RECEIVING_NUM"),
		from_=os.getenv("TWILIO_NUM"),
		body=message_text)

	print(message.sid)


app = Flask(__name__)
port = 8080


@app.route("/")
def home_route():
	return flask.redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login_route():
	if request.method == "GET":
		return render_template("login.html")
	else:
		send_code()
		return flask.redirect("/authenticate")

@app.route("/authenticate", methods=["GET", "POST"])
def authenticate_route():
	if request.method == "GET":
		return render_template("authenticate.html")
	else:
		user_input = request.form["code_textbox"]
		check_code(user_input)
		return flask.redirect("/landing")


@app.route("/landing")
def landing_route():
	return render_template("landing.html")


app.run(host="localhost", port=port)

