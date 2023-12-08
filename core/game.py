import pygame
import sys
from core.player import Player
from core.weapon import Weapon
from core.enemy import Enemy

class Game:
    def __init__(self, player_images, weapon_image, bullet_image, enemy_images):
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sigrun Adventures")

        # Cargar las imágenes del jugador
        self.player = Player(self.width, self.height, player_images, weapon_image, bullet_image)  # Añade bullet_image como un parámetro
        self.weapon = Weapon(weapon_image, bullet_image)
        
        self.score = 0
        self.font = pygame.font.Font(None, 36)

        self.bullets = pygame.sprite.Group()

        self.enemies = pygame.sprite.Group()
        for i, enemy_type_images in enumerate(enemy_images):
            enemy = Enemy(100 * i, 100, enemy_type_images)
            self.enemies.add(enemy)



    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.player.handle_input(keys)

            self.player.movements()
            self.player.update(self.bullets)

            self.bullets.update()
            self.bullets.draw(self.screen)

            self.enemies.update()
            self.enemies.draw(self.screen)

            self.draw()

            pygame.display.flip()

    def draw(self):
        self.screen.fill((0, 0, 30))
        self.player.draw(self.screen, self.bullets)
        self.enemies.draw(self.screen)  # Agrega esta línea para dibujar a los enemigos
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        
    def game_over(self):
        print(f"Game Over. Score: {self.score}")
        pygame.quit()
        sys.exit()
