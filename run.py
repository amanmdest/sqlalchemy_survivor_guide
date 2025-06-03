from infra.repository.filmes_repository import FilmesRepository
from infra.repository.atores_repository import AtoresRepository

repo_filmes = FilmesRepository()
repo_atores = AtoresRepository()
print(repo_filmes) # <infra.repository.filmes_repository.FilmesRepository object at 0x7faa04db9b80>

# repo_filmes.insert('Duna', 'Ficcao Cientifica', 2022)
# repo_filmes.insert('The Little Hours', 'Comedia', 2017)
# repo_filmes.insert('LOTR: Two Towers', 'Fantasia', 2002) #TODO: como colocar vários gêneros

# repo_filmes.update_gender('Mr. Nobody', 'Ficcao Cientifica')
# repo_filmes.update_gender('LOTR: Two Towers', 'Aventura')

# repo_filmes.delete('The Little Hours')

response = repo_filmes.select()
filme = response[0]
# print(response)
print(filme)
print(filme.titulo)
print(filme.atores)

response2 = repo_atores.select()
print(response2)

response3 = repo_filmes.select_drama_movie()
print(response3)
