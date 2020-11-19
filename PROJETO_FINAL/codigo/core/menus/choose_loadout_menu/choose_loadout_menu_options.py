from PROJETO_FINAL.codigo.core.menus.assault_rifles_menu.assault_rifle_menu_functions \
    import create_ak, create_m4

AK47 = 'AK-47'
M4A1 = 'M4A1'
RETURN = 'RETORNAR PARA O MENU DE LOADOUTS'


OPTIONS = {
    AK47: create_ak,
    M4A1: create_m4,
    RETURN: None
}
