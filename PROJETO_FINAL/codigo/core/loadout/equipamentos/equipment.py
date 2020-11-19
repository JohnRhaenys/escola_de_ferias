from pydub import AudioSegment
from pydub.playback import play


class Equipment:
    def __init__(self, name, design, description, area_of_effect):
        self.name = name

        # Desenho ("skin") do equipamento, criado pela equipe de direcao de arte do jogo
        self.design = design

        # String que diz o que o equipamento faz
        # Uma C4, por exemplo, explode.
        # Um molotov queima
        # Uma granada de fumaca gera fumaca ...
        self.description = description

        # Area de efeito do equipamento. Por exemplo, um explosivo tem uma area
        # de explosao. Uma granada de fumaca possui uma area de efeito da fumaca ...
        self.area_of_effect = area_of_effect

    def activate(self):
        """
        A ativacao do equipamento em si (o que ele faz ...)
        """
        pass

    def make_noise(self, audio_file_path):
        """
        Barulho do equipamento. Vou deixar sem implementar porque
        esta classe e' abstrata, ou seja, nao faz sentido eu ter um
        equipamento (e' uma ideia muito geral). Faz sentido eu criar
        uma granada de fragmentacao ou uma granada de fumaca, que sao
        tipos de equipamentos e objetos verdadeiros.
        """
        audio = AudioSegment.from_mp3(audio_file_path)
        play(audio)

    def __str__(self):
        return self.name
