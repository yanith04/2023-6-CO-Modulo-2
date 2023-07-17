import pygame
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_2,SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_1



class Enemy(Sprite):

    def __init__(self,name):
        Y_POS=[100,150,200,250,300]
        super().__init__()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.name = name
        if name == "dv1":  
            enemy = ENEMY_1 
        elif name == "dv2": 
            enemy = ENEMY_2
        
        self.enemy = pygame.transform.scale(enemy, (85, 85))
        self.rect = self.enemy.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - self.rect.width // 2 
        self.rect.y = Y_POS  
        self.speed = 6 
        self.target_x = self.rect.x  
        font = pygame.font.SysFont(None, 24)
        self.name_text = font.render(f"Enemy:{name}", True, (255, 255, 255))

    def update(self, x_pos_player):
        #target_x = x_pos_player - self.rect.width // 2
        # Calcular la interpolación lineal
        #if self.rect.x < target_x:
         #   self.rect.x += min(self.speed, target_x - self.rect.x)
        #elif self.rect.x > target_x:
        #    self.rect.x -= min(self.speed, self.rect.x - target_x)
        # Actualizar la posición objetivo
       # self.target_x = target_x
       pass
    
    def draw(self):
        self.screen.blit(self.enemy, self.rect)
        self.screen.blit(self.name_text, (self.rect - 30))  