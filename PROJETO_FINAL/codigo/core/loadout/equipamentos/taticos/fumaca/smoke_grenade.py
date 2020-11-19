from PROJETO_FINAL.codigo.core.loadout.equipamentos.taticos.tactical_equipment import TacticalEquipment


class SmokeGrenade(TacticalEquipment):
    def __init__(self, name, design, description, area_of_effect):
        super().__init__(name, design, description, area_of_effect)

    # Polimorfismo de sobreposicao. Estou fazendo a acao do equipamento especifico
    def activate(self):
        print('Gerando fumaça ...')
        self.make_noise('')

    # Polimorfismo de sobreposicao. Estou fazendo o barulho do equipamento especifico
    def make_noise(self, audio_file_path):
        print('Fazendo barulho de fumaça ...')
