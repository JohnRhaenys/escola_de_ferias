from PROJETO_FINAL.codigo.core.menus.match_menu.match_menu_functions import shoot_primary_weapon, shoot_secondary_weapon, \
    use_tactical_equipment, use_lethal_equipment, activate_night_vision_goggles

SHOOT_PRIMARY_WEAPON = 'ATIRAR COM A SUA ARMA PRIMÁRIA'
SHOOT_SECONDARY_WEAPON = 'ATIRAR COM A SUA ARMA SECUNDÁRIA'
USE_LETHAL_EQUIPMENT = 'USAR EQUIPAMENTO LETAL'
USE_TACTICAL_EQUIPMENT = 'USAR EQUIPAMENTO TÁTICO'
ACTIVATE_NIGHT_VISION_GOGGLES = 'ATIVAR ÓCULOS DE VISÃO NOTURNA'
RETURN = 'SAIR DA PARTIDA E RETORNAR AO MENU DO JOGADOR'


OPTIONS = {
    SHOOT_PRIMARY_WEAPON: shoot_primary_weapon,
    SHOOT_SECONDARY_WEAPON: shoot_secondary_weapon,
    USE_LETHAL_EQUIPMENT: use_lethal_equipment,
    USE_TACTICAL_EQUIPMENT: use_tactical_equipment,
    ACTIVATE_NIGHT_VISION_GOGGLES: activate_night_vision_goggles,
    RETURN: None
}