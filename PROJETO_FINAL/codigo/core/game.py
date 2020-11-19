from PROJETO_FINAL.codigo.core.menus.main_menu.main_menu import MainMenu
from PROJETO_FINAL.codigo.core.menus.menu_options import MenuOptions
from PROJETO_FINAL.codigo.core.tratamento_de_erros import exception_messages
from PROJETO_FINAL.codigo.dados.database import Database
from PROJETO_FINAL.codigo.core.tratamento_de_erros.my_exception import MyException
from PROJETO_FINAL.codigo.core.menus.main_menu.main_menu_options import OPTIONS as MAIN_MENU_OPTIONS
from PROJETO_FINAL.codigo.core.menus.main_menu.main_menu_options import RETURN as MAIN_MENU_RETURN


class Game:

    def __init__(self):
        self.database = Database()
        self.online_players = []
        main_menu_options = MenuOptions(option_function_mapping=MAIN_MENU_OPTIONS, return_option=MAIN_MENU_RETURN)
        self.main_menu = MainMenu(parent=self, title='MAIN MENU', options=main_menu_options)

    def start(self):
        self.main_menu.open()

    def create_player_account(self, gamertag, password):
        """
        Dados os inputs do usuario, cria uma conta de jogador

        :param gamertag: nome escolhido pelo usuario
        :param password: senha escolhida pelo usuario
        """
        try:
            self.database.create(gamertag, password)
            print('Conta criada com sucesso!')
        except MyException as e:
            print(e)

    def login(self, gamertag, password):
        """
        Dados os inputs do usuario, faz login no jogo

        :param gamertag: nome do usuario
        :param password: senha do usuario
        """
        try:
            player = self.database.read(gamertag, password)
            print(f'Seja bem vindo, {player.gamertag}!')

            # Inserindo o jogador na lista de jogadores online
            self.online_players.append(player)
            return player
        except MyException as e:
            if str(e) == exception_messages.EMPTY_DATABASE:
                print('Jogador não cadastrado!')
            else:
                print(e)

    def update_player_password(self, gamertag, password, new_password):
        """
        Dados os inputs do usuario, realiza a troca da senha

        :param gamertag: nome do jogador
        :param password: senha do jogador
        :param new_password: nova senha escolhida pelo jogador
        """
        try:
            self.database.update_password(gamertag, password, new_password)
            print(f'Senha atualizada com sucesso!')
        except MyException as e:
            print(e)

    def update_player_gamertag(self, gamertag, password, new_gamertag):
        """
        Dados os inputs do usuario, altera a gamertag do jogador

        :param gamertag: nome do jogador
        :param password: senha do jogador
        :param new_gamertag: nova gamertag escolhida pelo jogador
        """
        try:
            self.database.update_gamertag(gamertag, password, new_gamertag)
            print(f'Gamertag atualizada com sucesso!')
        except MyException as e:
            print(e)

    def delete_player_account(self, gamertag, password):
        """
        Dados os inputs do usuario, remove a conta do jogador

        :param gamertag: nome do jogador
        :param password: senha do jogador
        """
        try:
            self.database.delete(gamertag, password)
            print(f'Conta removida com sucesso!')
        except MyException as e:
            print(e)
