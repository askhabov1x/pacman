import pygame
from settings import *
from wall import Wall
from player import Player
from ghost import Ghost

class Game:
    def __init__(self, level_file):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.load_level(level_file)

    def load_level(self, level_file):
        """Загрузка уровня из текстового файла"""
        self.walls = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        with open(level_file) as f:
            for row, line in enumerate(f):
                for col, char in enumerate(line.strip()):
                    x, y = col * TILE_SIZE, row * TILE_SIZE
                    if char == "X":
                        wall = Wall(x, y)
                        self.walls.add(wall)
                        self.all_sprites.add(wall)
                    elif char == "P":
                        self.player = Player(x, y)
                        self.all_sprites.add(self.player)
                    elif char == "G":
                        ghost = Ghost(x, y)
                        self.ghosts.add(ghost)
                        self.all_sprites.add(ghost)

    def run(self):
        """Главный игровой цикл"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def handle_events(self):
        """Обработка событий (выход из игры)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """Обновление объектов"""
        keys = pygame.key.get_pressed()
        self.player.update(self.walls, keys)
        self.ghosts.update(self.walls)

    def draw(self):
        """Отрисовка объектов"""
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()