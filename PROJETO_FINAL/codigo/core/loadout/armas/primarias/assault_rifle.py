from PROJETO_FINAL.codigo.core.loadout.armas.weapon import Weapon


# Estou herdando todas as caracteristicas (atributos e metodos) da classe pai, Weapon
# Estou dizendo que a Assault Rifle é um subtipo de Arma.
# Visualize o diagrama de classe para entender melhor!
class AssaultRifle(Weapon):

    """
    Obs: Quando tenho uma linha muito grande de parametros, o Python
    recomenda usar o estilo do PEP8 (https://www.python.org/dev/peps/pep-0008/)
    Sao boas praticas de como fazer um codigo bonito!
    """
    def __init__(
            self, name, accuracy, damage, reload_speed, ammunition, muzzle='Default', barrel='Default',
            laser=False,  optic=None, stock='Default', underbarrel='Default', sound_file_path=None):

        # Chamando o construtor da classe pai (Weapon)
        super().__init__(
            name=name, accuracy=accuracy, damage=damage,
            reload_speed=reload_speed, ammunition=ammunition,
            muzzle=muzzle, barrel=barrel, laser=laser, optic=optic, sound_file_path=sound_file_path)

        # Inicializando atributos especificos da classe Assault Rifle
        # A classe pai, Weapon, não sabe desses atributos!
        self.stock = stock
        self.underbarrel = underbarrel

    def fire(self):
        """
        Nao esqueci de implementar. Eu nao vou implementar esses metodos porque
        eles sao da classe AssaultRifle, que nao e' um objeto do mundo real.
        'Assault Rifle'  e' uma ideia de uma coisa. Para cada arma verdadeira (AK47, M4A1)
        sera' criada uma classe que, ai' sim, sera' instanciada e ira' implementar os metodos
        fire( ) e reload( )
        :return:
        """
        pass

    def reload(self):
        pass
