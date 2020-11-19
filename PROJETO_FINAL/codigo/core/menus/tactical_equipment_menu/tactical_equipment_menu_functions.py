from PROJETO_FINAL.codigo.core.loadout.equipamentos.taticos.flash import FlashGrenade
from PROJETO_FINAL.codigo.core.loadout.equipamentos.taticos import SmokeGrenade


def create_smoke_grenade():
    return SmokeGrenade(
        name='GRANADA DE FUMAÇA', design=None,
        description='Quando usada, gera uma cortina de fumaça branca',
        area_of_effect=8)


def create_flash_grenade():
    return FlashGrenade(
        name='GRANADA DE FLASH', design=None,
        description='Quando usada, gera uma forte explosão de luz, deixando'
                    'os inimigos cegos por alguns instantes',
        area_of_effect=5)
