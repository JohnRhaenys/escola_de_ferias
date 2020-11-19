import os
from pydub import AudioSegment
from pydub.playback import play

from PROJETO_FINAL.codigo.core.menus.menu import Menu


class MatchMenu(Menu):

    def __init__(self, parent, title, options):
        super().__init__(parent=parent, title=title, options=options)

    def open(self):

        print('Carregando partida ...')
        audio = AudioSegment.from_mp3(os.path.join(os.getcwd(), 'menus', '../match_begins.mp3'))
        play(audio)

        while True:
            self.display()
            choice = self.get_user_choice()

            if choice is not None:
                if choice == self.return_option:
                    return
                self.options[choice](self)

            print()
            _ = input('Aperte ENTER para escolher outra opção')
            print()
