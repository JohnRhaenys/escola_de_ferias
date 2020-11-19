from PROJETO_FINAL.codigo.core.menus.handguns_menu.handguns_menu_functions \
    import create_desert_eagle, create_revolver

DESERT_EAGLE = 'DESERT EAGLE'
REVOLVER = 'REVOLVER'
RETURN = 'RETORNAR PARA O MENU DE LOADOUTS'


OPTIONS = {
    DESERT_EAGLE: create_desert_eagle,
    REVOLVER: create_revolver,
    RETURN: None
}
