import pygame

class Player(pygame.Rect):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width // 2 - 25, screen_height - 50, 50, 50)
        self.speed = 5

    def handle_input(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < screen_width - 50:
            self.x += self.speed

    def update(self):
        pass  # Puedes agregar lógica de actualización si es necesario

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self)
