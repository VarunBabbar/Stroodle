import pygame
import time
pygame.init()
pygame.mixer.init()
sounda= pygame.mixer.Sound("European_Dragon_Roaring_and_breathe_fire-daniel-simon_wav.wav")
wonka= pygame.mixer.Sound("SCOTT_JOPLIN_The_Entertainer_wav.wav")
pygame.mixer.Channel(1).play(wonka)
time.sleep(3)
pygame.mixer.Channel(0).play(sounda)
for i in range(10000000000):
    print (i)


