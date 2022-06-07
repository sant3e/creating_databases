# mysql db needs a server (install MySQL Community Server)
# creating the db and tables can be done via a Python application (like we did in the sqlite_db.py)
# or using MySQL's GUi (MySQL Workbench) or even in a terminal

# to connect in Python, we need pip install mysql-connector (do this in an venv)

import mysql.connector as mysql

def connect(db_name):
	try:
		return mysql.connect(
			host='localhost',
			user='root',
			password='password',
			database=db_name)
	except Error as e:
		print(e)

if __name__ == '__main__':
	db = connect("projects")
	cursor = db.cursor()

	cursor.execute("SELECT * FROM projects")
	project_records = cursor.fetchall()
	print(project_records)

	db.close()
