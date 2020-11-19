from PROJETO_FINAL.codigo.core.menus.tactical_equipment_menu.tactical_equipment_menu_functions \
    import create_smoke_grenade, create_flash_grenade

SMOKE_GRENADE = 'GRANADA DE FUMAÇA'
FLASH_GRENADE = 'GRANADA DE FLASH'
RETURN = 'RETORNAR PARA O MENU DE LOADOUTS'

OPTIONS = {
    SMOKE_GRENADE: create_smoke_grenade,
    FLASH_GRENADE: create_flash_grenade,
    RETURN: None
}
