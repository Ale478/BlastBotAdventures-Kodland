import pygame

class Weapon:
    def __init__(self, weapon_image):
        weapon_width = 35
        weapon_height = 45

        # Almacena la imagen original del arma
        self.original_image = pygame.transform.scale(weapon_image, (weapon_width, weapon_height))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.speed = 1

    def update(self, player_rect):
        self.rect.center = player_rect.center
        self.rect.x = (player_rect.x + player_rect.width / 2) + 10
        


    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

