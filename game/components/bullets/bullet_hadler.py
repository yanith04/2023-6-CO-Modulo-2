import pygame
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_player import BulletPlayer
from game.components.bullets.bullet import Bullet
from game.components.bullets.bullet_factory import BulletFactory

class BulletHandler:
    def __init__(self):
        self.bullets = pygame.sprite.Group()
        self.bullet_factory = BulletFactory()
        self.bullet = Bullet()

    def update(self, player, enemies):
        for bullet in self.bullets:
            bullet.update()

            if type(bullet) == BulletEnemy:
                self.check_player_collition(bullet, player)
            elif type(bullet) == BulletPlayer:
                self.check_enemies_collition(bullet, enemies)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def check_player_collition(self, bullet, player):
        if pygame.sprite.collide_rect(bullet, player) and not player.is_blinking:
            player.start_blink()
            player.reduce_lifes()

    def check_enemies_collition(self, bullet, enemies):
        enemies_collided = pygame.sprite.spritecollide(bullet, enemies, False)

        if len(enemies_collided) > 0:
            bullet.kill()
            for enemy in enemies_collided:
                enemy.destroy()


    def add_bullet(self, bullet_type, origin):
            bullet = self.bullet_factory.get_bullet(bullet_type, origin)
            self.bullets.add(bullet)

    def reset(self):
        self.bullets.empty()