from PROJETO_FINAL.codigo.core.menus.loadout_menu.loadout_menu import LoadoutMenu
from PROJETO_FINAL.codigo.core.menus.match_menu.match_menu import MatchMenu
from PROJETO_FINAL.codigo.core.menus.choose_loadout_menu.choose_loadout_menu import ChooseLoadoutMenu

from PROJETO_FINAL.codigo.core.menus.match_menu.match_menu_options import OPTIONS as MATCH_MENU_OPTIONS
from PROJETO_FINAL.codigo.core.menus.match_menu.match_menu_options import RETURN as MATCH_RETURN

from PROJETO_FINAL.codigo.core.menus.choose_loadout_menu.choose_loadout_menu_options \
    import OPTIONS as CHOOSE_LOADOUT_MENU_OPTIONS
from PROJETO_FINAL.codigo.core.menus.choose_loadout_menu.choose_loadout_menu_options \
    import RETURN as CHOOSE_LOADOUT_RETURN

from PROJETO_FINAL.codigo.core.menus.loadout_menu.loadout_menu_options \
    import OPTIONS as LOADOUT_MENU_OPTIONS
from PROJETO_FINAL.codigo.core.menus.loadout_menu.loadout_menu_options \
    import RETURN as LOADOUT_RETURN

from PROJETO_FINAL.codigo.core.menus.menu_options import MenuOptions


def show_database(player_menu):
    player_menu.parent.parent.database.mostrar_tudo()


def create_loadout(player_menu):
    loadout_menu_options = MenuOptions(
        option_function_mapping=LOADOUT_MENU_OPTIONS, return_option=LOADOUT_RETURN)
    loadout_menu = LoadoutMenu(
        parent=player_menu, title='CRIE SEU LOADOUT', options=loadout_menu_options)
    loadout = loadout_menu.open()
    if loadout is not None:
        player_menu.player.loadouts.append(loadout)
        player_menu.parent.parent.database.salvar_dados()


def view_favorite_loadout(player_menu):
    print(player_menu.player.favorite_loadout)


def play(player_menu):
    if player_menu.player.favorite_loadout is None:
        if not player_menu.player.loadouts:
            print('Crie um loadout primeiro!')
        else:
            choose_loadout_menu_options = MenuOptions(
                option_function_mapping=CHOOSE_LOADOUT_MENU_OPTIONS, return_option=CHOOSE_LOADOUT_RETURN)
            choose_loadout_menu = ChooseLoadoutMenu(
                parent=player_menu, title='ESCOLHA O SEU LOADOUT',
                options=choose_loadout_menu_options, player=player_menu.player)
            player_menu.player.favorite_loadout = choose_loadout_menu.open()
            if player_menu.player.favorite_loadout is not None:
                player_menu.parent.parent.database.salvar_dados()
    else:
        match_menu_options = MenuOptions(
            option_function_mapping=MATCH_MENU_OPTIONS, return_option=MATCH_RETURN)
        match_menu = MatchMenu(
            parent=player_menu.player, title='O QUE DESEJA FAZER?', options=match_menu_options)
        match_menu.open()
