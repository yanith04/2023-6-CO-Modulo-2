import pygame
import random
import math
from pygame.sprite import Group
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_1, ENEMY_2
from game.components.bullet import Bullet


class Enemy(Sprite):

    def __init__(self,name):
        super().__init__()
        self.image = random.choice([ENEMY_1, ENEMY_2])  
        self.enemy = pygame.transform.scale(self.image, (85, 85))
        self.rect = self.enemy.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = 10
        self.amplitude = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))  # Amplitud del movimiento en el eje X
        self.frequency = random.uniform(0.10, 0.10)  # Frecuencia del movimiento en el eje X
        self.phase = random.uniform(0, 2 * math.pi)  # Fase inicial del movimiento en el eje X
        self.shoot_timer = 100
        self.bullets_enemies = Group()


        self.enemy_name = name   
        font = pygame.font.SysFont(None, 24)
        self.name_text = font.render(f"Enemy:{self.enemy_name}", True, (255, 255, 255))

    def update(self):    
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_HEIGHT:
            self.rect.y = -self.rect.height

        # Calcular la posición X en función del tiempo usando la función seno
        time = pygame.time.get_ticks() * 0.001  # Convertir tiempo en segundos
        self.rect.x = self.amplitude * math.sin(2 * math.pi * self.frequency * time + self.phase) + (SCREEN_WIDTH - self.rect.width) / 2
    
        self.shoot_timer -= 1
        if self.shoot_timer <= 0:
            self.shoot_bullet()
            self.shoot_timer = 20
            # Actualizar las balas del enemigo
        self.bullets_enemies.update()

        

 
    def draw(self, screen):
        screen.blit(self.enemy, (self.rect.x, self.rect.y))
        screen.blit(self.name_text, (self.rect.x, self.rect.y - 30))
        self.bullets_enemies.draw(screen)

    def shoot_bullet(self):
        bullet_enemy = Bullet(self.rect.centerx, self.rect.top, 15)
        self.bullets_enemies.add(bullet_enemy)
    



