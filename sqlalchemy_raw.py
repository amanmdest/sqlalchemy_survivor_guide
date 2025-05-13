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
# data_insert = Filmes(titulo="The Little Hours", genero="Comêdia", ano=2017) # objeto da classe
# session.add(data_insert)
# session.commit()

# Delete
# data = session.query(Filmes).filter(Filmes.titulo=="Forest Gump").delete()
# session.commit()

# Update
data = session.query(Filmes).filter(Filmes.genero=="Comêdia").update({ "genero": "Comedia" })
# data = session.query(Filmes).filter(Filmes.genero=="Drama").update({ "ano": "2016" })
session.commit()

# Select
data = session.query(Filmes).all()
print(data) 
print(data[0].titulo) # Aquarius
print(data[1].genero) # Horror


session.close()


# The Godfather - Policial
# Filme de 1972
