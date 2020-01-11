import sys
import pygame

pygame.init()
pygame.key.set_repeat(200, 70)

tank_left = False
tank_right = False
tank_up = False
tank_down = False
shoot = False

FPS = 60
WIDTH = 800
HEIGHT = 800
STEP = 10

move = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
brick = pygame.sprite.Group()
bullet = pygame.sprite.Group()

def load_image(name, color_key=None):
    image = pygame.image.load(name)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image

def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))

def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile(x, y)
            elif level[y][x] == 'x':
                Brick(x, y)
            elif level[y][x] == '@':
                Tile(x, y)
                new_player = Player(x, y)
    return new_player, x, y

def terminate():
    pygame.quit()
    sys.exit()

tile_images = {'wall': load_image('brick.jpg'), 'empty': load_image('black.jpg')}
player_image = load_image('tnk.png')

tile_width = tile_height = 40

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images['empty']
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Brick(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(brick, all_sprites)
        self.image = tile_images['wall']
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)


class Bullet(pygame.sprite.Sprite):
    image = load_image('goodbullet2.png')
    def __init__(self, x, y):
        super().__init__(bullet, all_sprites)
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x + 10
        self.rect.y = y + 10

    def update(self):
        global tank_down
        global tank_up
        global tank_left
        global tank_right

        if tank_down:
            box = []
            if self.rect.y <= 810:
                self.rect = self.rect.move(0, 5)
            elif self.rect.y > 810:
                for bull in bullet:
                    box.append(bull)
                bullet.remove(box[0])

        if tank_up:
            box = []
            if self.rect.y >= -10:
                self.rect = self.rect.move(0, -5)
            if self.rect.y < - 10:
                for bull in bullet:
                    box.append(bull)
                if pygame.sprite.spritecollideany(self, brick):
                    bullet.remove(box[0])
                bullet.remove(box[0])

        if tank_right:
            box = []
            if self.rect.x <= 810:
                self.rect = self.rect.move(5, 0)
            elif self.rect.y > 810:
                for bull in bullet:
                    box.append(bull)
                bullet.remove(box[0])

        if tank_left:
            box = []
            if self.rect.x >= -10:
                self.rect = self.rect.move(-5, 0)
                if pygame.sprite.spritecollideany(self, brick):
                    print('da')
            elif self.rect.x < - 10:
                for bull in bullet:
                    box.append(bull)
                bullet.remove(box[0])

player, level_x, level_y = generate_level(load_level("firstlevell.txt"))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if move:
                    tank_left = True
                    tank_right = False
                    tank_up = False
                    tank_down = False
                    player.image = load_image('tnk4.png')
                    player.rect.x -= STEP

            if event.key == pygame.K_RIGHT:
                tank_right = True
                tank_down = False
                tank_up = False
                tank_left = False
                player.image = load_image('tnk2.png')
                player.rect.x += STEP

            if event.key == pygame.K_UP:
                tank_up = True
                tank_down = False
                tank_left = False
                tank_right = False
                player.image = load_image('tnk.png')
                player.rect.y -= STEP

            if event.key == pygame.K_DOWN:
                tank_down = True
                tank_right = False
                tank_up = False
                tank_left = False
                player.image = load_image('tnk3.png')
                player.rect.y += STEP

            if event.key == pygame.K_SPACE:
                shoot = True
                x, y = player.rect.x, player.rect.y
                Bullet(x, y)


    screen.fill(pygame.Color(0, 0, 0))
    tiles_group.draw(screen)
    brick.draw(screen)
    brick.update()
    bullet.draw(screen)
    if shoot:
        bullet.update()
    player_group.draw(screen)
    player_group.update()
    pygame.display.flip()
    clock.tick(FPS)

terminate()
