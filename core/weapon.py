import pygame
from core.bullet import Bullet


class Weapon:
    def __init__(self, weapon_image, bullet_image):
        """
        Inicializa un objeto de arma.

        Args:
            weapon_image (pygame.Surface): Imagen de la arma.
            bullet_image (pygame.Surface): Imagen de la bala asociada con el arma.
        """
        weapon_width = 35
        weapon_height = 45
        self.original_image = pygame.transform.scale(
            weapon_image, (weapon_width, weapon_height)
        )
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.speed = 1
        self.bullet_image = bullet_image

    def update(self, player_rect):
        """
        Actualiza la posición del objeto de arma y crea una bala cuando se presiona el botón del mouse.

        Args:
            player_rect (pygame.Rect): Rectángulo que representa la posición del jugador.

        Returns:
            Bullet or None: Retorna un objeto de bala si se ha presionado el botón del mouse, de lo contrario, None.
        """
        self.rect.center = player_rect.center
        self.rect.x = player_rect.x + player_rect.width / 2

        bala = None
        if pygame.mouse.get_pressed()[0]:
            bala = Bullet(
                self.bullet_image, self.rect.centerx, self.rect.centery, player_rect
            )

        return bala

    def draw(self, screen, bullets):
        """
        Dibuja el objeto de arma en la pantalla y todas las balas asociadas.

        Args:
            screen (pygame.Surface): Superficie de la pantalla.
            bullets (list): Lista de objetos de bala.
        """
        screen.blit(self.image, self.rect.topleft)
        for bullet in bullets:
            bullet.draw(screen)
