import flask
from flask import Flask, render_template, request
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

# from https://www.twilio.com/docs/verify/api/verification
# sends a verification code to the receiving number
def sendCode():
	verification = client.verify \
		.services(os.getenv("VERIFICATION_SID")) \
		.verifications \
		.create(to=os.getenv("RECEIVING_NUM"), channel="sms")

	print(verification.sid)

# from https://www.twilio.com/docs/verify/api/verification-check
# something up on line 26? these docs do not make sense
def checkCode(code_input):
	verification_check = client.verify \
		.services(os.getenv("VERIFICATION_SID")) \
		.verification_checks \
		.create(verification_sid=os.getenv("VERIFICATION_SID"), code=code_input)

	print(verification_check.status)

sendCode()
code_input = input("Enter code: ")
checkCode(code_input)


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
	return render_template("base.html")


@app.route("/login", methods=["GET", "POST"])
def login_route():
	if request.method == "GET":
		return render_template("login.html")
	account_string = "Username " + request.form["username"] + " logged in."
	send_message(account_string)
	return flask.redirect("/landing")


@app.route("/landing")
def landing_route():
	return render_template("landing.html")


app.run(host="localhost", port=port)

