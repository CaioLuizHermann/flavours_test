import pygame

class Music:
    def __init__(self, script_dir, volume=0.5):
        self.dir = script_dir / "assets"
        self.current = None
        pygame.mixer.music.set_volume(volume)

    def play(self, name, loops=-1, fade_ms=500):
        if name == self.current:
            return
        self.current = name
        pygame.mixer.music.load(str(self.dir / f"{name}.mp3"))
        pygame.mixer.music.play(loops, fade_ms=fade_ms)