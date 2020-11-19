from time import sleep
from PROJETO_FINAL.codigo.core.loadout.equipamentos import Explosive


class FragGrenade(Explosive):
    def __init__(self, name, design, description, area_of_effect, damage):
        super().__init__(name, design, description, area_of_effect, damage)

    # Polimorfismo de sobreposicao. Estou fazendo a acao do equipamento especifico
    def activate(self):

        print('Cozinhando granada ...')

        # A granada possui um tempo antes de explodir (vamos considerar 3 segundos)
        for i in range(3):
            sleep(i)

        print('Animação de explosão ...')
        self.make_noise()

    # Polimorfismo de sobreposicao. Estou fazendo o barulho do equipamento especifico
    def make_noise(self):
        print('Fazendo barulho de explosão de granada ...')
