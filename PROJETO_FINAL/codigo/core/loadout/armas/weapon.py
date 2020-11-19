from pydub import AudioSegment
from pydub.playback import play


class Weapon:
    def __init__(
            self, name,  accuracy, damage, reload_speed,
            ammunition, muzzle, barrel, laser, optic, sound_file_path):

        # Atributos essenciais
        self.name = name
        self.accuracy = accuracy
        self.damage = damage
        self.reload_speed = reload_speed
        self.ammunition = ammunition

        # Acessorios opcionais
        self.muzzle = muzzle
        self.barrel = barrel
        self.laser = laser
        self.optic = optic

        self.sound_file_path = sound_file_path

    def fire(self):
        pass

    def reload(self):
        pass

    def make_noise(self):
        audio = AudioSegment.from_mp3(self.sound_file_path)
        play(audio)

    def __str__(self):
        return self.name
