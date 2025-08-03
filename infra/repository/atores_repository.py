from infra.configs.connection import DBConnectionHandler
from infra.entities.atores import Atores
from infra.entities.filmes import Filmes

class AtoresRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session\
                .query(Atores)\
                .join(Filmes, Atores.titulo_filme == Filmes.titulo)\
                .with_entities(
                    Atores.nome,
                    # Filmes.genero,
                    Filmes.titulo
                )\
                .all()
            return data
    
    def insert(self, nome, titulo_filme):
        with DBConnectionHandler as db:
            try:
                data = Atores(nome=nome, titulo_filme=titulo_filme)
                db.session.add(data)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

            return data
        
    def update(self): ...

    def delete(self): ...
