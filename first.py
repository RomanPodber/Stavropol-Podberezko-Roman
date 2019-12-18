import pygame
import random

pygame.init()

size = witdhn, height = 1920, 1080

screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))

clock = pygame.time.Clock()

def load_image(name, colorkey=None):
    img = pygame.image.load(name)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = img.get_at((0, 0))
        img.set_colorkey(colorkey)
    else:
        img = img.convert_alpha()
    return img


all_sprites = pygame.sprite.Group()

sprite = pygame.sprite.Sprite()
all_sprites.add(sprite)

class Ball(pygame.sprite.Sprite):
    def __init__(self, all_sprites, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color('red'), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randint(-5, 5)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx

class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)

        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)

all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

pos = 0, 0
running = True

Border(5, 5, witdhn - 5, 5)
Border(5, height - 5, witdhn - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(witdhn - 5, 5, witdhn - 5, height - 5)
for i in range(10):
    Ball(all_sprites, 20, 100, 100)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    Ball(all_sprites, 100, 100, 100)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(100)
pygame.quit()
