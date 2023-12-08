import pygame

class Weapon:
    def __init__(self, weapon_image):
        weapon_width = 35
        weapon_height = 45
        angle = 0

        self.image = pygame.transform.scale(weapon_image, (weapon_width, weapon_height))
        self.rect = self.image.get_rect()
        self.speed = 1

    def update(self, player_rect):
        self.rect.center = player_rect.center
        self.rect.x = (player_rect.x + player_rect.width / 2 ) + 2
        self.rect.y = self.rect.y + 8.5

    

    def rotate_weapon(self, rotate):
       
        if rotate == True:
            flip_image = pygame.transform.flip(self.weapon_image,
                                           flip_x=True, flip_y=False)
            self.image = pygame.transform.rotate(flip_image, self.angle)
        else:
            flip_image = pygame.transform.flip(self.weapon_image,
                                           flip_x=False, flip_y=False)

        

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
