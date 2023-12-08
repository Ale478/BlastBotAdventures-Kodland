import pygame
import sys
from core.game import Game

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

    goblin_images = [
        "core/assets/enemies/goblin/goblin_1.png",
        "core/assets/enemies/goblin/goblin_2.png",
        "core/assets/enemies/goblin/goblin_3.png",
        "core/assets/enemies/goblin/goblin_4.png",
        "core/assets/enemies/goblin/goblin_5.png",
        "core/assets/enemies/goblin/goblin_6.png",
        "core/assets/enemies/goblin/goblin_7.png",
        "core/assets/enemies/goblin/goblin_8.png",
    ]

    
    hongo_images = [
        "core/assets/enemies/honguito/honguito_1.png",
        "core/assets/enemies/honguito/honguito_2.png",
        "core/assets/enemies/honguito/honguito_3.png",
        "core/assets/enemies/honguito/honguito_4.png",
    ]

    
    enemy_images = [goblin_images, hongo_images]

    image_gun = pygame.image.load("core/assets/weapons/weapon.png")
    image_bullet = pygame.image.load("core/assets/weapons/bullet.png")

    game = Game(image_files, image_gun, image_bullet, enemy_images)
    game.run()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

