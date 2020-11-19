from PROJETO_FINAL.codigo.core.loadout.loadout import Loadout
from PROJETO_FINAL.codigo.core.menus.loadout_menu.loadout_menu_options import CONFIRM
from PROJETO_FINAL.codigo.core.menus.menu import Menu


class LoadoutMenu(Menu):

    def __init__(self, parent, title, options):
        super().__init__(parent=parent, title=title, options=options)
        self.current_loadout = Loadout()

    def open(self):
        while True:
            self.display()
            choice = self.get_user_choice()
            if choice is not None:
                print('CHOICE LOADOUT MENU: ', choice)
                if choice == self.return_option:
                    return None
                elif choice == CONFIRM:
                    return self.options[choice](self)
                else:
                    self.options[choice](self)

            print()
            input('Aperte ENTER para escolher outra opção')
            print()
