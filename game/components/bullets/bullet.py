from game.utils.constants import SCREEN_HEIGHT
from pygame.sprite import Sprite

class Bullet(Sprite):
    WIDTH = 0
    HEIGHT = 0
    SPEED = 0

    def __init__(self, image, origin):
        super().__init__()
        self.image = image
        self.rect = self.image.get.rect()
        self.rect.center = origin
        self.is_alive = False

    def update(self):
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)