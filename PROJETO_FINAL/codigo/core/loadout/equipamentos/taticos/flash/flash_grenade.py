import os

from PROJETO_FINAL.codigo.core.loadout.equipamentos.taticos.tactical_equipment import TacticalEquipment


class FlashGrenade(TacticalEquipment):

    AUDIO_FILE_PATH = os.path.join(os.getcwd(), 'loadout', 'equipamentos', 'taticos', 'flash', 'flash.mp3')

    def __init__(self, name, design, description, area_of_effect):
        super().__init__(name, design, description, area_of_effect)

    # Polimorfismo de sobreposicao. Estou fazendo a acao do equipamento especifico
    def activate(self):
        self.make_noise(self.AUDIO_FILE_PATH)
        print('Cegando o inimigo ...')
