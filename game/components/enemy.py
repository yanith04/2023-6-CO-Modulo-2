import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_1, ENEMY_2


class Enemy(Sprite):

    MOV_X = {0: 'left', 1: 'right'}
    Y_POS=[100,150,200,250,300]
    MOV_X = {0: 'left', 1: 'right'}


    def __init__(self,name):
        super().__init__()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.name = name 
        self.image = random.choice([ENEMY_1, ENEMY_2])     
        self.enemy = pygame.transform.scale(self.image, (85, 85))
        self.rect = self.enemy.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - self.rect.width // 2 
        self.rect.y = random.choice([100, 150, 200, 250])
        self.mov_x = self.MOV_X[random.randint(0, 1)]
        self.mov_x_for = random.randint(30, 100)
        self.speed = 6  
        self.index = 0 
        font = pygame.font.SysFont(None, 24)
        self.name_text = font.render(f"Enemy:{name}", True, (255, 255, 255))


    def update(self):
        self.rect.y += self.speed
        if self.mov_x == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        self.change_mov_x()


    def change_mov_x(self):
        self.index += 1
        if (self.index >= self.mov_x_for and self.mov_x == 'right') or (self.rect.x >= SCREEN_WIDTH - 85):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.mov_x_for and self.mov_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.index = 0


    def draw(self):
        self.screen.blit(self.enemy, (self.rect.x, self.rect.y))
        self.screen.blit(self.name_text, (self.rect.x, self.rect.y - 30))  