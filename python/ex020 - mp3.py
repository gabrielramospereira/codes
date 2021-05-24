import pygame
pygame.init()
pygame.mixer.music.load("nomedoarquivo.mp3")   #coloqueoarquivo mp3 aqui também
pygame.mixer.music.play()
pygame.event.wait()
