from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer 
from sqlalchemy.orm import sessionmaker

# Configs
engine = create_engine('mysql+pymysql://root:passtest@localhost:3306/cinema')
conn = engine.connect()
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Entidades
class Filmes(Base):
    __tablename__ = "filmes"

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Filme [titulo={self.titulo}, ano={self.ano}]"

# SQL    

# Insert
# data_insert = Filmes(titulo="Aquarius", genero="Drama", ano=2015) # objeto da classe
# session.add(data_insert)
# session.commit()

# Delete
# data = session.query(Filmes).filter(Filmes.titulo=="Forest Gump").delete()
# session.commit()

# Update
# data = session.query(Filmes).filter(Filmes.genero=="Mindfuck").update({ "genero": "Horror" })
# session.commit()

# Select
data = session.query(Filmes).all()
print(data)
print(data[0].titulo) # Aquarius
print(data[1].genero) # Horror


session.close()

