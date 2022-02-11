import sqlite3

import bcrypt

# Connects to database
db = sqlite3.connect("database.db", check_same_thread=False)


def hash_password(password: str) -> bytes:
	"""
	Hashes and salts a password
	:param password: str
	:return: bytes
	"""
	salt = bcrypt.gensalt()
	return bcrypt.hashpw(password.encode("UTF-8"), salt)


def dict_factory(cursor, row):
	"""
	Populates row dict with user info
	:param cursor: object
	:param row: tuple
	:return: dict
	"""
	row_dict = {}
	for index, column in enumerate(cursor.description):  # iterate through every column and get an index of it's position
		row_dict[column[0]] = row[index]  # set the key equal to the column name, and value to the columns' data in the row
	return row_dict


# Sets row processing to return dicts
db.row_factory = dict_factory


# Add new user to database
# Figure out what errors get raised to tell user that username/number already in use?
def register(new_username, new_password, new_mobile_number):
	"""
	Registers a new user
	:param new_username: str
	:param new_password: str
	:param new_mobile_number: str
	:return: bool, str, str
	"""
	try:
		db.execute("INSERT INTO users(username, password, mobile_number) VALUES(?, ?, ?);",
					[new_username, hash_password(new_password), new_mobile_number])
	except sqlite3.IntegrityError:
		print("Username or Mobile Number already in use")
		return False, None, "Username or Mobile Number is already in use"
	else:
		print("User added!")
		db.commit()  # Updates db with new additions
		return True, new_mobile_number, None


def verify_credentials(username, password):
	"""
	Attempts to verify a user on login
	:param username: str
	:param password: str
	:return:
	"""
	user = db.execute("SELECT * FROM users WHERE username = ?", [username]).fetchone()
	if user:
		pass_match = bcrypt.checkpw(password.encode("UTF-8"), user["password"])
		if pass_match:
			return True, user["mobile_number"], None
	return False, None, "Username or Password is incorrect"
