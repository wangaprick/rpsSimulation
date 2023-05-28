import pygame
import random

pygame.init()

screen_width = 540
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


class rock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('rock.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width)
        self.rect.y = random.randint(0, screen_height)
        self.speed_x = random.randint(-3, 3)
        self.speed_y = random.randint(-3, 3)

    def move(self):
        self.rect = self.rect.move(self.speed_x, self.speed_y)
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x = self.speed_x * -1
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.speed_y = self.speed_y * -1

    def draw(self):
        screen.blit(self.image, self.rect)


rock1 = rock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(30)
    rock1.move()

    screen.fill((0, 0, 0))

    rock1.draw()

    pygame.display.update()
