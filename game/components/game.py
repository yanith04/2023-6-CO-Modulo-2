import pygame
from game.components.spaceship import Player
from game.components.enemy import Enemy
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from pygame.sprite import Group


class Game:
    def __init__(self, num_enemies = 5):
        pygame.init() 
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        #PLAYER
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
  
  
        self.y_pos_bg = 0
        self.player = Player("xwing")
        self.bullets_player =Group()

        #ENEMY
        self.enemy = Enemy("dv1")
        self.num_enemies = num_enemies
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.enemies = Group()
        self.bullets_enemies = Group()
        self.collided_enemies = pygame.sprite.groupcollide(self.enemies, self.player.bullets_player, True, True)
        self.enemies_killed = 0
      
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
                # Comprobar si el temporizador ha expirado
            if event.type == pygame.USEREVENT:
                self.add_enemy()

    
    def add_enemy(self):
        if len(self.enemies) < self.num_enemies:
            enemy_name = f"ENEMY{len(self.enemies) + 1}"
            new_enemy = Enemy(enemy_name)
            self.enemies.add(new_enemy)
     

    def update(self):
        #PLAYER
        user_input = pygame.key.get_pressed()  
        self.player.update(user_input)
        print(f"{self.player.update(user_input)}")
            

        #ENEMY
        for enemy in self.enemies:
            enemy.update()
            

            # Detectar colisiones entre balas enemigas y el jugador
            if pygame.sprite.spritecollide(self.player, enemy.bullets_enemies, dokill=True):
                self.playing = False
                print("¡Has sido golpeado por una bala enemiga! El juego ha terminado.")
                
            # Verificar colisión entre el jugador y los enemigos
            if pygame.sprite.spritecollide(self.player, self.enemies, dokill=True):
               self.playing = False
               print("¡Has chocado con un enemigo! El juego ha terminado.")
        
        # Detectar colisiones entre balas del jugador y los enemigos
        collided_enemies = pygame.sprite.groupcollide(self.enemies, self.player.bullets_player, True, True)
        if collided_enemies:
          self.enemies_killed += len(collided_enemies)  # Actualizar el contador
          print("¡Has eliminado a un enemigo!")

                    
    def draw(self):
        self.clock.tick(FPS) 
        self.screen.fill((255, 255, 255)) 
        self.draw_background()
        self.player.draw(self.screen)
        self.player.draw_lives(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)

         # Dibujar el contador en la parte superior de la pantalla
        font = pygame.font.Font(None, 36)
        text = font.render("Enemigos eliminados: " + str(self.enemies_killed), True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 30))
        self.screen.blit(text, text_rect)    
        
        
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