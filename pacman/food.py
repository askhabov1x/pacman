import pygame
from settings import WHITE, FOOD_SIZE

class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((FOOD_SIZE, FOOD_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

def create_foods(maze_layout):
    foods = pygame.sprite.Group()
    for row, line in enumerate(maze_layout):
        for col, char in enumerate(line):
            if char == " ":
                food = Food(col * 20 + 5, row * 20 + 5)
                foods.add(food)
    return foods