from PROJETO_FINAL.codigo.core.menus.menu import Menu


class ChooseLoadoutMenu(Menu):

    def __init__(self, parent, title, options, player):
        super().__init__(parent=parent, title=title, options=options)

        # Referencia para o jogador
        self.player = player

        self.options = [i for i in range(len(self.player.loadouts))]

    def display(self):
        print()
        print(f'{"-=" * 10} ESCOLHA O SEU LOADOUT {"-=" * 10}')
        for option in self.options:
            print(f'LOADOUT {option}')
        print(f'{"-=" * 10} ESCOLHA O SEU LOADOUT {"-=" * 10}')
        print()

    def open(self):

        while True:
            # Mostra o menu
            self.display()

            # Pega a escolha do usuario
            choice = self.get_user_choice()

            if choice is not None:
                try:
                    loadout = self.player.loadouts[choice]
                    return loadout
                except IndexError:
                    print('Loadout inexistente.')
                    return None

            print()
            _ = input('Aperte ENTER para escolher outra opção')
            print()
