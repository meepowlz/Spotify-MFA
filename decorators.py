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
				if page != "register":
					if page != "login":
						return flask.redirect(url_for("login_route_get"))
			elif not (session.get("verified") and session.get("code_pending")):
				if page != "authenticate":
					return flask.redirect(url_for("authenticate_route_get"))
			elif page == "logout":
				return function()
			elif page != "landing":
				return flask.redirect(url_for("landing_route"))
			return function()
		return wrapper
	return decorator
