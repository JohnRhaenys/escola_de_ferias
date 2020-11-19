import os

from PROJETO_FINAL.codigo.core.loadout.oticos.optic import Optic


class NightVision(Optic):

    AUDIO_FILE_PATH = os.path.join(os.getcwd(), 'loadout', 'oticos', 'visao_noturna', 'night.mp3')

    def __init__(self, name, color):
        super().__init__(name, color)

    def activate(self):
        self.make_sound(self.AUDIO_FILE_PATH)
        print('Enxergando no escuro')

    def deactivate(self):
        self.make_sound(self.AUDIO_FILE_PATH)
        print('Não enxergo mais no escuro')
