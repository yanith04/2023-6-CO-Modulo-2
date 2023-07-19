import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30

## IMG_DIR es el camino a encontrar los "archivos" de imagenes
# sonido, etc

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants

# pygame.image.load --> carga la imagen en memoria y la guardamos en la variable ....por ejemplo ICON
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = 'freesansbold.ttf'

# Movement constants
LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'

# Enemies constants
ENEMY_DV1_TYPE = 'dv1'
ENEMY_DV2_TYPE = 'dv2'
ENEMY_DV3_TYPE = 'dv3'
ENEMIES_TYPES = [ENEMY_DV1_TYPE, ENEMY_DV2_TYPE, ENEMY_DV3_TYPE]

EASY_LEVEL_MAX_ENEMIES = 3
MEDIUM_LEVEL_MAX_ENEMIES = 5
HARD_LEVEL_MAX_ENEMIES = 7

EASY_LEVEL_ENEMY_SPAWNS = [3, 1, 0]
MEDIUM_LEVEL_ENEMY_SPAWNS = [4, 2, 1]
HARD_LEVEL_ENEMY_SPAWNS = [1, 2, 1]

# Bullet constants
BULLET_ENEMY_TYPE = 'enemy'
BULLET_PLAYER_TYPE = 'player'

# Custom events
SPAWN_ENEMY = pygame.USEREVENT + 1
ENEMY_DV1_SHOOT = pygame.USEREVENT + 2
ENEMY_DV2_SHOOT = pygame.USEREVENT + 3
ENEMY_DV3_SHOOT = pygame.USEREVENT + 4
ENEMY_SHOOT = pygame.USEREVENT + 5

# Color
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255 ,255)

