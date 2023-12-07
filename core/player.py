import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (screen_width // 2 - self.rect.width // 2, screen_height - self.rect.height - 10)
        self.speed = 1
        self.screen_width = screen_width 
        self.screen_height = screen_height 
        self.vel_x = 0
        self.vel_y = 0

        self.flip = False

    def handle_input(self, keys):
        # Reiniciar la velocidad a cero en cada iteración
        self.vel_x = 0
        self.vel_y = 0

        if keys[pygame.K_LEFT]:
            self.vel_x = -self.speed
        if keys[pygame.K_RIGHT]:
            self.vel_x = self.speed
        if keys[pygame.K_UP]:
            self.vel_y = -self.speed
        if keys[pygame.K_DOWN]:
            self.vel_y = self.speed

    def update(self):

        if self.vel_x < 0:
            self.flip = True
        if self.vel_x > 0:
            self.flip = False

        # Actualizar la posición del rectángulo basándose en la velocidad
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Restringir el rectángulo dentro de los límites de la pantalla
        self.rect.x = max(0, min(self.rect.x, self.screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, self.screen_height - self.rect.height))

    def draw(self, screen):
        image_flip = pygame.transform.flip(self.image, self.flip, flip_y =False)
        screen.blit(image_flip, self.rect.topleft)
