import pygame
from game.utils.constants import SPACESHIP,SCREEN_HEIGHT,SCREEN_WIDTH

class Player:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.image_player = pygame.transform.scale(SPACESHIP, (100,100))
        self.x_pos_player = 1000
        self.y_pos_player = 500
        self.speed = 0

        # self.rect = image_player.get_rect(self.x_pos_bg,self.y_pos_bg,100,100)
        #image_width = image_player.get_width
        

    def update(self, user_input):
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_LEFT]:
           self.speed = -8
        if user_input[pygame.K_RIGHT]:
           self.speed = 8
        if not user_input[pygame.K_LEFT] and not user_input[pygame.K_RIGHT]:
           self.speed = 0

           self.x_pos_player += self.speed
        
        if self.x_pos_player > 1000:
           self.x_pos_player = self.speed
        if self.x_pos_player < -1000:
           self.x_pos_player = self.speed
           

        
        


    def draw(self):
        self.screen.blit(self.image_player, (self.x_pos_player , self.y_pos_player))      
    


