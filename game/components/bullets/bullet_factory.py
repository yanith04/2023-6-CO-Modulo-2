from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_PLAYER_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_player import BulletPlayer


class BulletFactory:
    
    BULLETS = [BULLET_ENEMY_TYPE]

    def get_bullet(self, bullet_type, origin):
        bullet = None

        if bullet_type == BULLET_ENEMY_TYPE:
            bullet = BulletEnemy(origin)
        elif bullet_type == BULLET_PLAYER_TYPE:
            bullet = BulletPlayer(origin)

        return bullet