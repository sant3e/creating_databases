import psycopg2

conn = psycopg2.connect(database="dbname",
	user="postgres",
	password="password",
	host="localhost",
	port="5432")

cursor = conn.cursor()

# creating the table
cursor.execute('''CREATE TABLE mytablename
	(ID INT PRIMARY KEY,
		col2 TEXT,
		col3 TEXT,
		col4 FLOAT);''')

# (manual) inserting a value into the table
cursor.execute('''INSERT INTO mytablename(ID, 
	col2, col3, col4) VALUES
	(1105910, 'Value1', 'Value2', 'Value3', 
		'Value4')''')

# secure (manual) inserting a value into the table
insert_data = (id, col2, col3, col4)
cursor.execute('''INSERT INTO mytablename(id, col2, col3, col4

# Filtering data
cursor.execute("SELECT col2, col3 from mytablename WHERE ID=1105910")
rows = cursor.fetchall()
for row in rows:
	print("col2 =", row[0])
	print("col3 =", row[1],"\n")
  
  
  -----
# deleting records
cursor.execute('''DELETE FROM mytablename WHERE id=xxxx''')
  
# inserting with functions with input
def insert_record(conn, id, col2, col3, col4,...):
  new_record = (id, col2, col3, col4)
  cursor = conn.cursor()
  cursor.execute('''INSERT INTO tablename(id, col2, col3, col4)
                    VALUES (%s, %s, %s, %s)''', new_record)
  conn.commit()

## inserting can also be more complex, like calculated columns
## just add in the insert_record function (this is a mock example)
  order_total = quantity * price
  if discount != 0:
    order_total = order_total * discount
    
    
if __name__ == '__main__':
  id = int(input('text\n"))
  col2 = input('text\n")
  col3 = input('text\n")
  col4 = float(input('text\n")
  
  insert_data(conn, id, col2, col3, col4)
  print('Data inserted!')
  
  conn.close()
  # the commit part will be present within the function
                      
  
  
conn.commit()
conn.close()
