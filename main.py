# main.py
import pygame
import sys
from core.game import Game
from core.weapon import Weapon

def main():
    pygame.init()

    image_files = [
        "core/assets/sigrun/s1.png",
        "core/assets/sigrun/s2.png",
        "core/assets/sigrun/s3.png",
        "core/assets/sigrun/s4.png",
        "core/assets/sigrun/s5.png",
        "core/assets/sigrun/s6.png",
        "core/assets/sigrun/s7.png",
    ]

    image_gun = pygame.image.load("core/assets/weapons/weapon.png")
    image_bullet = pygame.image.load("core/assets/weapons/bullet.png")

    game = Game(image_files, image_gun, image_bullet)
    game.run()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

