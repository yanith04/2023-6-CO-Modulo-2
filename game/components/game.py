import pygame
import random
from game.components.spaceship import Player
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, SPAWN_ENEMY, ENEMY_SHOOT, EASY_LEVEL_ENEMY_SPAWNS, EASY_LEVEL_MAX_ENEMIES
from game.components.bullets.bullet_hadler import BulletHandler
from game.components.bullets.bullet_factory import BulletFactory
from game.components.enemy.factory.factory_level_enemy import LevelBasedEnemyFactory
from game.components.enemy.enemy_handler import EnemyHandler

class Game:
    def __init__(self):
        pygame.init() 
        pygame.time.set_timer(SPAWN_ENEMY, 700)
        pygame.time.set_timer(ENEMY_SHOOT, 1500)
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.runnig = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0

        self.player = Player("xwing")
        self.enemy_handler = EnemyHandler(LevelBasedEnemyFactory(EASY_LEVEL_ENEMY_SPAWNS, EASY_LEVEL_MAX_ENEMIES))
        self.bullet_handler = BulletHandler(BulletFactory())
        self.deaths_count = 0
        self.destroyed_enemies = 0

         
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.player.shoot(self.bullet_handler)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.player.shoot(self.bullet_handler)
            elif event.type == SPAWN_ENEMY:
                self.enemy_handler.add_enemy()
            elif event.type == ENEMY_SHOOT:
                self.enemy_handler.shoot(self.bullet_handler)


    def update(self):
        user_input = pygame.key.get_pressed()  
        self.player.update(user_input)
        if self.playing:
            if not self.player.is_alive:
                self.playing = False
                self.deaths_count += 1
                self.destroyed_enemies = self.enemy_handler.get_destroyed_enemies_count()
                self.reset()

            user_input = pygame.key.get_pressed()
            self.player.update(user_input)
            self.enemy_handler.update(self.player)
            self.bullet_handler.update(self.player, self.enemy_handler.get_enemies())


    def draw(self):
        if self.playing:
           self.clock.tick(FPS) 
           self.screen.fill((255, 255, 255)) 
           self.draw_background()
           self.player.draw()
           self.enemy_handler.draw(self.screen)
           self.bullet_handler.draw(self.screen)
        else:
            self.draw_menu()


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

    def draw_menu(self):
        if self.deaths_count == 0:
            font = pygame.font.SysFont(None, 24)
            self.name_text = font.render(f"MENU", True, (255, 255, 255))

        else:
            font = pygame.font.SysFont(None, 24)
            self.name_text = font.render(f"Enemies destroyed: " + str(self.destroyed_enemies), True, (255, 255, 255))
    
    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
            
        