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

    game = Game(image_files)
    game.run()

    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    main()

