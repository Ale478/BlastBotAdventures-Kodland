import pygame
import sys
from core.player import Player

class Game:
    def __init__(self, player_image):
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("BlastBot Adventures")

        # Cargar la imagen del jugador
        self.player = Player(self.width, self.height, player_image)
        
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.player.handle_input(keys)

            self.player.movements()
            self.player.update()

            self.draw()

            pygame.display.flip()

    def draw(self):
        self.screen.fill((0, 0, 30))
        self.player.draw(self.screen)

        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def game_over(self):
        print(f"Game Over. Score: {self.score}")
        pygame.quit()
        sys.exit()
