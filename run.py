from infra.repository.filmes_repository import FilmesRepository

repo = FilmesRepository()
# print(repo)

repo.insert('Duna', 'Ficcao Cientifica', 2022)

repo.update('Mr. Nobody', 'Ficcao Cientifica')

repo.delete('The Little Hours')

data = repo.select()

print(data)