import pygame
import random
import string
from classes.letter import Letter


def spawn_letter():
    if len(list_of_letters) <= 7:
        letter = random.choice(string.ascii_uppercase)
        x_spawn_pos = random.randint(0, screen_width)
        y_spawn_pos = 0
        letter_obj = Letter(letter, x_spawn_pos, y_spawn_pos)
        letter_obj.add_to_list(list_of_letters)
    return 0


def check_key(key, scr, lvl):
    for letter in list_of_letters:
        if letter.name.lower() == key:
            list_of_letters.remove(letter)
            scr += 1
            if scr > 0 and scr % 5 == 0:
                lvl += 0.3
    return scr, lvl


def display_score():
    score_text = font.render(f"Score: {score}", False, "white")
    score_rect = score_text.get_rect(midright=(1270, 700))
    screen.blit(score_text, score_rect)
    return 0


def display_lives(live_left):
    lives_left_text = font.render(f"Lives: {live_left}", False, "white")
    lives_left_rect = lives_left_text.get_rect(midleft=(10, 700))
    screen.blit(lives_left_text, lives_left_rect)
    return 0


def check_lives(lives):
    for letter in list_of_letters:
        if letter.y_pos >= 720:
            lives -= 1
            list_of_letters.remove(letter)
    return lives


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

spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_timer, 800)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_status == 0:
                game_status = 1
            elif event.key == pygame.K_SPACE and game_status == 2:
                lives_left = 3
                score = 0
                level = 1
                list_of_letters = []
                game_status = 1
            elif game_status == 1:
                score, level = check_key(pygame.key.name(event.key), score, level)
        if event.type == spawn_timer and game_status == 1:
            spawn_letter()

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
        screen.blit(background, (0, 0))

        display_score()
        lives_left = check_lives(lives_left)
        display_lives(lives_left)

        for item in list_of_letters:
            item.move(level)
            item.display(font_letters, screen)

        pygame.display.update()
        clock.tick(60)
