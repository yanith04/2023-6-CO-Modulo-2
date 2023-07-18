import pygame
import random
from game.components.spaceship import Player
from game.components.enemy import Enemy
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

class Game:
    def __init__(self, num_enemies = 10):
        pygame.init() 
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Player("xwing")
        self.enemy = Enemy("dv1")
        self.enemies = []
        self.num_enemies = num_enemies

        
# # Game loop: events - update - draw
    def run(self):
        self.playing = True
        while self.playing:
            print(f"I am still in the game loop")
            self.handle_events()
            self.update()
            self.draw()
        else:
            print(f"game is over because self.playing is", self.playing)
        pygame.display.quit()
        pygame.quit()


    def handle_events(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.playing = False


    def update(self):
        user_input = pygame.key.get_pressed()  
        self.player.update(user_input)
        self.move_x_for = random.randint(30, 100)
        for enemy in self.enemies:
            enemy.update()
        
        if len(self.enemies) < self.num_enemies:
            enemy_name = f"ENEMY(len(self.enemies)+1)"
            new_enemy = Enemy(enemy_name)
            self.enemies.append(new_enemy)

        


    def draw(self):
        self.clock.tick(FPS) 
        self.screen.fill((255, 255, 255)) 
        self.draw_background()
        self.player.draw()
        for self.enemy in self.enemies:
            self.enemy.draw()
        pygame.display.update()
        pygame.display.flip()


    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()

        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
