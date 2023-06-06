import pygame, random

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ALIEN_SIZE = (30, 40)
ALIEN_SPACER = 20
BARRIER_ROW = 10
BARRIER_COLUMN = 4
BULLET_SIZE = (5, 10)
MISSILE_SIZE = (5, 5)
BLOCK_SIZE = (10, 10)
RES = (800, 600)

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = (60, 55)
        self.rect = self.image.get_rect()
        self.rect.x = (RES[0] / 2) - (self.size[0] / 2)
        self.rect.y = 520
        self.travel = 7
        self.speed = 350
        self.time = pygame.time.get_ticks()

    def update(self):
        self.rect.x += GameState.vector * self.travel
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > RES[0] - self.size[0]:
            self.rect.x = RES[0] - self.size[0]
            
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = (ALIEN_SIZE)
        self.rect = self.image.get_rect()
        self.has_moved = [0, 0]
        self.vector = [1, 1]
        self.travel = [(ALIEN_SIZE[0] - 7), ALIEN_SPACER]
        self.speed = 700
        self.time = pygame.time.get_ticks()

    def update(self):
        if GameState.alien_time - self.time > self.speed:
            if self.has_moved[0] < 12:
                self.rect.x += self.vector[0] * self.travel[0]
                self.has_moved[0] +=1
            else:
                if not self.has_moved[1]:
                    self.rect.y += self.vector[1] * self.travel[1]
                self.vector[0] *= -1
                self.has_moved = [0, 0]
                self.speed -= 20
                if self.speed <= 100:
                    self.speed = 100
            self.time = GameState.alien_time
            
class Ammo(pygame.sprite.Sprite):
    def __init__(self, color, (width, height)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = 0
        self.vector = 0
    def update(self):
        self.rect.y += self.vector * self.speed
        if self.rect.y < 0 or self.rect.y > RES[1]:
            self.kill()
class Block(pygame.sprite.Sprite):
    def __init__(self, color, (width, height)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
class GameState:
    pass

class Game(object):
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.Font(
        ‘data/Orbitracer.ttf’, 28)
        self.intro_font = pygame.font.Font(
        ‘data/Orbitracer.ttf’, 72)
        self.screen = pygame.display.set_mode([RES[0], RES[1]])
        self.time = pygame.time.get_ticks()
        self.refresh_rate = 20
        self.rounds_won = 0
        self.level_up = 50
        self.score = 0
        self.lives = 2
        self.player_group = pygame.sprite.Group()
        self.alien_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.missile_group = pygame.sprite.Group()
        self.barrier_group = pygame.sprite.Group()
        self.all_sprite_list = pygame.sprite.Group()
        self.intro_screen = pygame.image.load(‘data/start_screen.jpg’).convert()
        self.background = pygame.image.load(‘data/Space-Background.jpg’).convert()
        pygame.display.set_caption(‘Pivaders - ESC to exit’)
        pygame.mouse.set_visible(False)
        Player.image = pygame.image.load(
        ‘data/ship.png’).convert()
        Player.image.set_colorkey(BLACK)
        Alien.image = pygame.image.load(
        ‘data/Spaceship16.png’).convert()
        Alien.image.set_colorkey(WHITE)
        GameState.end_game = False
        GameState.start_screen = True
        GameState.vector = 0
        GameState.shoot_bullet = False
        
def control(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameState.start_screen = False
            GameState.end_game = True
        if event.type == pygame.KEYDOWN \and event.key == pygame.K_ESCAPE:
            if GameState.start_screen:
                GameState.start_screen = False
                GameState.end_game = True
                self.kill_all()
            else:
                GameState.start_screen = True
    self.keys = pygame.key.get_pressed()
    if self.keys[pygame.K_LEFT]:
        GameState.vector = -1
    elif self.keys[pygame.K_RIGHT]:
        GameState.vector = 1
    else:
        GameState.vector = 0
    if self.keys[pygame.K_SPACE]:
        if GameState.start_screen:
            GameState.start_screen = False
            self.lives = 2
            self.score = 0
            self.make_player()
            self.make_defenses()
            self.alien_wave(0)
        else:
            GameState.shoot_bullet = True
            
def splash_screen(self):
    while GameState.start_screen:
        self.kill_all()
        self.screen.blit(self.intro_screen, [0, 0])
        self.screen.blit(self.intro_font.render(
        “PIVADERS”, 1, WHITE), (265, 120))
        self.screen.blit(self.game_font.render(
        “PRESS SPACE TO PLAY”, 1, WHITE), (274, 191))