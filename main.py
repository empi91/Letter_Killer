import pygame
# from classes.letter import Letter
import pathlib

pygame.init()

screen = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Letter Killer")

clock = pygame.time.Clock()

font = pygame.font.Font("graphics/font/Pixeltype.ttf", 64)

game_status = 0
screen_width = screen.get_width()
screen_height = screen.get_height()

# Surface definitions
background = pygame.image.load("graphics/background/background.jpg").convert_alpha()
background = pygame.transform.scale(background, (1280, 720))

start_game_text = font.render("Press SPACE to start", False, "white")
start_game_rect = start_game_text.get_rect(midbottom=(screen_width / 2, 590))

game_over_text = font.render("Press SPACE to restart", False, "white")
game_over_rect = game_over_text.get_rect(midbottom=(screen_width / 2, 590))

# Variables definitions


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_status != 1:
                game_status = 1

    if game_status == 0:
        screen.blit(background, (0, 0))
        screen.blit(start_game_text, start_game_rect)
        pygame.display.update()
        clock.tick(60)
    elif game_status == 2:
        screen.blit(background, (0, 0))
        screen.blit(game_over_text, game_over_rect)
        pygame.display.update()
        clock.tick(60)
    elif game_status == 1:
        screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(60)


