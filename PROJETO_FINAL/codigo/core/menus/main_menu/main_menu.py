from PROJETO_FINAL.codigo.core.menus.main_menu.main_menu_options import SHOW_DATABASE
from PROJETO_FINAL.codigo.core.menus.menu import Menu


class MainMenu(Menu):

    def __init__(self, parent, title, options):
        super().__init__(parent=parent, title=title, options=options)
        self.gamertag = None
        self.password = None

    def open(self):
        while True:
            self.display()
            choice = self.get_user_choice()
            if choice is not None:
                if choice == self.return_option:
                    exit()
                elif choice != SHOW_DATABASE:
                    self.gamertag = input('Insira a sua gamertag: ')
                    self.password = str(input('Insira a sua senha: '))
                self.options[choice](self)

            print()
            _ = input('Aperte ENTER para escolher outra opção')
            print()
