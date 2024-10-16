import pygame
import Configuration as config

SKY_LEVEL = config.SKY_LEVEL
GROUND_LEVEL = config.GROUND_LEVEL
COIN_SIZE = config.COIN_SIZE

# Coins
coin_path = 'images/coin.png'
coin_surface = pygame.image.load(coin_path)
coin_surface = pygame.transform.scale(coin_surface, (COIN_SIZE, COIN_SIZE))
coin_rect    = coin_surface.get_rect(center=(200, SKY_LEVEL))

class Collectible(pygame.sprite.Sprite):
    def __init__(self, type, coin_num):
        super().__init__()
        self.surface = pygame.image.load('images/coin.png')
        if type == 1: self.y_pos   = SKY_LEVEL
        else:         self.y_pos   = GROUND_LEVEL
        self.image = pygame.transform.scale(self.surface,(COIN_SIZE, COIN_SIZE))
        self.rect = coin_surface.get_rect(bottomright= \
                    (1000+ COIN_SIZE*coin_num, self.y_pos))
        self.speed = 5

    def update(self):
        self.rect.left -= self.speed
        if self.rect.x <= -100: self.kill()