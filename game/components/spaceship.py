import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP,SCREEN_WIDTH,SCREEN_HEIGHT, FPS, BULLET_PLAYER_TYPE
from game.components.bullets.bullet_hadler import BulletHandler

class Player(Sprite):
    BLINK_DURATION_SECS = 2
    BLINK_DURATION_CYCLES = BLINK_DURATION_SECS * FPS
    ALPHA_INTERVAL = (255 // (FPS // 2)) 
    WIDTH = 40
    HEIGTH = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500  
    def __init__(self, name,):
        super().__init__()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.image = pygame.transform.scale(SPACESHIP, (self.WIDTH,self.HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.speed = 10
        self.limit_y = 300
        font = pygame.font.SysFont(None, 24)
        self.name_text = font.render(f"Player:{name}", True, (255, 255, 255))
        self.is_alive = True
        self.lifes = 3
        self.is_blinking = False
        self.is_visible = True
        self.cycles = self.BLINK_DURATION_CYCLES
        self.alpha_value = 255
        self.bullet_handler = BulletHandler()

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
        
        if self.is_blinking:
            self.__blink()
        if self.lifes <= 0:
            self.kill()


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

    def kill(self):
        self.is_alive = False

    def reduce_lifes(self):
        self.lifes -= 1
    def __blink(self):
        if self.cycles < self.BLINK_DURATION_CYCLES:
            new_alpha = self.alpha_value - self.ALPHA_INTERVAL

            if new_alpha < 0:
                self.is_visible = False
            
            if self.alpha_value == 255:
                self.is_visible = True

            if self.is_visible:
                self.alpha_value = new_alpha
            else:
                self.alpha_value += self.ALPHA_INTERVAL
            self.image.set_alpha(self.alpha_value)
            self.cycles += 1
        else:
            self.is_blinking = False
            self.is_visible = True
            self.image.set_alpha(255)
            self.alpha_value = 255

    def start_blink(self):
        self.is_blinking = True
        self.cycles = 0

    def shoot(self):
        self.bullet_handler.add_bullet(BULLET_PLAYER_TYPE, self.rect.center)


    def display_limit(self):
        if self.rect.x < 0:
           self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - 80:    
           self.rect.x = SCREEN_WIDTH - 80
                             
        if self.rect.y < self.limit_y: 
           self.rect.y = self.limit_y 
        if self.rect.y > SCREEN_HEIGHT - 80:
           self.rect.y = SCREEN_HEIGHT - 80
    

    def draw(self):
        self.screen.blit(self.image, (self.rect.x , self.rect.y))     
        self.screen.blit(self.name_text, (self.rect.x, self.rect.y - 30))

    def reset(self):
        self.is_alive = True
        self.lifes = 3
        self.is_blinking = False
        self.is_visible = True
        self.cycles = self.BLINK_DURATION_CYCLES
        self.alpha_value = 255
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
