# mysql sqlalchemy will not create a db only connect to one
# so use GUi to create the DB
# you need to pip install: mysql-connector-python, sqlalchemy
# this .py uses SQLAlchemy ORM

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/dbname",
	echo=True)
Base = declarative_base()    #this is specific to sqlalchemy ORM

class Mytable1name(Base):
	__tablename__ = 'mytable1name'
	__table_args__ = {'schema':'dbname'}

	col_id_specific_to_table1 = Column(Integer, primary_key=True)
	col2 = Column(String(length=50))
	col3 = Column(String(length=50))

	def __repr__(self):
		return "<Mytable1name(col2'{0}', col3='{1}, ...)'>".format(
			self.col2, self.col3, ...)

class Mytable2name(Base):
	__tablename__ = 'mytable2name'
	__table_args__ = {'schema':'dbname'}

	col_id_specific_to_table2 = Column(Integer, primary_key=True)
	col_id_specific_to_table1 = Column(Integer, ForeignKey('dbname.mytable1name.col_id_specific_to_table1'))
	col3 = Column(String(length=50))

	relation_for_foreign_key = relationship("Mytable1name")   #use the name of the class not the name of the table, (M not m)

	def __repr__(self):
		return "<Mytable2name(col3='{0}, ...)'>".format(self.col3, ...)

Base.metadata.create_all(engine)

----------
## to query the db we need a sessionmaker
session_maker = sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()

# inserting values; use the Class defined above
value_for_table1 = Mytable1name(col2='Value', col3='Value', ...)
session.add(value_for_table1)    # if you add only one value
session.commit()

value_for_table2 = [Mytable2name(col_id_specific_to_table1=value_for_table1.col_id_specific_to_table1, col3='Value1'),
Mytable2name(col_id_specific_to_table1=value_for_table1.col_id_specific_to_table1, col3='Value2'),
Mytable2name(col_id_specific_to_table1=value_for_table1.col_id_specific_to_table1, col3='Value3'),...]
session.bulk_save_objects(value_for_table2)    # if you add multiple values
session.commit()

# filter records
query_table1 = session.query(Mytable1name).filter_by(col2='Value').first()    #use first if you want only 1 result
print(query_table1)

query_table2 = session.query(Mytable2name).all()    #use all if you want to retrieve all results
print(query_table2)
