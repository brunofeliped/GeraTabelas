from random import shuffle
from contextlib import redirect_stdout

# Quantidade / Nomes das Equipes
teams = []
n = int(input("Digite a Quantidade de Equipes: "))

for i in range(0, n):
    i += 1
    t = "Equipe " + str(i).zfill(2)
    teams.append(t)

# Adicionando ítem "Folga" nos casos impares
qtdteams = len(teams)
if len(teams) % 2 != 0:
    teams.append("Folga")

# Shuffling equipes
shuffle(teams)

class Fixture():
    def __init__(self, home, away):
        if not all([type(x) is str for x in (home, away)]):
            raise TypeError("home and away must both be of type str")
        self.home = home
        self.away = away

    def __str__(self):
        """ Return home vs. away. """
        return f"{self.home};x;{self.away}"

# Total de Jogos / Jogos por Rodada
num_jogos = int((len(teams)) / 2) * int(len(teams) - 1)
jgs_por_rodada = len(teams) // 2
num_rod = num_jogos // jgs_por_rodada

# Aplicando Round Robin
def rearrange_items():
    copy = teams[:]
    for i in range(1, len(copy)):
        if i == 1:
            teams[i] = copy[-1]
        else:
            teams[i] = copy[i - 1]

# Gerando jogos de cada rodada
def gera_jogos_rodada():
    rodada = []
    i = 0
    while i < jgs_por_rodada:
        fixture = Fixture(teams[i], teams[-i - 1])
        rodada.append(fixture)
        i += 1
        print(fixture)

# Gerando tabela total de jogos
def gera_tabela():
    r = 0
    while r < num_rod:
        r += 1
        print("Rodada ", r)
        print("-" * 40)
        gera_jogos_rodada()
        rearrange_items()
        print()

# Salvando em .csv
with open(f"TABELA{n}x{n}.csv", "w", newline="", encoding="utf-8") as f:
    with redirect_stdout(f):
        gera_tabela()
        print("Gera Tabelas v1")
        print("Dev. by brunofeliped@icloud.com")
