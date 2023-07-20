import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, SCREEN_HEIGHT
class Bullet(Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.transform.scale(BULLET, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed # Velocidad hacia arriba (negativa en el eje y)

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom <= 0 or self.rect.top >= SCREEN_HEIGHT:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)