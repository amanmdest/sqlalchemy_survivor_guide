from infra.repository.filmes_repository import FilmesRepository
from infra.repository.atores_repository import AtoresRepository

repo = FilmesRepository()
repo2 = AtoresRepository()
print(repo) # <infra.repository.filmes_repository.FilmesRepository object at 0x7faa04db9b80>

# repo.insert('Duna', 'Ficcao Cientifica', 2022)
# repo.insert('The Little Hours', 'Comedia', 2017)
# repo.insert('LOTR: Two Towers', 'Fantasia', 2002) #TODO: como colocar vários gêneros

# repo.update('Mr. Nobody', 'Ficcao Cientifica')
# repo.update('LOTR: Two Towers', 'Aventura')

# repo.delete('The Little Hours')

response = repo.select()
filme = response[0]
# print(response)
print(filme)
print(filme.titulo)
print(filme.atores)

response2 = repo2.select()
print(response2)
