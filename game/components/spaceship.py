import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP,SCREEN_WIDTH,SCREEN_HEIGHT, HEART
from game.components.bullet import Bullet

class Player(Sprite):   
    def __init__(self, name, starting_lives=3):
        super().__init__()
        self.image_player = pygame.transform.scale(SPACESHIP, (50,50))
        self.rect = self.image_player.get_rect()
        self.rect.x = 460
        self.rect.y = 460
        self.speed = 10
        font = pygame.font.SysFont(None, 24)
        self.name_text = font.render(f"Player:{name}", True, (255, 255, 255))
        self.bullets_player = Group()
        self.lives = starting_lives
      


    def update(self, user_input):
        
        if user_input[pygame.K_LEFT]  or user_input[pygame.K_a] :
            self.move_left()
            print("move left")
        if user_input[pygame.K_RIGHT] or user_input[pygame.K_d] :
           self.move_right()
           print("move right")
        if user_input[pygame.K_UP] or user_input[pygame.K_w] :
            self.move_up()
            print("move up")
        if user_input[pygame.K_DOWN] or user_input[pygame.K_s] :
            self.move_down()
            print("move down")
        if user_input[pygame.K_SPACE]:
            self.shoot_bullet()
            print("shoot bullet") 
        self.update_bullet_trajectory()


    def move_left(self):
        self.rect.x -= self.speed
        self.display_limit()
    def move_right(self):
        self.rect.x += self.speed
        self.display_limit()
    def move_up(self):
        self.rect.y -= self.speed
        self.display_limit()
    def move_down(self):
        self.rect.y += self.speed
        self.display_limit()

    def shoot_bullet(self):
           bullet_player = Bullet(self.rect.centerx, self.rect.top, -15)
           self.bullets_player.add(bullet_player)

        

    def display_limit(self):
        if self.rect.x < 0:
           self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - 80:    
           self.rect.x = SCREEN_WIDTH - 80
         
                        
        if self.rect.y < 0: 
           self.rect.y = 0 
        if self.rect.y > SCREEN_HEIGHT - 80:
           self.rect.y = SCREEN_HEIGHT - 80

    def update_bullet_trajectory(self):
        for bullet in self.bullets_player:
            bullet.rect.y += bullet.speed
            if bullet.rect.y < 0:
               self.bullets_player.remove(bullet)

    def remove_life(self):
        self.lives -= 1
        if self.lives <= 0:
            # Aquí puedes tomar alguna acción cuando el jugador se queda sin vidas,
            # como terminar el juego o mostrar un mensaje de "Game Over".
            print("Game Over")

    def draw_lives(self, screen):
        for i in range(self.lives):
            heart_x = SCREEN_WIDTH - 30 - i * 30
            heart_y = 10
            screen.blit(HEART, (heart_x, heart_y))
    

    def draw(self,screen):
        screen.blit(self.image_player, (self.rect.x , self.rect.y))      
        screen.blit(self.name_text, (self.rect.x, self.rect.y - 30))
        self.bullets_player.draw(screen)


