import pygame
import sys
from core.player import Player
from core.weapon import Weapon
from core.enemy import Enemy

class Game:
    def __init__(self, player_images, weapon_image, bullet_image, enemy_images, num_enemies):
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

        enemy_positions = [
            (400, 150),
            (550, 300),
            (600, 450),
            (350, 200)
        ]

        for i in range(num_enemies):
            position = enemy_positions[i % len(enemy_positions)]
            enemy = Enemy(position[0], position[1], enemy_images[i % len(enemy_images)])
            self.enemies.add(enemy)
        
        self.num_enemies = num_enemies
        self.enemy_count = num_enemies

    
        
    
    def check_collisions(self):
        hits = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)
        for enemy, bullets in hits.items():
            self.score += len(bullets)

        self.bullets = pygame.sprite.Group([bullet for bullet in self.bullets if 0 < bullet.rect.x < self.width])

        self.enemies = pygame.sprite.Group([enemy for enemy in self.enemies if 0 < enemy.rect.x < self.width])

        player_hit = pygame.sprite.spritecollide(self.player, self.enemies, False)
        if player_hit:
            self.enemy_count -= 1
            if self.enemy_count == 0:
                self.game_over()


    def run(self):
        running = True

        while running and self.enemy_count > 0:
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

            self.check_collisions()

            self.draw()

            pygame.display.flip()

    def draw(self):
        self.screen.fill((0, 0, 30))
        self.player.draw(self.screen, self.bullets)
        self.enemies.draw(self.screen)  # Agrega esta línea para dibujar a los enemigos
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        enemy_count_text = self.font.render(f"Enemies: {self.enemy_count}", True, (255, 255, 255))
        self.screen.blit(enemy_count_text, (10, 40))

        
    def game_over(self):
        self.running = False 
        #pygame.quit()
        #sys.exit()
