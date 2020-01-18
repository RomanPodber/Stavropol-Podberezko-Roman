import sys
import pygame
import random

pygame.init()
pygame.key.set_repeat(200, 70)


win = False
shoot_enemy = False
tank_left = False
tank_right = False
tank_up = False
tank_down = False
shoot = False
back = False
da = False
lvl = 'firstlevell.txt'
remark = False
first = True
sec = False
thrd = False
fou = False
fifth = False
ending = False
dead = False

count1 = 0
count2 = 0
count3 = 0
count4 = 0

FPS = 120
WIDTH = 800
HEIGHT = 800
STEP = 4
DAMAGE = 30

move = True

menu = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
bricks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
enemybullets = pygame.sprite.Group()
first = False

box = []

class Menu:
    def __init__(self, event):
        self.event = event

level = pygame.display.set_mode()

def load_image(name, color_key=None):
    image = pygame.image.load(name)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image

screen = pygame.display.set_mode((WIDTH, HEIGHT))
main_menu = load_image('fon.png')

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
            elif level[y][x] == 'U':
                Tile(x, y)
                Respawn(x, y, 'u')
                box.append((x, y))
            elif level[y][x] == 'R':
                Tile(x, y)
                Respawn(x, y, 'r')
                box.append(((x, y)))
            elif level[y][x] == 'L':
                Tile(x, y)
                Respawn(x, y, 'l')
                box.append(((x, y)))
            elif level[y][x] == 'D':
                Tile(x, y)
                Respawn(x, y, 'd')
                box.append(((x, y)))
            elif level[y][x] == '?':
                Tile(x, y)
                screen.blit(load_image('que.png'), (x, y))

    return new_player, x, y

def terminate():
    pygame.quit()
    sys.exit()

tile_images = {'wall': load_image('brick.jpg'), 'empty': load_image('grass.png')}
player_image = load_image('tnk.png')

tile_width = tile_height = 40

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images['empty']
        self.rect = self.image.get_rect().move(tile_width * x, tile_height * y)

class Respawn(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__(enemies)
        self.type = type
        self.image = load_image('enemy2_4.png')
        self.box = [1, 2, 3]
        self.chose = random.choice(self.box)
        self.flag = 0
        self.rect = self.image.get_rect()
        self.x = 2
        self.rect.x = tile_width * x
        self.rect.y = tile_height * y
        self.hp1 = 100
        self.hp2 = 200
        self.hp3 = 300
        if self.chose == 1:
            if self.type == 'u':
                self.image = load_image('enemy2_4.png')
                self.flag = 1
            elif self.type == 'd':
                self.image = load_image('enemy2_2.png')
                self.flag = 2
            elif self.type == 'l':
                self.image = load_image('enemy2_3.png')
                self.flag = 3
            elif self.type == 'r':
                self.image = load_image('enemy2_1.png')
                self.flag = 4

        elif self.chose == 2:
            if self.type == 'u':
                self.image = load_image('enemy1_4.png')
                self.flag = 1
            elif self.type == 'd':
                self.image = load_image('enemy1_2.png')
                self.flag = 2
            elif self.type == 'l':
                self.image = load_image('enemy1_3.png')
                self.flag = 3
            elif self.type == 'r':
                self.image = load_image('enemy1_1.png')
                self.flag = 4

        elif self.chose == 3:
            if self.type == 'u':
                self.image = load_image('enemy3_4.png')
                self.flag = 1
            elif self.type == 'd':
                self.image = load_image('enemy3_2.png')
                self.flag = 2
            elif self.type == 'l':
                self.image = load_image('enemy3_3.png')
                self.flag = 3
            elif self.type == 'r':
                self.image = load_image('enemy3_1.png')
                self.flag = 4

    def update(self):
        global count1
        global first
        global count2
        global count4
        global count3
        global sec
        global thrd
        global fou
        if self.chose == 1:
            if self.flag == 1:
                if self.rect.bottom >= 800 or pygame.sprite.spritecollideany(self, bricks):
                    self.rect.bottom -= 3
                    box = [2, 3, 4]
                    choice = random.choice(box)
                    self.flag = choice
                else:
                    self.rect.bottom += 3
                    self.image = load_image('enemy2_1.png')

            elif self.flag == 2:
                if self.rect.top <= 0 or pygame.sprite.spritecollideany(self, bricks):
                    self.rect.top += 3
                    box = [1, 3, 4]
                    choice = random.choice(box)
                    self.flag = choice
                else:
                    self.rect.top -= 3
                    self.image = load_image('enemy2_2.png')

            elif self.flag == 3:
                if self.rect.right >= 800 or pygame.sprite.spritecollideany(self, bricks):
                    self.rect.right -= 3
                    box = [1, 2, 4]
                    choice = random.choice(box)
                    self.flag = choice
                else:
                    self.rect.right += 3
                    self.image = load_image('enemy2_3.png')

            elif self.flag == 4:
                if self.rect.left <= 0 or pygame.sprite.spritecollideany(self, bricks):
                    self.rect.left += 3
                    box = [1, 2, 3]
                    choice = random.choice(box)
                    self.flag = choice
                else:
                    self.rect.left -= 3
                    self.image = load_image('enemy2_4.png')

            if pygame.sprite.spritecollideany(self, bullets):
                self.hp2 -= DAMAGE
                if self.hp2 <= 0:
                    self.kill()
                    self.hp2 = 100
                    if lvl == 'firstlevell.txt':
                        count1 += 1
                        if count1 == 4:
                            first = True
                            count1 =0
                    elif lvl == 'secondlevell.txt':
                        count2 += 1
                        if count2 == 7:
                            sec = True
                            count2 = 0
                    elif lvl == 'thirdlevell.txt':
                        count3 += 1
                        if count3 == 9:
                            thrd = True
                            count3 = 0
                    elif lvl == 'fourthlevell.txt':
                        count4 += 1
                        if count4 == 9:
                            fou = True
                            count4 = 0

        elif self.chose == 2:
            if self.flag == 1:
                if self.rect.bottom >= 800 or pygame.sprite.spritecollideany(self, bricks):
                    self.rect.bottom -= 2
                    box = [2, 3, 4]
                    choice = random.choice(box)
                    self.flag = choice
                else:
                    self.rect.bottom += 2
                    self.image = load_image('enemy1_1.png')

            elif self.flag == 2:
                if self.rect.top <= 0 or pygame.sprite.spritecollideany(self, bricks):
                    self.rect.top += 2
                    box = [1, 3, 4]
                    choice = random.choice(box)
                    self.flag = choice
                else:
                    self.rect.top -= 2
                    self.image = load_image('enemy1_2.png')

            elif self.flag == 3:
                if self.rect.right >= 800 or pygame.sprite.spritecollideany(self, bricks):
                    self.rect.right -= 2
                    box = [1, 2, 4]
                    choice = random.choice(box)
                    self.flag = choice
                else:
                    self.rect.right += 2
                    self.image = load_image('enemy1_3.png')

            elif self.flag == 4:
                if self.rect.left <= 0 or pygame.sprite.spritecollideany(self, bricks):
                    self.rect.left += 2
                    box = [1, 2, 3]
                    choice = random.choice(box)
                    self.flag = choice
                else:
                    self.rect.left -= 2
                    self.image = load_image('enemy1_4.png')

            if pygame.sprite.spritecollideany(self, bullets):
                self.hp2 -= DAMAGE
                if self.hp2 <= 0:
                    self.kill()
                    self.hp2 = 200
                    if lvl == 'firstlevell.txt':
                        count1 += 1
                        if count1 == 4:
                            first = True
                            count1 = 0
                    elif lvl == 'secondlevell.txt':
                        count2 += 1
                        if count2 == 7:
                            sec = True
                            count2 = 0

                    elif lvl == 'thirdlevell.txt':
                        count3 += 1
                        if count3 == 9:
                            thrd = True
                            count3 = 0
                    elif lvl == 'fourthlevell.txt':
                        count4 += 1
                        if count4 == 9:
                            fou = True
                            count4 = 0

        if self.chose == 3:
            if self.flag == 1:
                if self.rect.bottom >= 800 or pygame.sprite.spritecollideany(self, bricks):
                    self.rect.bottom -= 1
                    box = [2, 3, 4]
                    choice = random.choice(box)
                    self.flag = choice
                else:
                    self.rect.bottom += 1
                    self.image = load_image('enemy3_1.png')

            elif self.flag == 2:
                if self.rect.top <= 0 or pygame.sprite.spritecollideany(self, bricks):
                    self.rect.top += 1
                    box = [1, 3, 4]
                    choice = random.choice(box)
                    self.flag = choice
                else:
                    self.rect.top -= 1
                    self.image = load_image('enemy3_2.png')

            elif self.flag == 3:
                if self.rect.right >= 800 or pygame.sprite.spritecollideany(self, bricks):
                    self.rect.right -= 1
                    box = [1, 2, 4]
                    choice = random.choice(box)
                    self.flag = choice
                else:
                    self.rect.right += 1
                    self.image = load_image('enemy3_3.png')

            elif self.flag == 4:
                if self.rect.left <= 0 or pygame.sprite.spritecollideany(self, bricks):
                    self.rect.left += 1
                    box = [1, 2, 3]
                    choice = random.choice(box)
                    self.flag = choice
                else:
                    self.rect.left -= 1
                    self.image = load_image('enemy3_4.png')

            if pygame.sprite.spritecollideany(self, bullets):
                self.hp3 -= DAMAGE
                if self.hp3 <= 0:
                    self.kill()
                    self.hp3 = 300
                    if lvl == 'firstlevell.txt':
                        count1 += 1
                        if count1 == 4:
                            first = True
                            count1 = 0
                    elif lvl == 'secondlevell.txt':
                        count2 += 1
                        if count2 == 7:
                            sec = True
                            count2 = 0
                    elif lvl == 'thirdlevell.txt':
                        count3 += 1
                        if count3 == 9:
                            thrd = True
                            count3 = 0
                    elif lvl == 'fourthlevell.txt':
                        count4 += 1
                        if count4 == 9:
                            fou = True
                            count4 = 0


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(bricks)
        self.image = tile_images['wall']
        self.rect = self.image.get_rect().move(tile_width * x, tile_height * y)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(player_group)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * x, tile_height * y)
        self.hp = 100

    def update(self):
        global dead
        if move:
            if tank_up:
                self.rect.top -= STEP
                if pygame.sprite.spritecollideany(self, bricks) or pygame.sprite.spritecollideany(self, enemies) or \
                        self.rect.top <= 0:
                    self.rect.top += STEP
                else:
                    self.rect.top += 0
                self.image = load_image('tnk.png')

            if tank_left:
                self.rect.left -= STEP
                if pygame.sprite.spritecollideany(self, bricks) or pygame.sprite.spritecollideany(self, enemies) or \
                        self.rect.left <= 0:
                    self.rect.left += STEP
                else:
                    self.rect.left += 0
                self.image = load_image('tnk4.png')
            if tank_right:
                self.rect.right += STEP
                if pygame.sprite.spritecollideany(self, bricks) or pygame.sprite.spritecollideany(self, enemies) or \
                        self.rect.right >= 800:
                    self.rect.right -= STEP
                else:
                    self.rect.right -= 0
                self.image = load_image('tnk2.png')
            if tank_down:
                self.rect.bottom += STEP
                if pygame.sprite.spritecollideany(self, bricks) or pygame.sprite.spritecollideany(self, enemies) or \
                        self.rect.bottom >= 800:
                    self.rect.bottom -= STEP
                else:
                    self.rect.bottom += 0
                self.image = load_image('tnk3.png')

            if pygame.sprite.spritecollideany(self, enemybullets):
                self.hp -= 20
                if self.hp <= 20:
                    self.kill()
                    dead = True

class EnemyBullet(pygame.sprite.Sprite):
    image = load_image('goodbullet2.png')

    def __init__(self, x, y, pos):
        super().__init__(enemybullets)
        self.pos = pos
        self.image = EnemyBullet.image
        self.rect = self.image.get_rect()
        self.rect.x = x + 15
        self.rect.y = y + 15

    def update(self):
        if shoot_enemy:
            if self.pos == 2:
                if self.rect.y <= 0 or pygame.sprite.spritecollideany(self, bricks) or \
                        pygame.sprite.spritecollideany(self, player_group):
                    self.kill()
                else:
                    self.rect.y -= 4

            elif self.pos == 1:
                if self.rect.y >= 800 or pygame.sprite.spritecollideany(self, bricks) or \
                        pygame.sprite.spritecollideany(self, player_group):
                    self.kill()
                else:
                    self.rect.y += 4

            elif self.pos == 3:
                if self.rect.x >= 800 or pygame.sprite.spritecollideany(self, bricks) or \
                        pygame.sprite.spritecollideany(self, player_group):
                    self.kill()
                else:
                    self.rect.x += 4

            elif self.pos == 4:
                if self.rect.y <= 0 or pygame.sprite.spritecollideany(self, bricks) or \
                        pygame.sprite.spritecollideany(self, player_group):
                    self.kill()
                else:
                    self.rect.x -= 4


class Bullet_up(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(bullets)
        self.x = x
        self.y = y
        self.image = load_image('goodbullet2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x + 10
        self.rect.y = y + 10

    def update(self):
        if self.rect.y <= 0 or pygame.sprite.spritecollideany(self, bricks):
            self.kill()
        else:
            self.rect.y -= 4

class Bullet_down(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(bullets)
        self.x = x
        self.y = y
        self.image = load_image('goodbullet2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x + 10
        self.rect.y = y + 10

    def update(self):
        if self.rect.y >= 800 or pygame.sprite.spritecollideany(self, bricks):
            self.kill()
        else:
            self.rect.y += 4

class Bullet_left(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(bullets)
        self.x = x
        self.y = y
        self.image = load_image('goodbullet2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x + 10
        self.rect.y = y + 10

    def update(self):
        if self.rect.x <= 0 or pygame.sprite.spritecollideany(self, bricks):
            self.kill()
        else:
            self.rect.x -= 4

class Bullet_right(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(bullets)
        self.x = x
        self.y = y
        self.image = load_image('goodbullet2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x + 10
        self.rect.y = y + 10

    def update(self):
        if self.rect.x >= 800 or pygame.sprite.spritecollideany(self, bricks):
            self.kill()
        else:
            self.rect.x += 4

def remarka():
    rem = True
    while rem:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rem = False

        screen.blit(load_image('fon3.png'), (0, 0))
        pygame.display.update()
        clock.tick(60)

def paused():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False
                if event.key == pygame.K_q:
                    terminate()

        screen.blit(load_image('pause.png'), (200, 200))
        pygame.display.update()
        clock.tick(60)


running = True
levels = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            if x >= 100 and x <= 350 and y >= 500 and y <= 540 and dead:
                levels = False
                da = False

            if not da and not levels and x >= 200 and y >= 500 and x <= 900 and y <= 590:
                menu.blit(load_image('info.png'), (0, 0))

            if x >= 450 and x <= 700 and y >= 500 and y <= 550 and dead:
                dead = False
                for i in bricks:
                    i.kill()
                for i in player_group:
                    i.kill()
                for i in enemies:
                    i.kill()
                for i in bullets:
                    i.kill()
                for i in enemybullets:
                    i.kill()

                if lvl == 'firstlevell.txt':
                    lvl = 'firstlevell.txt'
                    player, level_x, level_y = generate_level(load_level(lvl))
                elif lvl == 'secondlevell.txt':
                    lvl = 'secondlevell.txt'
                    player, level_x, level_y = generate_level(load_level(lvl))
                elif lvl == 'thirdlevell.txt':
                    lvl = 'thirdlevell.txt'
                    player, level_x, level_y = generate_level(load_level(lvl))
                elif lvl == 'fourthlevell.txt':
                    lvl = 'fourthlevell.txt'
                    player, level_x, level_y = generate_level(load_level(lvl))

            if x >= 30 and x <= 55 and y >= 0 and y <= 28 and da:
                da = False
                levels = False
                for i in bricks:
                    i.kill()
                for i in player_group:
                    i.kill()
                for i in enemies:
                    i.kill()
                for i in bullets:
                    i.kill()

            if x >= 0 and x <= 25 and y >= 0 and y <= 28 and da:
                remarka()

            if x >= 200 and y >= 300 and x <= 600 and y <= 377 and not levels:
                levels = True

            if x >= 50 and x <= 300 and y >= 400 and y <= 440:
                levels = False
                da = False
                for i in bricks:
                    i.kill()
                for i in player_group:
                    i.kill()
                for i in enemies:
                    i.kill()
                for i in bullets:
                    i.kill()

            if x >= 500 and x <= 750 and y >= 400 and y <= 430:
                for i in bricks:
                    i.kill()
                for i in player_group:
                    i.kill()
                for i in enemies:
                    i.kill()
                for i in bullets:
                    i.kill()

                if lvl == 'firstlevell.txt':
                    lvl = 'secondlevell.txt'
                    player, level_x, level_y = generate_level(load_level(lvl))

                elif lvl == 'secondlevell.txt':
                    lvl = 'thirdlevell.txt'
                    player, level_x, level_y = generate_level(load_level(lvl))

                elif lvl == 'thirdlevell.txt':
                    lvl = 'fourthlevell.txt'
                    player, level_x, level_y = generate_level(load_level(lvl))

            elif levels and x >= 80 and y >= 250 and x <= 180 and y <= 350:
                levels = False
                da = True
                lvl = 'firstlevell.txt'
                player, level_x, level_y = generate_level(load_level(lvl))

            elif levels and x >= 220 and y >= 250 and x <= 320 and y <= 350 and first:
                screen.fill((0, 0, 0))
                levels = False
                da = True
                lvl = 'secondlevell.txt'
                player, level_x, level_y = generate_level(load_level(lvl))

            elif levels and x >= 360 and y >= 250 and x <= 460 and y <= 350 and sec:
                screen.fill((0, 0, 0))
                levels = False
                da = True
                lvl = 'thirdlevell.txt'
                player, level_x, level_y = generate_level(load_level(lvl))
            elif levels and x >= 500 and y >= 250 and x <= 600 and y <= 350 and thrd:
                screen.fill((0, 0, 0))
                levels = False
                da = True
                lvl = 'fourthlevell.txt'
                player, level_x, level_y = generate_level(load_level(lvl))



        if event.type == pygame.KEYDOWN and da:
            if event.key == pygame.K_ESCAPE and not dead:
                paused()

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                move = True
                tank_up = True
                tank_right = False
                tank_left = False
                tank_down = False

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move = True
                tank_left = True
                tank_right = False
                tank_up = False
                tank_down = False


            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                move = True
                tank_right = True
                tank_left = False
                tank_up = False
                tank_down = False

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move = True
                tank_down = True
                tank_right = False
                tank_up = False
                tank_left = False

            if event.key == pygame.K_SPACE:
                shoot = True
                if tank_up:
                    Bullet_up(player.rect.x, player.rect.y)
                elif tank_down:
                    Bullet_down(player.rect.x, player.rect.y)
                elif tank_right:
                    Bullet_right(player.rect.x, player.rect.y)
                elif tank_left:
                    Bullet_left(player.rect.x, player.rect.y)


        if event.type == pygame.KEYUP:
            move = False

    if not da and not levels:
        menu.fill((0, 0, 0))
        menu.blit(main_menu, (0, 0))
        menu.blit(load_image('nadpis.png'), (100, 100))
        menu.blit(load_image('playbutton.png'), (200, 300))
        menu.blit(load_image('dannie.png'), (200, 500))

    if not da and levels:
        level.fill((0, 0, 0))
        level.blit(main_menu, (0, 0))
        level.blit(load_image('level1.png'), (80, 250))
        level.blit(load_image('level2.png'), (220, 250))
        level.blit(load_image('level3.png'), (360, 250))
        level.blit(load_image('level4.png'), (500, 250))
        level.blit(load_image('level5.png'), (640, 250))
        if first:
            level.blit(load_image('allowed.png'), (220, 230))
        if sec:
            level.blit(load_image('allowed.png'), (360, 230))
        if thrd:
            level.blit(load_image('allowed.png'), (500, 230))
        if fou:
            level.blit(load_image('allowed.png'), (640, 230))

    if da and not levels:
        screen.fill(pygame.Color(0, 0, 0))
        tiles_group.draw(screen)
        enemies.draw(screen)
        enemies.update()
        bricks.draw(screen)
        bricks.update()
        bullets.draw(screen)
        bullets.update()
        enemybullets.draw(screen)
        enemybullets.update()
        for i in enemies:
            ticks = pygame.time.get_ticks()
            if (ticks // 1000) % 3 == 0:
                shoot_enemy = True
                EnemyBullet(i.rect.x, i.rect.y, i.flag)

        player_group.draw(screen)
        screen.blit(load_image('que.png'), (0, 0))
        screen.blit(load_image('home.png'), (30, 0))
        if first and lvl == 'firstlevell.txt':
            screen.blit(load_image('fon.png'), (0, 0))
            screen.blit(load_image('lvl1.png'), (225, 200))
            screen.blit(load_image('next.png'), (500, 400))
            screen.blit(load_image('menu.png'), (50, 400))
        if sec and lvl == 'secondlevell.txt':
            screen.blit(load_image('fon.png'), (0, 0))
            screen.blit(load_image('lvl2.png'), (225, 200))
            screen.blit(load_image('next.png'), (500, 400))
            screen.blit(load_image('menu.png'), (50, 400))
        if thrd and lvl == 'thirdlevell.txt':
            screen.blit(load_image('fon.png'), (0, 0))
            screen.blit(load_image('lvl3.png'), (225, 200))
            screen.blit(load_image('next.png'), (500, 400))
            screen.blit(load_image('menu.png'), (50, 400))
        if fou and lvl == 'fourthlevell.txt':
            screen.blit(load_image('fon.png'), (0, 0))
            screen.blit(load_image('lvl4.png'), (225, 200))
            screen.blit(load_image('next.png'), (500, 400))
            screen.blit(load_image('menu.png'), (50, 400))
        if dead:
            screen.blit(load_image('fon.png'), (0, 0))
            screen.blit(load_image('ulose.png'), (200, 200))
            screen.blit(load_image('menu.png'), (100, 500))
            screen.blit(load_image('replay.png'), (450, 500))
        if move:
            player_group.update()


    pygame.display.flip()
    clock.tick(60)

terminate()
