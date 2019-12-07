import pygame

box = input().split()
w = int(box[0])
h = int(box[1])

pygame.init()
size = witdhn, height = 300, 300
screen = pygame.display.set_mode(size)


def draw():
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, w, w))
    first = w // 2
    pygame.draw.polygon(screen, (0, 0, 255), [(100, 100), (100 + first, 100 - first), (100 + first * 3, 100 - first),
                                              (100 + first * 2, 100)])
    pygame.draw.polygon(screen, (0, 255, 0), [(100 + first * 2, 100 + first * 2), (100 + first * 2, 100), (100 + first * 3, 100 - first), (100 + first * 3, (100 - first) + w)])

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
