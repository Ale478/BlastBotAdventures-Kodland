import pygame
import math
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, bullet_image, x, y, player_rect):
        super().__init__()
        self.original_image = bullet_image
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        angle = math.degrees(math.atan2(player_rect.centery - y, x - player_rect.centerx))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.speed = 5

    def update(self):
        self.rect.x += self.speed

        # Elimina la bala si sale de la pantalla
        if self.rect.right < 0 or self.rect.left > 800 or self.rect.bottom < 0 or self.rect.top > 600:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
