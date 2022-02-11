import os

from dotenv import load_dotenv
from twilio.rest import Client

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
	client.verify \
		.services(os.getenv("VERIFICATION_SID")) \
		.verifications \
		.create(to=receiving_num, channel="sms")


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
