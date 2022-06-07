# sqlite is a simple local DB
# connecting to a local DB & creating a table

import sqlite3

connection = sqlite3.connect('mydbname.db')

cursor = connection.cursor()

# chose the column names and data type for each
cursor.execute('''CREATE TABLE IF NOT EXISTS mytablename
	(col1 type1, col2 type2, col3 type3)''')

connection.commit()
connection.close()


-------------------------
## Additional commands (place them between curosr and connection.comit()

# Insert (manual) values into table (text and data need ' ' )
 cursor.execute("INSERT INTO mytablename VALUES ('Value1', 'Value2', 'Value3')")
  
# Insert (manual) multiple values at once into table
# declare a list of values, create a variable with it, insert it with ??? (for security purposes)
variablename = [('Value11', 'Value12', 'Value13'),
                ('Value21', 'Value22', 'Value23'),
                ('Value31', 'Value32', 'Value33')]
cursor.executemany('Insert INTO mytablename VALUES (?,?,?)', variablename)
  
## Cheking values
# we have multiple ways:
# a) fetch a single row
# b) iterate through every row
# c) fetch all results at once
cursor.execute("SELECT * FROM mytablename")
print(cursor.fetchone())    # a)
  
# Checking values alternative
records = cursor.execute("SELECT * FROM Movies")
print(cursor.fetchall())
for record in records:
  print(record)
# fetches a single row
cursor.fetchone()
