from PROJETO_FINAL.codigo.core.menus.menu_options import MenuOptions
from PROJETO_FINAL.codigo.core.menus.player_menu.player_menu import PlayerMenu

from PROJETO_FINAL.codigo.core.menus.player_menu.player_menu_options import OPTIONS as PLAYER_MENU_OPTIONS
from PROJETO_FINAL.codigo.core.menus.player_menu.player_menu_options import RETURN as PLAYER_RETURN


def show_database(main_menu):
    main_menu.parent.database.mostrar_tudo()


def login(main_menu):
    player = main_menu.parent.login(main_menu.gamertag, main_menu.password)
    player_menu_options = MenuOptions(option_function_mapping=PLAYER_MENU_OPTIONS, return_option=PLAYER_RETURN)
    if player is not None:
        player_menu = PlayerMenu(
            parent=main_menu, title='MENU DO JOGADOR',
            options=player_menu_options, player=player)
        player_menu.open()


def create_account(main_menu):
    main_menu.parent.create_player_account(main_menu.gamertag, main_menu.password)


def change_gamertag(main_menu):
    new_gamertag = input('Insira a sua nova gamertag: ')
    main_menu.parent.update_player_gamertag(main_menu.gamertag, main_menu.password, new_gamertag)


def change_password(main_menu):
    new_password = str(input('Insira a sua nova senha: '))
    main_menu.parent.update_player_password(main_menu.gamertag, main_menu.password, new_password)


def delete_account(main_menu):
    main_menu.parent.delete_player_account(main_menu.gamertag, main_menu.password)
