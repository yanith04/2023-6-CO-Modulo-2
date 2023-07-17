import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP,SCREEN_WIDTH,SCREEN_HEIGHT

class Player(Sprite):   
    def __init__(self,name):
        super().__init__()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.image_player = pygame.transform.scale(SPACESHIP, (80,80))
        self.x_pos_player = 460
        self.y_pos_player = 460
        self.speed = 10
        self.limit_y = 300
        #self.player_name = name
        font = pygame.font.SysFont(None, 24)
        self.name_text = font.render(f"Player:{name}", True, (255, 255, 255))

    def update(self, user_input):
        if user_input[pygame.K_LEFT]  or user_input[pygame.K_a] :
            self.move_left()
        if user_input[pygame.K_RIGHT] or user_input[pygame.K_d] :
           self.move_right()
        if user_input[pygame.K_UP] or user_input[pygame.K_w] :
            self.move_up()
        if user_input[pygame.K_DOWN] or user_input[pygame.K_s] :
            self.move_down()


    def move_left(self):
        self.x_pos_player -= self.speed
        self.display_limit()
    def move_right(self):
        self.x_pos_player += self.speed
        self.display_limit()
    def move_up(self):
        self.y_pos_player -= self.speed
        self.display_limit()
    def move_down(self):
        self.y_pos_player += self.speed
        self.display_limit()

    
    def display_limit(self):
        if self.x_pos_player < 0:
           self.x_pos_player= 0
        if self.x_pos_player > SCREEN_WIDTH - 80:    
           self.x_pos_player = SCREEN_WIDTH - 80
         
                        
        if self.y_pos_player < self.limit_y: 
           self.y_pos_player = self.limit_y 
        if self.y_pos_player > SCREEN_HEIGHT - 80:
           self.y_pos_player = SCREEN_HEIGHT - 80
    

    def draw(self):
        self.screen.blit(self.image_player, (self.x_pos_player , self.y_pos_player))      
       
       # label
        self.screen.blit(self.name_text, (self.x_pos_player, self.y_pos_player - 30))
