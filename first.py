import pygame

box = input().split()
w = int(box[0])
h = int(box[1])

pygame.init()
size = witdhn, height = 300, 300
screen = pygame.display.set_mode(size)


def draw():
    color = pygame.Color(50, 150, 50)
    hsva = color.hsva
    color.hsva = (h, 100, 75, hsva[3])
    pygame.draw.rect(screen, color, (150 - w // 2, 150 - w // 2, w, w))
    first = w // 2
    color.hsva = (h, 100, 100, hsva[3])
    pygame.draw.polygon(screen, color, [(150 - w // 2, 150 - w // 2), (150 - w // 2 + first, 150 - w // 2 - first),
                                        (150 - w // 2 + first * 3, 150 - w // 2 - first),
                                              (100 + first * 2, 150 - w // 2)])
    color.hsva = (h, 100, 50, hsva[3])
    pygame.draw.polygon(screen, color, [(150 - w // 2 + first * 2, 150 - w // 2 + first * 2),
                                        (150 - w // 2 + first * 2, 150 - w // 2),
                                        (150 - w // 2 + first * 3, 150 - w // 2 - first),
                                        (150 - w // 2 + first * 3, (150 - w // 2 - first) + w)])

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
