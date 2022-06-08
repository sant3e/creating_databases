import mysql.connector as mysql
import csv

connection = mysql.connect(user='root',
	password='password',
	host='localhost',
	database='dbname',
	allow_local_infile=True)

cursor = connection.cursor()

create_query = '''CREATE TABLE mytable(
	id INT(10) NOT NULL AUTO_INCREMENT,
	col2 VARCHAR(255) NOT NULL,
	col3 VARCHAR(255) NOT NULL,
  col4 VARCHAR(255) NOT NULL,
	PRIMARY KEY (id))'''

cursor.execute("DROP TABLE IF EXISTS mytablename")

cursor.execute(create_query)

# Method 1
# this does a row by row importing
with open('./mycsvfile.csv', 'r') as f:
	csv_data = csv.reader(f)
	for row in csv_data:
		print(row)
		row_tuple = tuple(row)
		cursor.execute('INSERT INTO mytablename(col2, col3, col4, ...) VALUES("%s", "%s", "%s", ...)', row_tuple)

# Method 2
# this does a bulk importing (=faster)
q = '''LOAD DATA LOCAL INFILE 
'/Users/author/desktop/mysql-csv-workspace/salespeople.csv'
 INTO TABLE salesperson FIELDS TERMINATED BY ',' ENCLOSED BY '"' 
 (first_name, last_name, email_address, city, state);'''
cursor.execute(q)


connection.commit()

# Check the records
cursor.execute("SELECT * FROM mytablename LIMIT 10")
print(cursor.fetchall())

connection.close()
