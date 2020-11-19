from PROJETO_FINAL.codigo.core.loadout.oticos.optic import Optic


class SniperScope(Optic):

    def __init__(self, name, color, zoom):
        super().__init__(name, color)

        self.zoom = zoom

    def zoom_in(self):
        print('Enxergando mais longe')

    def zoom_out(self):
        print('Enxergando menos longe')
