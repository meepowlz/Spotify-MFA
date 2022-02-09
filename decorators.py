import flask
from flask import session, url_for
from functools import wraps


# Decorator for ensuring user is in an active session
# Checks if a user is logged in or authenticated at each page
def check_session(page):
	def decorator(function):
		@wraps(function)
		def wrapper():
			if not session.get("username"):
				if page != "login":
					print("Redirected to login")
					return flask.redirect(url_for("login_route_get"))
			elif not session.get("verified"):
				if page != "authenticate":
					print("Redirected to authenticate")
					return flask.redirect(url_for("authenticate_route"))
			elif page == "logout":
				return function()
			elif page != "landing":
				print("Redirected to landing")
				return flask.redirect(url_for("landing_route"))
			return function()
		return wrapper
	return decorator
