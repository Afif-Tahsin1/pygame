import pygame
pygame.init()
window : pygame.surface = pygame.display.set_mode((400, 480))
window.fill((255, 255, 255))
GREEN : tuple = (0, 255, 0)
pygame.draw.circle(window, GREEN, (30, 300), 50)
pygame.draw.circle(window, GREEN, (108, 108), 50, 3)
pygame.display.update()
running : bool = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()