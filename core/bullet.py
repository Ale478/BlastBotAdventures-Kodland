import pygame
import math
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, bullet_image, x, y, player_rect):
        """
        Inicializa un objeto de bala.

        Args:
            bullet_image (pygame.Surface): Imagen de la bala.
            x (int): Posición horizontal inicial de la bala.
            y (int): Posición vertical inicial de la bala.
            player_rect (pygame.Rect): Rectángulo del jugador para calcular el ángulo.
        """
        super().__init__()
        self.original_image = bullet_image
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        angle = math.degrees(
            math.atan2(player_rect.centery - y, x - player_rect.centerx)
        )
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.speed = 5

    def update(self):
        """
        Actualiza la posición de la bala en función de su velocidad.

        Elimina la bala si sale de la pantalla.
        """
        self.rect.x += self.speed

        if (
            self.rect.right < 0
            or self.rect.left > 800
            or self.rect.bottom < 0
            or self.rect.top > 600
        ):
            self.kill()

    def draw(self, screen):
        """
        Dibuja la bala en la pantalla.

        Args:
            screen (pygame.Surface): Superficie de la pantalla donde se dibuja la bala.
        """
        screen.blit(self.image, self.rect.topleft)
