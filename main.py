import pygame
import random

gamerules = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors']
}


class rps_Sprites(pygame.sprite.Sprite):
    def __init__(self, choice):
        super().__init__()
        self.choice = choice
        self.image = pygame.transform.scale(pygame.image.load(f'{choice}.png'), (40, 40))
        self.rect = self.image.get_rect()
        self.speed_x = random.randint(-3, 3)
        self.speed_y = random.randint(-3, 3)
        if self.speed_x == 0:
            self.speed_x += random.choice([-1, 1])
        elif self.speed_y == 0:
            self.speed_y += random.choice([-1, 1])

    def move(self):
        self.rect = self.rect.move(self.speed_x, self.speed_y)
        if self.rect.left < 0:
            self.speed_x *= -1
            self.rect.left = 1
        elif self.rect.right > screen_width:
            self.speed_x *= -1
            self.rect.right = screen_width - 1
        if self.rect.top < 0:
            self.speed_y *= -1
            self.rect.top = 1
        elif self.rect.bottom > screen_height:
            self.speed_y *= -1
            self.rect.bottom = screen_height - 1

    def draw(self):
        screen.blit(self.image, self.rect)

    def spawn_sprite(self, sprites):
        self.rect.x = random.randint(40, screen_width - 40)
        self.rect.y = random.randint(40, screen_height - 40)
        for j in sprites:
            if pygame.sprite.collide_rect(self, j):
                self.rect.x = j.rect.x + 40
                self.rect.y = j.rect.y + 40

    def convert(self, new_choice):
        self.choice = new_choice
        self.image = pygame.transform.scale(pygame.image.load(f'{new_choice}.png'), (40, 40))


def check_collide(sprite1, sprite2):
    if pygame.sprite.collide_rect(sprite1, sprite2):
        temp_x, temp_y = sprite1.speed_x, sprite1.speed_y
        sprite1.speed_x, sprite1.speed_y = sprite2.speed_x, sprite2.speed_y
        sprite2.speed_x, sprite2.speed_y = temp_x, temp_y

        if sprite1.choice in gamerules[sprite2.choice]:
            sprite1.convert(sprite2.choice)
        elif sprite2.choice in gamerules[sprite1.choice]:
            sprite2.convert(sprite1.choice)


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.set_volume(0.03)
pygame.mixer.music.play(-1)
screen_width = 500
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('background.jpg')
clock = pygame.time.Clock()

pieces = pygame.sprite.Group()
for i in range(random.randrange(3, 8)):
    new_rock = rps_Sprites('rock')
    new_rock.spawn_sprite(pieces)
    pieces.add(new_rock)

for i in range(random.randrange(3, 8)):
    new_paper = rps_Sprites('paper')
    new_paper.spawn_sprite(pieces)
    pieces.add(new_paper)

for i in range(random.randrange(3, 8)):
    new_scissors = rps_Sprites('scissors')
    new_scissors.spawn_sprite(pieces)
    pieces.add(new_scissors)

for i in range(random.randrange(3, 8)):
    new_lizard = rps_Sprites('lizard')
    new_lizard.spawn_sprite(pieces)
    pieces.add(new_lizard)

for i in range(random.randrange(3, 8)):
    new_spock = rps_Sprites('spock')
    new_spock.spawn_sprite(pieces)
    pieces.add(new_spock)

running = True
while running:
    screen.blit(background, (0, 0))
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
    pygame.display.flip()

pygame.quit()
