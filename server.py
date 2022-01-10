import flask
from flask import Flask, render_template, request
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

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

