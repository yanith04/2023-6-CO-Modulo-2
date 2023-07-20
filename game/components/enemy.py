import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_1



class Enemy(Sprite):
    limite_y = SCREEN_HEIGHT
    limite_x = SCREEN_WIDTH
    
    pos_y = [y for y in range(limite_y + 1)]
    pos_x = [x for x in range(limite_x + 1)]

    def __init__(self,name):
        super().__init__()
        self.image = ENEMY_1 
        self.enemy = pygame.transform.scale(self.image, (85, 85))
        self.rect = self.enemy.get_rect()
        self.rect.x = random.choice(self.pos_x)
        self.rect.y = random.choice(self.pos_y)
        self.speed = 6

        self.enemy_name = name   
        font = pygame.font.SysFont(None, 24)
        self.name_text = font.render(f"Enemy:{self.enemy_name}", True, (255, 255, 255))

    def update(self):    

        self.rect.y += self.speed
        if self.rect.y >= SCREEN_HEIGHT:
           self.rect.y = -self.rect.height
        
        self.rect.x += self.speed
        if self.rect.x >= SCREEN_WIDTH:
           self.rect.x = -self.rect.width

    def display_limit(self): 
        pass
    


    def draw(self, screen):
        screen.blit(self.enemy, (self.rect.x, self.rect.y))
        screen.blit(self.name_text, (self.rect.x, self.rect.y - 30))  