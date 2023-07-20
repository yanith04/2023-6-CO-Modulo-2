import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP,SCREEN_WIDTH,SCREEN_HEIGHT
#from game.components.bullet import Bullet

class Player(Sprite):   
    def __init__(self,name):
        super().__init__()
        self.image_player = pygame.transform.scale(SPACESHIP, (50,50))
        self.rect = self.image_player.get_rect()
        self.rect.x = 460
        self.rect.y = 460
        self.speed = 10
        font = pygame.font.SysFont(None, 24)
        self.name_text = font.render(f"Player:{name}", True, (255, 255, 255))

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

    
    def display_limit(self):
        if self.rect.x < 0:
           self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - 80:    
           self.rect.x = SCREEN_WIDTH - 80
         
                        
        if self.rect.y < 0: 
           self.rect.y = 0 
        if self.rect.y > SCREEN_HEIGHT - 80:
           self.rect.y = SCREEN_HEIGHT - 80
    

    def draw(self,screen):
        screen.blit(self.image_player, (self.rect.x , self.rect.y))      
        screen.blit(self.name_text, (self.rect.x, self.rect.y - 30))
        #screen.blit(bullet,(self.x_pos_player, self.y_pos_player))





    