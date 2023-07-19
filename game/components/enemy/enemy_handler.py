import pygame
from game.components.enemy.dv3 import Dv3
from game.components.spaceship import Player
from game.components.enemy.factory.factory import Enemyfactory
from game.components.enemy.enemy import Enemy


class EnemyHandler():

    def __init__(self):
        self.enemies = pygame.sprite.Group()
        self.enemy_factory = Enemyfactory()
        self.destroyed_enemies = 0
        self.total_score = 0
        self.player = Player()
        self.enemy = Enemy()
        

    def update(self):
        for self.enemy in self.enemies:
            if type(self.enemy) == Dv3:
                self.enemy.update(self.player.rect.x, self.player.rect.y)
            else:
                self.enemy.update()
            
            if self.enemy.was_destroyed():
                self.enemy.kill()
                self.enemy_factory.reduce_instance_count()
                self.destroyed_enemies += 1

            if self.enemy.is_out_of_bounds:
                self.enemy.kill()
                self.enemy_factory.reduce_instance_count()

        for enemy in pygame.sprite.spritecollide(self.player, self.enemies, False):
            if not self.player.is_blinking:
                self.player.start_blink()
                self.player.reduce_lifes()
                enemy.kill()
                self.enemy_factory.reduce_instance_count()

    def draw(self, screen):
        self.enemies.draw(screen)

    def shoot(self, bullet_handler):
        for self.enemy in self.enemies:
            self.enemy.shoot(bullet_handler)

    def add_enemy(self):
        new_enemy = self.enemy_factory.get_enemy()
        
        if new_enemy != None:
            self.enemies.add(new_enemy)

    def get_enemies(self):
        return self.enemies
    
    def get_destroyed_enemies_count(self):
        return self.destroyed_enemies

    def get_player_collisions(self, player):
        return pygame.sprite.spritecollide(player, self.enemies, False)
    
    def reset(self):
        self.enemies.empty()
        self.enemy_factory.instance_count = 0
        self.destroyed_enemies = 0
        self.total_score = 0