import pygame
import Configuration as config

PLAYER_SIZE = config.PLAYER_SIZE
GROUND_LEVEL = config.GROUND_LEVEL
INIT_GRAVITY = config.INIT_GRAVITY

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img_1_path  = 'images/Char-1.png'
        img_2_path  = 'images/Char-2.png'
        img_3_path  = 'images/Char-3.png'
        img_4_path  = 'images/Char-4.png'

        self.player_img_list = [img_1_path, img_2_path, img_3_path, img_4_path]
        self.player_index = 0
        player_surface = pygame.image.load(self.player_img_list[self.player_index])

        self.image = pygame.transform.scale(player_surface,(PLAYER_SIZE,PLAYER_SIZE))
        self.rect = self.image.get_rect(midbottom=(100,GROUND_LEVEL))

        # self.jump_sound = pygame.mixer.Sound('images/jump.mp3')
        # self.jump_sound.set_volume(0.5)
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= GROUND_LEVEL:
            self.gravity = INIT_GRAVITY
            # self.jump_sound.play()
        
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y  += self.gravity
        if self.rect.bottom >= GROUND_LEVEL:
            self.rect.bottom = GROUND_LEVEL
        
    def player_animation(self):
        self.player_index += 0.1
        if self.player_index >= len(self.player_img_list):
            self.player_index = 0

        player_surface = pygame.image.load(self.player_img_list[int(self.player_index)])
        self.image = pygame.transform.scale(player_surface,(PLAYER_SIZE,PLAYER_SIZE))

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.player_animation()