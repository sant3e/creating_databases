import pandas
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/dbname')

Base = declarative_base()

class Mytable1name(Base):
	__tablename__ = 'mytablename'
	__table_args__ = {"schema":"dbname"}

	id = Column(Integer, primary_key=True)
	col2 = Column(String(250))
	col3 = Column(String(250))
	col4 = Column(Integer)
	col5 = Column(Float)

	def __repr__(self):
    # we use here the Class name (M not m)
		return '''<Mytable1name(id='{0}', col2='{1}', 
			col3='{2}', col4='{3}', 
			col5='{4}')>'''.format(self.id,
			self.col2, self.col3,
			self.col4, self.col5)

Base.metadata.create_all(engine)

file_name = "mycsvfile.csv"

df = pandas.read_csv(file_name)

df.to_sql(con=engine, name=Mytable1name.__tablename__, if_exists='append', index=False)

session = sessionmaker()
session.configure(bind=engine)
s = session()

# check records
results = s.query(Mytable1name).limit(10).all()
for r in results:
	print(r)
