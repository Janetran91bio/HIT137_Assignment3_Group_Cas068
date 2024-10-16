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
pygame.display.set_caption("Zod Runner")
clock = pygame.time.Clock()

game_over = False
push_obstacle = False
start_time = 0
score = 0
hit_score = 0
life = 2
levels = 4
current_level = 1
current_enemies = 0
enemies_level = [10, 12, 15]

# background music
# bg_music = pygame.mixer.Sound('images/bg.mp3')
# bg_music.play(loops = -1)
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 800)

def game_over_render(life = 0):
    screen.blit(context.background_surface, (0,0))
    screen.blit(context.game_over_surface, context.game_over_rect)
    if life == 0:
        screen.blit(context.player_dead_surface, context.player_dead_rect)
    screen.blit(context.restart_surface, context.restart_rect)

    engine.render_life(life)
    screen.blit(context.text_score_surface, context.text_score_rect)
    screen.blit(context.text_life_surface, context.text_life_rect)
    # screen.blit(context.levels_surface, context.levels_rect)
    # screen.blit(context.test_enemies_surface, context.text_enemies_rect)
    return 0, 0

def game_render(start_time, life, hit_score):
    # print(f"Hello: ${len(context.obstacle_group)}")
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
    screen.blit(context.levels_surface, context.levels_rect)
    # screen.blit(context.test_enemies_surface, context.text_enemies_rect)

    is_game_over = False
    if collision: 
        life -= 1
        if life == 0: is_game_over = True
        else: pygame.time.delay(1000)

    return is_game_over, score, life, hit_score

def render_levels(levels):
    engine.render_levels(levels)
    screen.blit(context.levels_surface, context.levels_rect)

while current_level <= levels:
    # engine.render_enemies(current_enemies)
    engine.render_levels(current_level)
    # render_levels(current_level)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_over == True:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_time = pygame.time.get_ticks() // 1000
                game_over, life, hit_score, current_level, current_enemies = False, 2, 0, 1, 0
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                start_time = pygame.time.get_ticks() // 1000
                game_over, life, hit_score, current_level, current_enemies = False, 2, 0, 1, 0
        else:
            if event.type == obstacle_timer:
                
                if push_obstacle and current_enemies <= enemies_level[current_level - 1]:
                    if current_enemies == enemies_level[current_level - 1]:
                        context.obstacle_group.add(Enemy(4))
                    else:
                        context.obstacle_group.add(Enemy(choice([1,1,1,2,2,2,2,3,3,3,3])))
                    current_enemies = current_enemies + 1
                    push_obstacle = False
                    if current_enemies > enemies_level[current_level - 1]:
                        current_enemies = 0
                        current_level = current_level + 1
                        if current_level == levels:
                            game_over = True
                            pygame.time.delay(1000)
                else:
                    type = choice([1,2])
                    for i in range(randint(1,4)):
                        context.coins_group.add(Collectible(type, i))
                    push_obstacle = True
    # print(f"Hello: ${len(context.obstacle_group)}")
    if game_over == True:
        score = game_over_render(life)
    else:
        game_over, score, life, hit_score = game_render(start_time, life, hit_score)

    pygame.display.update()
    clock.tick(60)
