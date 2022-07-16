class Programas():
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome:{self._nome} - Ano:{self.ano} - Likes:{self._likes}'


class Filme(Programas):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  # chama da classe mae
        self.duracao = duracao

    def __str__(self):
        return f'Nome:{self._nome} - Ano:{self.ano} - Likes:{self._likes} - Duração:{self.duracao}'


class Serie(Programas):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)  # chama da classe mae
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome:{self._nome} - Ano:{self.ano} - Likes:{self._likes} - Temporadas:{self.temporadas}'


class Playlist():  # poderia herdar list mas como nao conhecemos tudo pode gerar um bug
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas  # array

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

lista = [vingadores, atlanta]

playlist_fim_de_semana = Playlist("findi", lista)

for programa in lista:
    print(programa)

print(f'Tamanho: {playlist_fim_de_semana.tamanho}')
