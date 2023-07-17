import pygame
from game.components.spaceship import Player
from game.components.enemy import Enemy
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE

class Game:
    def __init__(self):
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
        self.enemies =Enemy[dv1,dv2]

        dv1 = Enemy("dv1")
        dv2 = Enemy("dv2")

        

        
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
       # for self.enemy in self.enemies:
        #    self.enemy.update()


    def draw(self):
        self.clock.tick(FPS) 
        self.screen.fill((255, 255, 255)) 
        self.draw_background()
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
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
