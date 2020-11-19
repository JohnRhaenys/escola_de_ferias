from PROJETO_FINAL.codigo.core.loadout.armas.weapon import Weapon


class Handgun(Weapon):
    def __init__(
            self, name, accuracy, damage, reload_speed,
            ammunition, muzzle, barrel, laser, optic, dual, sound_file_path):

        # Chamando o construtor do pai
        super().__init__(
            name=name, accuracy=accuracy, damage=damage,
            reload_speed=reload_speed, ammunition=ammunition,
            muzzle=muzzle, barrel=barrel, laser=laser, optic=optic, sound_file_path=sound_file_path)

        self.dual = dual
