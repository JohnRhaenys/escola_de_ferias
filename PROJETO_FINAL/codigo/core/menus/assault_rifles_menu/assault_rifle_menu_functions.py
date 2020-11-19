from PROJETO_FINAL.codigo.assets.audio.audio_paths import AK_SOUND_PATH, M4_SOUND_PATH
from PROJETO_FINAL.codigo.core.loadout.armas.ammunition import Ammunition
from PROJETO_FINAL.codigo.core.loadout.armas.primarias.assault_rifle import AssaultRifle


def create_ak():
    ak47_ammo = Ammunition(bullets=90, type='7.62')
    return AssaultRifle(
        name='AK47', accuracy=7, damage=9,
        reload_speed=7, ammunition=ak47_ammo, sound_file_path=AK_SOUND_PATH)


def create_m4():
    m4a1_ammo = Ammunition(bullets=90, type='5.56')
    return AssaultRifle(
        name='M4A1', accuracy=9, damage=8,
        reload_speed=7, ammunition=m4a1_ammo, sound_file_path=M4_SOUND_PATH)
