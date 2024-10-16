import pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

from random import randint, choice 
import Configuration as config

from Player import Player

WIDTH = config.WIDTH
HEIGHT = config.HEIGHT
FONT_SIZE= config.FONT_SIZE
FONT_POS_X = config.FONT_POS_X
COIN_SIZE = config.COIN_SIZE
SKY_LEVEL = config.SKY_LEVEL
PLAYER_SIZE = config.PLAYER_SIZE
GROUND_LEVEL = config.GROUND_LEVEL
CHAR_DEAD_SIZE = config.CHAR_DEAD_SIZE


# Background
background_img_path = 'images/backg.jpg'
background_surface  = pygame.image.load(background_img_path)
background_surface  = pygame.transform.scale(background_surface,
                                                (WIDTH, HEIGHT))

# obstacles  
obstacle_group = pygame.sprite.Group()

# Player
player = pygame.sprite.GroupSingle()
player.add(Player())

# Coins 
coins_group = pygame.sprite.Group()

# Texts
font_path = 'fonts/Pixeltype.ttf'
test_font = pygame.font.Font(font_path, FONT_SIZE)

text_score_surface = test_font.render("Scores: ", False, "Green")
text_score_rect    = text_score_surface.get_rect(center= (FONT_POS_X, FONT_SIZE))

levels_surface = test_font.render("Level 1", False, "Red")
levels_surface = pygame.transform.scale(levels_surface, (400, 50))
levels_rect = levels_surface.get_rect(center = (400, 100))

test_enemies_surface = test_font.render("Enemies: ", False, "Red")
text_enemies_rect = test_enemies_surface.get_rect(center = (FONT_POS_X, FONT_SIZE * 4))

text_life_surface = test_font.render("Life: ", False, "Green")
text_life_rect = text_score_surface.get_rect(center = (FONT_POS_X, FONT_SIZE*2))

# Coins
coin_path = 'images/coin.png'
coin_surface = pygame.image.load(coin_path)
coin_surface = pygame.transform.scale(coin_surface, (COIN_SIZE, COIN_SIZE))
coin_rect    = coin_surface.get_rect(center=(200, SKY_LEVEL))


# Game Over State Components
game_over_path = 'images/gameOver.png'
game_over_surface = pygame.image.load(game_over_path)
game_over_surface = pygame.transform.scale(game_over_surface, (400, 50))
game_over_rect = game_over_surface.get_rect(center=(400, 100))

player_dead_path = 'images/char_dead.png'
player_dead_surface = pygame.image.load(player_dead_path)
player_dead_surface = pygame.transform.scale(player_dead_surface, 
                                                    (CHAR_DEAD_SIZE, CHAR_DEAD_SIZE))
player_dead_rect    = player_dead_surface.get_rect(midbottom=(100, GROUND_LEVEL))


restart_path = 'images/restart.png'
restart_surface = pygame.image.load(restart_path)
restart_surface = pygame.transform.scale(restart_surface, (80, 80))
restart_rect = restart_surface.get_rect(center=(400,220))