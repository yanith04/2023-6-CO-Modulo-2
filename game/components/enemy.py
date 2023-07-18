import pygame
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_1



class Enemy(Sprite):

    def __init__(self,name):
       # Y_POS=[100,150,200,250,300]
        super().__init__()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.name = name 
        self.image = ENEMY_1 

        
        self.enemy = pygame.transform.scale(self.image, (85, 85))
        self.rect = self.enemy.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - self.rect.width // 2 
        self.rect.y = 100
        self.speed = 6   
        font = pygame.font.SysFont(None, 24)
        self.name_text = font.render(f"Enemy:{name}", True, (255, 255, 255))

    def update(self):
        pass

    
    def draw(self):
        self.screen.blit(self.enemy, (self.rect.x, self.rect.y))
        self.screen.blit(self.name_text, (self.rect.x, self.rect.y - 30))  