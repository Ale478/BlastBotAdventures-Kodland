import pygame
from core.bullet import Bullet  # Asegúrate de tener la clase Bullet definida en el archivo core/bullet.py

class Weapon:
    def __init__(self, weapon_image, bullet_image):
        weapon_width = 35
        weapon_height = 45
        self.original_image = pygame.transform.scale(weapon_image, (weapon_width, weapon_height))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.speed = 1
        self.bullet_image = bullet_image

    def update(self, player_rect):
        self.rect.center = player_rect.center
        self.rect.x = (player_rect.x + player_rect.width / 2)
        

        bala = None
        if pygame.mouse.get_pressed()[0]:
            bala = Bullet(self.bullet_image, self.rect.centerx, self.rect.centery, player_rect)
            
        return bala

    def draw(self, screen, bullets):
        screen.blit(self.image, self.rect.topleft)
        for bullet in bullets:
            bullet.draw(screen)


