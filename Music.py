import pygame

def play_music(start_time):
    pygame.mixer.init()
    pygame.mixer.music.load("You_spin_me_round.mp3")
    pygame.mixer.music.play(start=start_time)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
play_music(60)
play_music('You_spin_me_round.mp3')
