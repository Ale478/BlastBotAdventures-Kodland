import pygame
from core.player import Player
from core.weapon import Weapon
from core.enemy import Enemy
import sys


class Game:
    def __init__(
        self, player_images, weapon_image, bullet_image, enemy_images, num_enemies
    ):
        """
        Inicializa un objeto de juego.

        Args:
            player_images (list): Lista de rutas de imágenes para la animación del jugador.
            weapon_image (pygame.Surface): Imagen del arma del jugador.
            bullet_image (pygame.Surface): Imagen de la bala del arma del jugador.
            enemy_images (list): Lista de listas de rutas de imágenes para las animaciones de los enemigos.
            num_enemies (int): Número de enemigos en el juego.
        """
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sigrun Adventures")

        self.game_over = False

        self.player = Player(
            self.width, self.height, player_images, weapon_image, bullet_image
        )
        self.weapon = Weapon(weapon_image, bullet_image)

        self.score = 0
        self.font = pygame.font.Font(None, 36)

        self.bullets = pygame.sprite.Group()

        self.enemies = pygame.sprite.Group()

        enemy_positions = [(400, 150), (550, 300), (600, 450), (350, 200)]

        for i in range(num_enemies):
            position = enemy_positions[i % len(enemy_positions)]
            enemy = Enemy(position[0], position[1], enemy_images[i % len(enemy_images)])
            self.enemies.add(enemy)

        self.num_enemies = num_enemies
        self.enemy_count = num_enemies

        self.victory_message = "Congratulations! You defeated all enemies!"
        self.defeat_message = "Game Over - You Lost!"

    def game_over_method(self, victory=False):
        """
        Marca el juego como terminado.

        Args:
            victory (bool): Indica si el juego terminó por victoria o derrota.
        """
        self.game_over = True
        print("Game Over - You Lost!")

        self.draw_game_over("You Lost!")

    def check_victory(self):
        """
        Verifica si el jugador ha ganado (eliminó a todos los enemigos).
        """
        if self.enemy_count == 0:
            self.game_over = True
            print("Congratulations! You Won!")

            self.draw_game_over("You Won!")

    def check_collisions(self):
        """
        Verifica y maneja las colisiones entre balas, enemigos y el jugador.
        """
        hits = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)
        for enemy, bullets in hits.items():
            self.score += len(bullets)
            self.enemy_count -= 1

        self.bullets = pygame.sprite.Group(
            [bullet for bullet in self.bullets if 0 < bullet.rect.x < self.width]
        )

        self.enemies = pygame.sprite.Group(
            [enemy for enemy in self.enemies if 0 < enemy.rect.x < self.width]
        )

        player_hit = pygame.sprite.spritecollide(self.player, self.enemies, False)
        if player_hit:
            self.enemy_count -= 1
            if self.enemy_count > 0:
                self.game_over_method()
            else:
                self.check_victory()

    def run(self):
        """
        Ejecuta el bucle principal del juego.
        """
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

            if self.game_over:
                break

    def game_over_method(self):
        """
        Marca el juego como terminado.
        """
        self.game_over = True
        print("Game Over - You Lost!")

    def draw_game_over(self, message):
        """
        Dibuja el mensaje de Game Over en la pantalla.

        Args:
            message (str): El mensaje a mostrar.
        """
        game_over_text = self.font.render(message, True, (255, 255, 255))
        text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(game_over_text, text_rect)

    def draw(self):
        """
        Dibuja los elementos del juego en la pantalla.
        """
        self.screen.fill((0, 0, 30))
        self.player.draw(self.screen, self.bullets)
        self.enemies.draw(self.screen)
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        enemy_count_text = self.font.render(
            f"Enemies: {self.enemy_count}", True, (255, 255, 255)
        )
        self.screen.blit(enemy_count_text, (10, 40))

        if self.game_over:
            self.draw_game_over("You Lost!" if self.enemy_count > 0 else "You Won!")
