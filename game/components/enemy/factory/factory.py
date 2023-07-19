from game.utils.constants import ENEMY_DV2_TYPE, ENEMY_DV1_TYPE, ENEMY_DV3_TYPE, EASY_LEVEL_MAX_ENEMIES
from game.components.enemy.dv1 import Dv1
from game.components.enemy.dv2 import Dv2
from game.components.enemy.dv3 import Dv3


class Enemyfactory:

    def __init__(self, max_enemies = EASY_LEVEL_MAX_ENEMIES):
        self.max_enemies = max_enemies
        self.instance_count = 0

    def get_enemy(self, enemy_type):
        enemy = None

        if self.instance_count < self.max_enemies:
            enemy = self.__instance_enemy(enemy_type)

        return enemy
    
    def __instance_enemy(self, enemy_type):
        enemy = None

        if enemy_type == ENEMY_DV2_TYPE:
            enemy = Dv2()
            self.instance_count += 1

        elif enemy_type == ENEMY_DV1_TYPE:
            enemy = Dv1()
            self.instance_count += 1

        elif enemy_type == ENEMY_DV3_TYPE:
            enemy = Dv3()
            self.instance_count += 1

        return enemy
    
    def reduce_instance_count(self):
        self.instance_count -= 1
    
    def get_max_enemies(self):
        return  self.max_enemies