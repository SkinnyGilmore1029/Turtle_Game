import pygame
pygame.mixer.init

class MusicManager:
    def __init__(self):
        pygame.mixer.init()
        self.current_track = None

    def play_music(self, track_path: str, loops=-1, volume=0.5):
        if self.current_track != track_path:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(track_path)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(loops=loops)
            self.current_track = track_path

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_track = None

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def set_volume(self, volume: float):
        pygame.mixer.music.set_volume(volume)


music = MusicManager()