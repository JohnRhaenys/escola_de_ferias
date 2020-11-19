from PROJETO_FINAL.codigo.core.menus.menu import Menu


class PlayerMenu(Menu):

    def __init__(self, parent, title, options, player):
        super().__init__(parent=parent, title=title, options=options)
        self.player = player

    def open(self):
        while True:
            self.display()
            choice = self.get_user_choice()
            if choice is not None:
                if choice == self.return_option:
                    print(f'Até mais, {self.player.gamertag}!')
                    break
                self.options[choice](self)
