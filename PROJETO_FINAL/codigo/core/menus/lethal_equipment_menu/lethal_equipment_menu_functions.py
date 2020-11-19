from PROJETO_FINAL.codigo.core.loadout.equipamentos import C4
from PROJETO_FINAL.codigo.core.loadout.equipamentos.letais.explosivos.frag_grenade import FragGrenade


def create_frag_grenade():
    return FragGrenade(
        name='GRANADA DE FRAGMENTAÇÃO', design=None,
        description='Explode gerando estilhaços em volta',
        area_of_effect=5, damage=7)


def create_c4():
    return C4(
        name='EXPLOSIVO C4', design=None,
        description='Gera uma forte explosão, podendo abrir portas e explodir paredes',
        area_of_effect=4, damage=10)
