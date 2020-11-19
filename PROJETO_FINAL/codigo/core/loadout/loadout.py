class Loadout:

    # O loadout comeca sem nenhuma arma ou equipamento
    def __init__(
            self, primary_weapon=None, secondary_weapon=None,
            lethal_equipment=None, tactical_equipment=None,
            night_vision_goggles=None):
        self.primary_weapon = primary_weapon
        self.secondary_weapon = secondary_weapon
        self.lethal_equipment = lethal_equipment
        self.tactical_equipment = tactical_equipment
        self.night_vision_goggles = night_vision_goggles

    def __str__(self):
        return """\nARMA PRIMÁRIA: {}\nARMA SECUNDÁRIA: {}\nEQUIP. LETAL: {}\nEQUIP. TÁTICO: {}\nÓCULOS DE VISÃO NOTURNA: {}\n""" \
            .format(
                self.primary_weapon, self.secondary_weapon,
                self.lethal_equipment, self.tactical_equipment, self.night_vision_goggles)
