def shoot_primary_weapon(match_menu):
    match_menu.parent.favorite_loadout.primary_weapon.fire()


def shoot_secondary_weapon(match_menu):
    match_menu.parent.favorite_loadout.secondary_weapon.fire()


def use_lethal_equipment(match_menu):
    match_menu.parent.favorite_loadout.lethal_equipment.activate()


def use_tactical_equipment(match_menu):
    match_menu.parent.favorite_loadout.tactical_equipment.activate()


def activate_night_vision_goggles(match_menu):
    if match_menu.parent.favorite_loadout.night_vision_goggles is None:
        print('Você não tem óculos de visão noturna!')
    else:
        match_menu.parent.favorite_loadout.night_vision_goggles.activate()
