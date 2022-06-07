# mysql db needs a server (install MySQL Community Server)
# creating the db and tables can be done via:
# Python application (like we did in the sqlite_db.py) or
# using MySQL's GUi (MySQL Workbench) or 
# in a terminal (like CMD in Windows)

# to connect in Python, we need pip install mysql-connector-python (do this in an venv)

# this code just connects to an already existant db (assume we created it in GUi which is easier)
import mysql.connector as mysql

def connect(db_name):
	try:
		return mysql.connect(
			host='localhost or server address',
			user='root',
			password='password',
			database=db_name)
	except Error as e:
		print(e)

if __name__ == '__main__':
	db = connect("mydbname")
	cursor = db.cursor()
	db.close()
	
	# Checking the records
	cursor.execute("SELECT * FROM mytablename")
	print(cursor.fetchall())

	
