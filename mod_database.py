import sqlite3
import bcrypt

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
		row_dict[column[0]] = row[index] # set the key equal to the column name, and value to the columns data in the row
	return row_dict


# Sets row processing to return dicts
db.row_factory = dict_factory


# Add new user to database
# Figure out what errors get raised to tell user that username/number already in use?
def register(new_username, new_password, new_mobile_number):
	try:
		db.execute("INSERT INTO users(username, password, mobile_number) VALUES(?, ?, ?);",
					[new_username, hash_password(new_password), new_mobile_number])
	except sqlite3.IntegrityError:
		print("Username or Mobile Number already in use")
		return False, None
	else:
		print("User added!")
		db.commit()  # Updates db with new additions
		return True, new_mobile_number


cursor = db.execute("SELECT * FROM users;")  # Selects all data from db

# data = cursor.fetchall()  # Sets data equal to all in db


def verify_credentials(username, password):

	user = db.execute("SELECT * FROM users WHERE username = ?", [username]).fetchone()
	if user:
		pass_match = bcrypt.checkpw(password.encode("UTF-8"), user["password"])
		if pass_match:
			print("yaycheese :)")
			print(user["mobile_number"])
		else:
			print("moldy cheese :/")
	else:
		print("nocheese :(")


# print("Enter username and password")
# username = input("Username: ")
# password = input("Password: ")
# verify_credentials(username, password)
