import pygame
import random
from settings import TILE_SIZE, RED

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2
        # Начальное случайное направление: вправо, влево, вниз или вверх
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        self.move_counter = 0
        # Интервал, через который направление меняется (в кадрах)
        self.change_direction_interval = random.randint(30, 60)

    def update(self, walls):
        # Увеличиваем счетчик движения
        self.move_counter += 1
        # Если истек интервал, выбираем новое случайное направление
        if self.move_counter >= self.change_direction_interval:
            self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            self.move_counter = 0
            self.change_direction_interval = random.randint(30, 60)

        dx = self.direction[0] * self.speed
        dy = self.direction[1] * self.speed

        # Перемещение по оси X
        self.rect.x += dx
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.x -= dx  # откат при столкновении
            # Выбираем новое случайное направление
            self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

        # Перемещение по оси Y
        self.rect.y += dy
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.y -= dy  # откат при столкновении
            self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])