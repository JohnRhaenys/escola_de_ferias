from PROJETO_FINAL.codigo.core.loadout.equipamentos import LethalEquipment


# Um explosivo e' um tipo de equipamento letal
class Explosive(LethalEquipment):
    def __init__(self, name, design, description, area_of_effect, damage):
        super().__init__(
            name=name, design=design, description=description,
            area_of_effect=area_of_effect, damage=damage)

    def explode(self):
        print('Animação de explosão')
        self.make_noise()

    def make_noise(self):
        print('Barulho de explosão')
