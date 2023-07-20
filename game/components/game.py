import pygame
from game.components.spaceship import Player
from game.components.enemy import Enemy
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, HEART
from pygame.sprite import Group


class Game:
    def __init__(self, num_enemies = 8):
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
        self.player_lives = 1
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
        self.show_menu()
        self.playing = True
        while self.playing:
            print(f"I am still in the game loop")
            self.handle_events()
            self.update()
            self.draw()
        else:
            print(f"game is over because self.playing is", self.playing)
        self.game_over()
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
                self.player_lives -= 1
                print("¡Has sido golpeado por una bala enemiga!")
                if self.player_lives <= 0:
                   self.playing = False
                   print("¡Has perdido todas tus vidas! El juego ha terminado.")
                else:
                    # Reiniciar la posición del jugador después de perder una vida
                    self.player.rect.centerx = SCREEN_WIDTH // 2
                    self.player.rect.bottom = SCREEN_HEIGHT - 10
             # Verificar colisión entre el jugador y los enemigos
            if pygame.sprite.spritecollide(self.player, self.enemies, dokill=True):
               self.player_lives -= 1
               print("¡Has chocado con un enemigo!")
               if self.player_lives <= 0:
                  self.playing = False
                  print("¡Has perdido todas tus vidas! El juego ha terminado.")
               else:
                    # Reiniciar la posición del jugador después de perder una vida
                    self.player.rect.centerx = SCREEN_WIDTH // 2
                    self.player.rect.bottom = SCREEN_HEIGHT - 10
        
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
        for enemy in self.enemies:
            enemy.draw(self.screen)
         # Dibujar el contador en la parte superior de la pantalla
        font = pygame.font.Font(None, 36)
        text = font.render("Enemigos eliminados: " + str(self.enemies_killed), True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 30))
        self.screen.blit(text, text_rect)    
        
        # Dibujar los corazones (vidas) del jugador en la parte superior izquierda de la pantalla
        heart_img = pygame.transform.scale(HEART, (30, 30))  # Ajusta el tamaño según tus preferencias
        heart_spacing = 40  # Espaciado entre los corazones
        for i in range(self.player_lives):
            self.screen.blit(heart_img, (10 + i * heart_spacing, 10))

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

    def show_menu(self):
        menu_font = pygame.font.Font(None, 50)
        options = ["Play"]

        self.screen.fill((0, 0, 139))
        for i, option in enumerate(options):
            text_color = (255, 255, 255)
            text = menu_font.render(option, True, text_color)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 60))
            self.screen.blit(text, text_rect)

        pygame.display.update()

        wait_for_key = True
        while wait_for_key:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    wait_for_key = False

    
    def game_over(self):
        game_over_font = pygame.font.Font(None, 50)
        instructions_font = pygame.font.Font(None, 30)
        options = ["Restart"]
        selected_option = 0

        while True:
              self.screen.fill((0, 0, 139))
              for i, option in enumerate(options):
                  text_color = (255, 255, 255)
              if i == selected_option:
                text_color = (255, 0, 0)  # Cambiar color de la opción seleccionada
                text = game_over_font.render(option, True, text_color)
                text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 60))
                self.screen.blit(text, text_rect)

                # Mostrar la cantidad de enemigos eliminados
                score_font = pygame.font.Font(None, 36)
                score_text = score_font.render("Enemigos eliminados: " + str(self.enemies_killed), True, (255, 255, 255))
                score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + len(options) * 60 + 60))
                self.screen.blit(score_text, score_rect)

                 # Mostrar instrucciones para reiniciar
                instructions_text = instructions_font.render("Press Enter to Restart", True, (255, 255, 255 ))
                instructions_rect = instructions_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + len(options) * 60 + 20))
                self.screen.blit(instructions_text, instructions_rect)

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                       pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_RETURN:
                          if selected_option == 0:  # Reiniciar el juego
                             self.reset_game()
                             return

                          return

    def reset_game(self):
        # Restablecer las variables del juego para reiniciar
        self.player_lives = 10
        self.enemies_killed = 0
        self.player.rect.centerx = SCREEN_WIDTH // 2
        self.player.rect.bottom = SCREEN_HEIGHT - 10
        self.enemies.empty()
        self.bullets_player.empty()
        self.bullets_enemies.empty()
        self.run()