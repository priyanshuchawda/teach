# If not already installed, install pygame using: pip install pygame

import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 255))
    pygame.display.flip()

pygame.quit()
