from infra.configs.connection import DBConnectionHandler
from infra.entities.filmes import Filmes

class FilmesRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Filmes).all()
            return data
        
    def insert(self, titulo, genero, ano):
        with DBConnectionHandler() as db:
            data_insert = Filmes(titulo=titulo, genero=genero, ano=ano)
            db.session.add(data_insert)
            db.session.commit()
            
    def update(self, titulo, genero):
        with DBConnectionHandler() as db:
            # db.session.query(Filmes).filter(Filmes.titulo == titulo).update({"ano": ano})
            db.session.query(Filmes).filter(Filmes.titulo == titulo).update({"genero": genero})
            db.session.commit()

    def delete(self, titulo):
        with DBConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
            db.session.commit()