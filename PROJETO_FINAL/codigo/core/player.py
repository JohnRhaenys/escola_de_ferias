class Player:
    MAX_NUMBER_OF_LOADOUTS = 10

    def __init__(self, gamertag, password, total_wins, favorite_loadout, loadouts):
        self.gamertag = gamertag
        self.password = password
        self.total_wins = total_wins
        self.favorite_loadout = favorite_loadout
        self.loadouts = loadouts

    def create_loadout(self, loadout):
        self.loadouts.append(loadout)

    def get_loadout(self, index):
        pass

    def update_loadout(self):
        pass

    def delete_loadout(self):
        pass

    def __str__(self):
        descricao_loadouts = '\n'
        temp = '-=' * 25
        for loadout in self.loadouts:
            descricao_loadouts += f'{temp}\n'
            descricao_loadouts += loadout.__str__()

        return """\nJogador: [{}]\nSenha: {}\nVitorias: {}\nLoadout favorito: {}\nLOADOUTS: {}""" \
            .format(self.gamertag, self.password, self.total_wins,
                    self.favorite_loadout, descricao_loadouts)
