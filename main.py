import pygame
import random
import string
from classes.letter import Letter


def spawn_letter():
    if len(list_of_letters) <= 2:
        letter = random.choice(string.ascii_uppercase)
        x_spawn_pos = random.randint(0, screen_width)
        y_spawn_pos = 0
        letter_obj = Letter(letter, x_spawn_pos, y_spawn_pos)

        if not list_of_letters:
            letter_obj.add_to_list(list_of_letters)

        letter_obj.add_to_list(list_of_letters)
        print(len(list_of_letters))

    return 0


def check_key(key):
    for letter in list_of_letters:
        if letter.name.lower() == key:
            list_of_letters.remove(letter)
    return 0


pygame.init()

screen = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Letter Killer")

clock = pygame.time.Clock()

# Variables definitions
font = pygame.font.Font("graphics/font/Pixeltype.ttf", 64)
font_letters = pygame.font.Font("graphics/font/Pixeltype.ttf", 100)

list_of_letters = []

game_status = 0
lives_left = 3
score = 0
level = 1
screen_width = screen.get_width()
screen_height = screen.get_height()

# Surface definitions
background = pygame.image.load("graphics/background/background.jpg").convert_alpha()
background = pygame.transform.scale(background, (1280, 720))

start_game_text = font.render("Press SPACE to start", False, "white")
start_game_rect = start_game_text.get_rect(midbottom=(screen_width / 2, 590))

game_over_text = font.render("Press SPACE to restart", False, "white")
game_over_rect = game_over_text.get_rect(midbottom=(screen_width / 2, 590))

lives_left_text = font.render(f"Lives: {lives_left}", False, "white")
lives_left_rect = lives_left_text.get_rect(midleft=(10, 700))

score_text = font.render(f"Score: {score}", False, "white")
score_rect = score_text.get_rect(midright=(1270, 700))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_status != 1:
                game_status = 1
            elif game_status == 1:
                check_key(pygame.key.name(event.key))
    if lives_left == 0:
        game_status = 2

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
        spawn_letter()
        screen.blit(background, (0, 0))
        screen.blit(lives_left_text, lives_left_rect)
        screen.blit(score_text, score_rect)
        for item in list_of_letters:
            item.move(level)
            item.display(font_letters, screen)
        pygame.display.update()
        clock.tick(60)





