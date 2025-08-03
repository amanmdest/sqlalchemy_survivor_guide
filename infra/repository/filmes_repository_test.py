from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from infra.entities.filmes import Filmes
from infra.entities.atores import Atores
from infra.repository.filmes_repository import FilmesRepository

from sqlalchemy.orm import sessionmaker


class ConnectionHandlerMock:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [
                        mock.call.query(Filmes),
                    ],
                    # [Filmes(titulo="Seven", genero="Thriller", ano=1995)],
                    [Filmes(titulo="Seven", genero="Drama", ano=1995)],
                ),
                (
                    [
                        mock.call.query(Filmes),
                        # mock.call.filter(Filmes.genero=="Thriller")
                        mock.call.filter(Filmes.genero=="Drama")
                    ],
                    # [Filmes(titulo="Seven", genero="Thriller", ano=1995)],
                    [Filmes(titulo="Seven", genero="Drama", ano=1995)],
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


def test_select():
    filme_repository = FilmesRepository(ConnectionHandlerMock)
    response = filme_repository.select()
    print()
    print(response)
    
    assert isinstance(response, list)
    assert isinstance(response[0], Filmes)


def test_select_drama_filme():
    filme_repository = FilmesRepository(ConnectionHandlerMock)
    response = filme_repository.select_drama_filme()
    print()
    print(response)

    assert isinstance(response, Filmes)
    assert response.titulo == 'Seven'


def test_insert():
    filme_repository = FilmesRepository(ConnectionHandlerMock)
    response = filme_repository.insert('Fallen Angels', 'Noir-crime', 1995)
    print()
    print(response)
    
    assert isinstance(response, Filmes)
    assert response.titulo == "Fallen Angels"


# def test_select():
#     response = session.query(Filmes).filter(Filmes.genero=="Thriller").all()
#     print()
#     print(response) # [Filme [titulo=Seven, ano=1995]] # pytest -s

    # assert response == '[Filme [titulo=Seven, ano=1995]]'