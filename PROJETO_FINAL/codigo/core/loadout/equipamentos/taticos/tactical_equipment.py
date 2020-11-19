from PROJETO_FINAL.codigo.core.loadout.equipamentos import Equipment


# Um equipamento tatico e' um tipo de equipamento.
# Logo, TaticalEquipment 'extends' Equipment
class TacticalEquipment(Equipment):
    def __init__(self, name, design, description, area_of_effect):

        # Chamando o construtor do pai
        super().__init__(name=name, design=design, description=description, area_of_effect=area_of_effect)
