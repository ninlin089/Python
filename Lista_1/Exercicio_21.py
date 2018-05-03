# Exerecicio 21 - faça um programa para rodar uma musica #

import pygame
from pygame import mixer
mixer.init()
mixer.music.load('Song_1.mp3')
mixer.music.play()
pygame.event.wait()