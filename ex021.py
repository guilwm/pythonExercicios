#Exercício 21 do curso em vídeo
import pygame
pygame.init()
pygame.mixer.music.load('petra.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass