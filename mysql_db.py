# mysql db needs a server (install MySQL Community Server)
# creating the db and tables can be done via:
# Python application (like we did in the sqlite_db.py) or
# using MySQL's GUi (MySQL Workbench) or 
# in a terminal (like CMD in Windows)

# to connect in Python, we need pip install mysql-connector-python (do this in an venv)

# this code just connects to an already existant db (assume we created it in GUi which is easier)
import mysql.connector as mysql
import csv    # only if you import from csvs

# connection to DB configuration using a function
def connect(db_name):
	try:
		return mysql.connect(
			host='localhost or server address',
			user='root',
			password='password',
			database='db_name',
			allow_local_infile=True)
	except Error as e:
		print(e)

# (manual) adding new records using a function
def add_new_values():
	table_data_single_entry = ('Value1', 'Value2', ... )   
	cursor.execute("INSERT INTO mytablename(col1, col2, ...) VALUES (%s, %s, ...)", table_data_single_entry)
	
	table_data_multiple_entries = [('Value11', 'Value12',...),('Value21', 'Value22', ...),...]   # a list of multiple tuples
	cursor.executemany("INSERT into mytablename(col1, col2, ...) VALUES (%s, %s, ...)", table_data_multiple_entries)
	
	## if we work with multiple tables and we want to take the id for a record from one table to another
	id = cursor.xxxx    # don't have the code for this yet, i need to pull the id values from another table
	table_data_multiple_entries = [(id, 'Value12', 'Value13',...),(id, 'Value22', 'Value23', ...),...]   # a list of multiple tuples
	cursor.executemany("INSERT into mytablename(col1, col2, ...) VALUES (%s, %s, ...)", table_data_multiple_entries)

# importing records from csv file
create_query = '''CREATE TABLE mytablename(
		id INT(10) NOT NULL AUTO_INCREMENT,
		col2 VARCHAR(255) NOT NULL
		col3 VARCHAR(255) NOT NULL
		PRIMARY KEY (id))'''
cursor.execute("DROP TABLE IF EXISTS mytablename")

if __name__ == '__main__':
	db = connect("mydbname")
	cursor = db.cursor()
		
	# Checking the records
	cursor.execute("SELECT * FROM mytablename")
	print(cursor.fetchall())
	
	db.close()
	
# (if we intended to to create the table within python) for the primary key we need: table1_id INT(n) NOT NULL AUTO_INCREMENT, col2 type2, col3 type3, ..., PRIMARY KEY(table1_id)
# (if we intended to to create the table within python) for the primary key we need: table2_id INT(n) NOT NULL AUTO_INCREMENT, table1_id INT(n), col3 type4, 
# , col4 type4, ..., FOREIGN KEY(table2_id) REFERENCES mytable1name(table1_id)
