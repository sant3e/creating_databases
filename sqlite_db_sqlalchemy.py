# interracting with a sqlite db using slqalchemy core

import sqlalchemy as db

# connecting/creating to sqlite db (stored locally)
# for this .py file we use the table created in the sqlite_db.py file
# place the .py file in the same directory as the .db file
# if db exists it will connect to it;
# if db doesn't exist it will create it
engine = db.create_engine('sqlite:///mydbname.db')
connection = engine.connect()

# loading everything what's in the db into our app
metadata = db.MetaData()
movies = db.Table('mytablename', metadata, autoload=True, autoload_with=engine)

# just save&run; sqlalchemy doesn't require commit&close
--------------------------

## Additional commands we can use

# select all records
query = db.select([mytablename])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()  # this is what pulls the data

# after we "stored" the data, we can print it
print(result_set[0])    # just the first record
print(result_set[:2])   # first 2 records

# filtering records
query = db.select([mytablename]).where(mytablename.columns.col_n == "Value_x")
# e.g. from table movie, filter for "Avatar" in column "title"
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(result_set[0])

# inserting new records
query = mytablename.insert().values(Col_1="Value1", Col_2="Value_2", Col_3="Value_3")
connection.execute(query)
