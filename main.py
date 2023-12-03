import pygame

pygame.init()

screen = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Letter Killer")

clock = pygame.time.Clock()

# Surface definitions

# Variables definitions

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
