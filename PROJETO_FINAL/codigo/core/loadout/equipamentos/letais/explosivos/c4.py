from PROJETO_FINAL.codigo.core.loadout.equipamentos import Explosive


class C4(Explosive):
    def __init__(self, name, design, description, area_of_effect, damage):
        super().__init__(name, design, description, area_of_effect, damage)

    # Polimorfismo de sobreposicao. Estou fazendo a acao do equipamento especifico
    def activate(self):

        print('Animação de explosão ...')
        self.make_noise()

    # Polimorfismo de sobreposicao. Estou fazendo o barulho do equipamento especifico
    def make_noise(self):
        print('Fazendo barulho de explosão de C4 ...')
