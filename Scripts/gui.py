import pygame

pygame.init()

size = (800, 600)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("Munchkin game")

clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            import sys
            pygame.quit()
            sys.exit()

    clock.tick(60)