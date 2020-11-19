from pydub import AudioSegment
from pydub.playback import play


class Optic:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_sound(self, audio_file_path):
        audio = AudioSegment.from_mp3(audio_file_path)
        play(audio)

    def __str__(self):
        return self.name
