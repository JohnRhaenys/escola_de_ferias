from PROJETO_FINAL.codigo.core.menus.main_menu.main_menu_functions \
    import show_database, login, create_account, \
    change_gamertag, change_password, delete_account

SHOW_DATABASE = 'MOSTRAR BANCO DE DADOS'
LOGIN = 'FAZER LOGIN'
CREATE_ACCOUNT = 'CRIAR CONTA'
CHANGE_GAMERTAG = 'MUDAR GAMERTAG'
CHANGE_PASSWORD = 'MUDAR SENHA'
DELETE_ACCOUNT = 'DELETAR CONTA'
RETURN = 'FECHAR JOGO'


OPTIONS = {
    SHOW_DATABASE: show_database,
    LOGIN: login,
    CREATE_ACCOUNT: create_account,
    CHANGE_GAMERTAG: change_gamertag,
    CHANGE_PASSWORD: change_password,
    DELETE_ACCOUNT: delete_account,
    RETURN: None
}
