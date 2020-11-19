from PROJETO_FINAL.codigo.core.menus.player_menu.player_menu_functions \
    import show_database, create_loadout, view_favorite_loadout, play

SHOW_DATABASE = 'MOSTRAR BANCO DE DADOS'
CREATE_LOADOUT = 'CRIAR LOADOUT'
VIEW_FAVORITE_LOADOUT = 'VISUALIZAR LOADOUT FAVORITO'
PLAY = 'JOGAR'
RETURN = 'LOGOUT'

OPTIONS = {
    SHOW_DATABASE: show_database,
    CREATE_LOADOUT: create_loadout,
    VIEW_FAVORITE_LOADOUT: view_favorite_loadout,
    PLAY: play,
    RETURN: None
}
