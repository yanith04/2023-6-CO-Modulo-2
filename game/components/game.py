import pygame
from game.components.spaceship import Player
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, SPACESHIP

class Game:
    def __init__(self):
        pygame.init() # este es el enlace con la libreria pygame para poder mostrar la pantalla del juego
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Player()
        

    # este es el "game loop"
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
        # esta expression es la llamada a un metodo pygame.event.get() que devuelve un "iterable"
        for event in pygame.event.get(): # con el for sacamos cada evento del "iterable"
            if event.type == pygame.QUIT: # pygame.QUIT representa la X de la ventana
                self.playing = False
            
            
           # elif event.type == pygame.KEYDOWN:
            #if event.type == pygame.K_LEFT:
             #     self.speed = -3
            #if event.type == pygame.K_RIGHT:
             #     self.speed = 3
           # elif event.type == pygame.KEYUP:
            #   if event.key == pygame.K_LEFT:
             #     self.speed = -3
              # if event.key == pygame.K_RIGHT:
               #   self.speed = 3
            
           
    # aca escribo ALGO de la logica "necesaria" -> repartimos responsabilidades entre clases
    # o sea aqui deberia llamar a los updates de mis otros objetos
    # si tienes un spaceship; el spaceship deberia tener un "update" method que llamamos desde aqui
    def update(self):
        user_input = pygame.key.get_pressed()  # Obtener el estado actual de todas las teclas
        self.player.update(user_input)

        
       # user_input = pygame.key.get_pressed()
      #  self.update_player(user_input) 
        #self.speed = 0
        #self.x_pos_player = 0
        #keystate = pygame.key.get_pressed()
        #if self.playing:
         #   user_input = pygame.key.get_pressed()
          #  if user_input[pygame.K_LEFT]:
           #  self.speed = -5
            #if user_input[pygame.K_RIGHT]:
             # self.speed = 10

            #self.x_pos_player -+ self.speed

    # este metodo "dibuja o renderiza o refresca mis cambios en la pantalla del juego"
    # aca escribo ALGO de la logica "necesaria" -> repartimos responsabilidades entre clases
    # o sea aqui deberia llamar a los metodos "draw" de mis otros objetos
    # si tienes un spaceship; el spaceship deberia tener un "draw" method que llamamos desde aqui
    def draw(self):
        self.clock.tick(FPS) # configuramos cuantos frames dibujaremos por segundo
        self.screen.fill((255, 255, 255)) # esta tupla (255, 255, 255) representa un codigo de color: blanco
        self.draw_background()
        self.player.draw()
        pygame.display.update()
        pygame.display.flip()


    def draw_background(self):
        # le indicamos a pygame que transforme el objeto BG (que es una imagen en memoria, no es un archivo)
        # y le pedimos que ajuste el ancho y alto de esa imagen
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        # obtenemos el alto de la imagen
        image_height = image.get_height()

        ## DIBUJAMOS dos veces para dar la impresion de que nos movemos en el spacio
        # blit DIBUJA la imagen en memoria en una posicion (x, y)
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        # blit DIBUJA la imagen en memoria en una posicion (x, y)
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        # Controlamos que en el eje Y (vertical) si me sali del screen height (alto de pantalla)
        if self.y_pos_bg >= SCREEN_HEIGHT:
            # dibujo la imagen
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            # reseteo la posicion en y
            self.y_pos_bg = 0
        # No hay una velocidad de juego como tal, el "game_speed" simplemente me indica
        # cuanto me voy a mover (cuantos pixeles hacia arriba o abajo) cen el eje Y
        self.y_pos_bg += self.game_speed

    

        
            
      #if self.x_pos_bg >= SCREEN_WIDTH:
            # dibujo la imagen
         #   self.screen.blit(image_player (self.x_pos_bg, self.y_pos_bg - image_width))
            # reseteo la posicion en y
          #  self.x_pos_bg = 0
        # No hay una velocidad de juego como tal, el "game_speed" simplemente me indica
        # cuanto me voy a mover (cuantos pixeles hacia arriba o abajo) cen el eje Y
        #self.x_pos_bg += self.game_speed

        
        



    



        
