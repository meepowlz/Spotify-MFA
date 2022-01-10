from flask import Flask, render_template, request
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18134822530",
    from_="+12512988473",
    body="Hello from Python!")

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
	print(request.form["username"], request.form["password"])
	return "Login Successful"


@app.route("/landing")
def landing_route():
	return render_template("landing.html")


app.run(host="localhost", port=port)

