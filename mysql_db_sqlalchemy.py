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
