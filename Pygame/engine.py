import pygame
import Configuration as config
import context

def display_score(start_time):
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    context.text_score_surface = context.test_font.render(
                        "Scores: " + f'{current_time}', False, "Green")
    context.text_score_rect = context.text_score_surface.\
                                get_rect(center= 
                                  (config.FONT_POS_X, config.FONT_SIZE))
    return current_time

def obstacle_collision_sprite():
    if pygame.sprite.spritecollide(context.player.sprite,context.obstacle_group,False):
        context.obstacle_group.empty()
        return True
    else: return False

def coin_collision_sprite():
    coin_hit_list = pygame.sprite.spritecollide(\
                    context.player.sprite,context.coins_group, True)
    return len(coin_hit_list)

def render_life(life):
    context.text_life_surface = context.test_font.render(
                        "Life: " + f'{life}', False, "Green")
    context.text_life_rect = context.text_life_surface.\
                            get_rect(center= (config.FONT_POS_X, config.FONT_SIZE*2)) 
    
def render_enemies(enemies): 
    context.test_enemies_surface = context.test_font.render(f"Enemies: {enemies}", False, "Red")
    context.text_enemies_rect = context.test_enemies_surface.get_rect(center= (config.FONT_POS_X, config.FONT_SIZE * 4))

def render_levels(levels): 
    context.levels_surface = context.test_font.render(f"Level {levels}", False, "Red")
    context.levels_surface = pygame.transform.scale(context.levels_surface, (400, 50))
    context.levels_rect = context.levels_surface.get_rect(center = (400, 100))

def add_coin_score(start_time, hit_score):
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    current_time += hit_score*10
    context.text_score_surface = context.test_font.render(
                "Scores: " + f'{current_time}', False, "Green")

    context.text_score_rect = context.text_score_surface.get_rect(
                                    center = (config.FONT_POS_X, config.FONT_SIZE))
    return current_time