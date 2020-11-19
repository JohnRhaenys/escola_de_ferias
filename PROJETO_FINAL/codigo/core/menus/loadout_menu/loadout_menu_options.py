from PROJETO_FINAL.codigo.core.menus.loadout_menu.loadout_menu_functions \
    import visualize_loadout, choose_primary_weapon, \
    choose_secondary_weapon, choose_lethal_equipment, \
    choose_tactical_equipment, choose_night_vision_goggles, confirm

VISUALIZE_LOADOUT = 'VISUALIZAR LOADOUT'
CHOOSE_PRIMARY_WEAPON = 'ESCOLHA SUA ARMA PRIMÁRIA'
CHOOSE_SECONDARY_WEAPON = 'ESCOLHA SUA ARMA SECUNDARIA'
CHOOSE_LETHAL_EQUIPMENT = 'ESCOLHA UM EQUIPAMENTO LETAL'
CHOOSE_TACTICAL_EQUIPMENT = 'ESCOLHA UM EQUIPAMENTO TÁTICO'
CHOOSE_NIGHT_VISION_GOGGLES = 'QUERO USAR ÓCULOS DE VISÃO NOTURNA'
CONFIRM = 'CONFIRMAR'
RETURN = 'RETORNAR AO MENU DO JOGADOR'

OPTIONS = {
    VISUALIZE_LOADOUT: visualize_loadout,
    CHOOSE_PRIMARY_WEAPON: choose_primary_weapon,
    CHOOSE_SECONDARY_WEAPON: choose_secondary_weapon,
    CHOOSE_LETHAL_EQUIPMENT: choose_lethal_equipment,
    CHOOSE_TACTICAL_EQUIPMENT: choose_tactical_equipment,
    CHOOSE_NIGHT_VISION_GOGGLES: choose_night_vision_goggles,
    CONFIRM: confirm,
    RETURN: None
}
