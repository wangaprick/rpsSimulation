import pygame
import random


class rps_Sprites(pygame.sprite.Sprite):
    def __init__(self, choice):
        super().__init__()
        self.choice = choice
        self.image = pygame.transform.scale(pygame.image.load(f'{choice}.png'), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(30, screen_width - 30)
        self.rect.y = random.randint(30, screen_height - 30)
        self.speed_x = random.randint(-3, 3)
        self.speed_y = random.randint(-3, 3)

    def move(self):
        self.rect = self.rect.move(self.speed_x, self.speed_y)
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.speed_y *= -1

    def draw(self):
        screen.blit(self.image, self.rect)

    def convert(self, new_choice):
        self.choice = new_choice
        self.image = pygame.transform.scale(pygame.image.load(f'{new_choice}.png'), (30, 30))


def check_collide(sprite1, sprite2):
    if pygame.sprite.collide_rect(sprite1, sprite2):
        temp_x, temp_y = sprite1.speed_x, sprite1.speed_y
        sprite1.speed_x, sprite1.speed_y = sprite2.speed_x, sprite2.speed_y
        sprite2.speed_x, sprite2.speed_y = temp_x, temp_y

        if sprite1.choice == 'rock' and sprite2.choice == 'scissors':
            sprite2.convert('rock')
        elif sprite1.choice == 'scissors' and sprite2.choice == 'rock':
            sprite1.convert('rock')
        elif sprite1.choice == 'paper' and sprite2.choice == 'rock':
            sprite2.convert('paper')
        elif sprite1.choice == 'rock' and sprite2.choice == 'paper':
            sprite1.convert('paper')
        elif sprite1.choice == 'scissors' and sprite2.choice == 'paper':
            sprite2.convert('scissors')
        elif sprite1.choice == 'paper' and sprite2.choice == 'scissors':
            sprite1.convert('scissors')


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.set_volume(0.03)
pygame.mixer.music.play(-1)
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

pieces = pygame.sprite.Group()
for i in range(random.randrange(2, 8)):
    new_rock = rps_Sprites('rock')
    pieces.add(new_rock)

for i in range(random.randrange(2, 8)):
    new_paper = rps_Sprites('paper')
    pieces.add(new_paper)

for i in range(random.randrange(2, 8)):
    new_scissors = rps_Sprites('scissors')
    pieces.add(new_scissors)

running = True
while running:
    screen.fill((255, 229, 229))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pieces.draw(screen)
    for i in pieces:
        i.move()
        for j in pieces:
            if i != j:
                check_collide(i, j)

    clock.tick(30)
    pygame.display.update()

pygame.quit()
