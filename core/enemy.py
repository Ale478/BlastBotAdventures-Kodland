import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, images):
        """
        Inicializa un objeto de enemigo.

        Args:
            x (int): Posición horizontal inicial del enemigo.
            y (int): Posición vertical inicial del enemigo.
            images (list): Lista de rutas de imágenes para la animación del enemigo.
        """
        super().__init__()
        self.images = [pygame.image.load(image) for image in images]
        self.image_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 1
        self.flip = False

    def update(self):
        """
        Actualiza la animación del enemigo.

        La animación cambia a la siguiente imagen en la lista después de un cierto tiempo.

        """
        cooldown_animation = 100
        self.image = self.images[self.image_index]

        if pygame.time.get_ticks() - self.update_time >= cooldown_animation:
            self.image_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.image_index >= len(self.images):
            self.image_index = 0

    def draw(self, screen):
        """
        Dibuja el enemigo en la pantalla.

        Args:
            screen (pygame.Surface): Superficie de la pantalla donde se dibuja el enemigo.
        """
        image_flip = pygame.transform.flip(self.image, self.flip, flip_y=False)
        screen.blit(image_flip, self.rect.topleft)
