from PROJETO_FINAL.codigo.core.menus.lethal_equipment_menu.lethal_equipment_menu_functions \
    import create_c4, create_frag_grenade

FRAG_GRENADE = 'GRANADA DE FRAGMENTAÇÃO'
C4 = 'C4'
RETURN = 'RETORNAR PARA O MENU DE LOADOUTS'

OPTIONS = {
    FRAG_GRENADE: create_frag_grenade,
    C4: create_c4,
    RETURN: None
}
