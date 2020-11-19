from PROJETO_FINAL.codigo.core.loadout.oticos.visao_noturna.night_vision import NightVision
from PROJETO_FINAL.codigo.core.menus.menu import Menu

from PROJETO_FINAL.codigo.core.menus.assault_rifles_menu.assault_rifle_menu_options \
    import OPTIONS as ASSAULT_RIFLE_MENU_OPTIONS

from PROJETO_FINAL.codigo.core.menus.assault_rifles_menu.assault_rifle_menu_options \
    import RETURN as AR_RETURN

from PROJETO_FINAL.codigo.core.menus.handguns_menu.handgun_menu_options \
    import OPTIONS as HANDGUN_MENU_OPTIONS

from PROJETO_FINAL.codigo.core.menus.handguns_menu.handgun_menu_options \
    import RETURN as HANDGUN_RETURN

from PROJETO_FINAL.codigo.core.menus.lethal_equipment_menu.lethal_equipment_menu_options \
    import OPTIONS as LETHAL_EQUIPMENT_MENU_OPTIONS

from PROJETO_FINAL.codigo.core.menus.lethal_equipment_menu.lethal_equipment_menu_options \
    import RETURN as LETHAL_RETURN

from PROJETO_FINAL.codigo.core.menus.menu_options import MenuOptions

from PROJETO_FINAL.codigo.core.menus.tactical_equipment_menu.tactical_equipment_menu_options \
    import OPTIONS as TACTICAL_EQUIPMENT_MENU_OPTIONS

from PROJETO_FINAL.codigo.core.menus.tactical_equipment_menu.tactical_equipment_menu_options \
    import RETURN as TACTICAL_RETURN


def visualize_loadout(loadout_menu):
    print(loadout_menu.current_loadout)


def choose_primary_weapon(loadout_menu):
    ar_menu_options = MenuOptions(option_function_mapping=ASSAULT_RIFLE_MENU_OPTIONS, return_option=AR_RETURN)
    assault_rifles_menu = Menu(
        parent=loadout_menu, title='ESCOLHA A SUA ASSAULT RIFLE', options=ar_menu_options)
    primary_weapon = assault_rifles_menu.open()
    loadout_menu.current_loadout.primary_weapon = primary_weapon


def choose_secondary_weapon(loadout_menu):
    handgun_menu_options = MenuOptions(
        option_function_mapping=HANDGUN_MENU_OPTIONS, return_option=HANDGUN_RETURN)
    handguns_menu = Menu(
        parent=loadout_menu, title='ESCOLHA A SUA ARMA SECUNDÁRIA', options=handgun_menu_options)
    secondary_weapon = handguns_menu.open()
    loadout_menu.current_loadout.secondary_weapon = secondary_weapon


def choose_lethal_equipment(loadout_menu):
    lethal_menu_options = MenuOptions(
        option_function_mapping=LETHAL_EQUIPMENT_MENU_OPTIONS, return_option=LETHAL_RETURN)
    lethal_equipment_menu = Menu(
        parent=loadout_menu,
        title='ESCOLHA O SEU EQUIPAMENTO LETAL', options=lethal_menu_options)
    lethal_equipment = lethal_equipment_menu.open()
    loadout_menu.current_loadout.lethal_equipment = lethal_equipment


def choose_tactical_equipment(loadout_menu):
    tactical_menu_options = MenuOptions(
        option_function_mapping=TACTICAL_EQUIPMENT_MENU_OPTIONS, return_option=TACTICAL_RETURN)
    tactical_equipment_menu = Menu(
        parent=loadout_menu,
        title='ESCOLHA O SEU EQUIPAMENTO TÁTICO', options=tactical_menu_options)
    tactical_equipment = tactical_equipment_menu.open()
    loadout_menu.current_loadout.tactical_equipment = tactical_equipment


def choose_night_vision_goggles(loadout_menu):
    loadout_menu.current_loadout.night_vision_goggles = NightVision(
        name='Óculos de Visão Noturna',
        color='Preto')


def confirm(loadout_menu):
    return loadout_menu.current_loadout