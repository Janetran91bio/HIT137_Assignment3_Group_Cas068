import pygame
import Configuration as config
from random import randint

ALTERNATE_ENEMY_SIZE = config.ALTERNATE_ENEMY_SIZE
FINAL_BOSS_SIZE = config.FINAL_BOSS_SIZE

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 1:
            self.surface = pygame.transform.scale(pygame.image.load('images/obstacle1.png'), (config.OBS_SIZE, config.OBS_SIZE))
            self.y_pos   = config.SKY_LEVEL
        elif type == 2:
            self.surface = pygame.transform.scale(pygame.image.load('images/enemy-2.png'), (config.OBS_SIZE * 1.2, ALTERNATE_ENEMY_SIZE))
            self.y_pos   = config.GROUND_LEVEL
        elif type == 3:
            self.surface = pygame.transform.scale(pygame.image.load('images/enemy-1.png'), (config.OBS_SIZE * 1.2, ALTERNATE_ENEMY_SIZE))
            self.y_pos   = config.GROUND_LEVEL
        else:
            self.surface = pygame.transform.scale(pygame.image.load('images/final_boss.png'), (config.OBS_SIZE * 1.2, FINAL_BOSS_SIZE))
            self.y_pos   = config.GROUND_LEVEL

        self.image = self.surface
        self.rect    = self.image.get_rect(
                            bottomright=(randint(900,1100), self.y_pos))
        self.speed = 5
        self.facing_right = False

    def flipping(self):
        if self.rect.left <= self.left_boundary: 
            self.rect.right += config.OBS_SIZE
            self.facing_right = True
            self.surface = pygame.transform.flip(self.surface, True, False)
        elif self.rect.right >= self.right_boundary: 
            self.rect.left -= config.OBS_SIZE
            self.facing_right = False
            self.surface = pygame.transform.flip(self.surface, True, False)

    def update(self):
        self.rect.left -= self.speed
        if self.rect.x <= -100: self.kill()