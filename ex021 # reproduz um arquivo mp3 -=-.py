# reproduz um arquivo mp3 -=-

'''import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('CURTE O SOM PIVETE!')'''


'''from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('CURTE O SOM PIVETE!')'''


'''import pygame
# Inicializando o mixer PyGame
pygame.mixer.init()
# Iniciando o Pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
input('CURTE O SOM PIVETE!')'''


import playsound as playsound
playsound.playsound('ex021 # musica para usar no 21 .mp3')