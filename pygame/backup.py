import pygame
import Configuration as config

import context
from Enemy import Enemy
from Collectible import Collectible

import engine
from sys import exit
from random import choice,randint

pygame.init()
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Mario Runner")
clock = pygame.time.Clock()

game_over = False
push_obstacle = False
start_time = 0
score = 0
hit_score = 0
life = 2

# background music
# bg_music = pygame.mixer.Sound('images/bg.mp3')
# bg_music.play(loops = -1)
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 800)

def game_over_render(life = 0):
    screen.blit(context.background_surface, (0,0))
    screen.blit(context.game_over_surface, context.game_over_rect)
    screen.blit(context.player_dead_surface, context.player_dead_rect)
    screen.blit(context.restart_surface, context.restart_rect)

    engine.render_life(life)
    screen.blit(context.text_score_surface, context.text_score_rect)
    screen.blit(context.text_life_surface, context.text_life_rect)
    return 0, 0

def game_render(start_time, life, hit_score):
    screen.blit(context.background_surface, (0,0))

    # Player
    context.player.draw(screen)
    context.player.update()

    # obstacles
    context.obstacle_group.draw(screen)
    context.obstacle_group.update()

    # Coins
    context.coins_group.draw(screen)
    context.coins_group.update()

    collision = engine.obstacle_collision_sprite()
    
    hit_score += engine.coin_collision_sprite()

    score = engine.add_coin_score(start_time, hit_score)
    engine.render_life(life)
    screen.blit(context.text_score_surface, context.text_score_rect)
    screen.blit(context.text_life_surface, context.text_life_rect)

    is_game_over = False
    if collision: 
        life -= 1
        if life == 0: is_game_over = True
        else: pygame.time.delay(1000)

    return is_game_over, score, life, hit_score

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_over == True:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_time = pygame.time.get_ticks() // 1000
                game_over, life, hit_score = False, 2 , 0
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                start_time = pygame.time.get_ticks() // 1000
                game_over, life, hit_score = False, 2 , 0
        else:
            if event.type == obstacle_timer:
                if push_obstacle:
                    context.obstacle_group.add(Enemy(choice([1,1,1,2,2,2,2,3,3,3,3])))
                    push_obstacle = False
                else:
                    type = choice([1,2])
                    for i in range(randint(1,4)):
                        context.coins_group.add(Collectible(type,i))
                    push_obstacle = True

    if game_over == True:
        score = game_over_render()
    else:
        game_over, score, life, hit_score = game_render(start_time, life, hit_score)

    pygame.display.update()
    clock.tick(60)
