import os, sys
import random
import pygame
from PIL import Image
from Doctor import Plague_Doctor
from Monster import Monster

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

#########



#Inicializando o Pygam e criando Janela
pygame.init()
display = pygame.display.set_mode((1360, 680))
pygame.display.set_caption("Caramount")


#objects
obejctGroup = pygame.sprite.Group()

monsterGroup = pygame.sprite.Group()



#background

bg = pygame.sprite.Sprite(obejctGroup)
bg.image = pygame.image.load("data/teste.gif")
bg.image = pygame.transform.scale(bg.image, [1360, 680])
bg.rect = bg.image.get_rect()

doctor = Plague_Doctor(obejctGroup)

#music
pygame.mixer.music.load("data/bg_music.wav")
pygame.mixer.music.play(-1)


gameloop = True
timer = 0

clock = pygame.time.Clock()
if __name__ == "__main__":
    while gameloop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False


        # Update Logic:
        obejctGroup.update()

        timer += 1
        if timer > 15:
            timer = 0
            if random.random() < 1:
                newMonster = monster = Monster(obejctGroup, monsterGroup)

        collisions = pygame.sprite.spritecollide(doctor, monsterGroup, False)

        if collisions:
            gameloop = False

        #draw
        display.fill([206, 161, 84])
        obejctGroup.draw(display)

        pygame.display.update()
