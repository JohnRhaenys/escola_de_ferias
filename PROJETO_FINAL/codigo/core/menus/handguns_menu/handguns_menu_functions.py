from PROJETO_FINAL.codigo.core.loadout.armas.ammunition import Ammunition
from PROJETO_FINAL.codigo.core.loadout.armas.secundarias.pistol import Pistol
from PROJETO_FINAL.codigo.core.loadout.armas.secundarias.revolver import Revolver


def create_desert_eagle():
    desert_eagle_ammo = Ammunition(bullets=30, type='.50')
    return Pistol(name='DESERT EAGLE', accuracy=7, damage=10, reload_speed=7, ammunition=desert_eagle_ammo)


def create_revolver():
    revolver_ammo = Ammunition(bullets=30, type='.357')
    return Revolver(name='Revolver 357', accuracy=9, damage=8, reload_speed=3, ammunition=revolver_ammo)
