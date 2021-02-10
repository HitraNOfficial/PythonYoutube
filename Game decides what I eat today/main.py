import pygame
import math
import random

# Initialize the game
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
PLAYER_SPEED = 0.4
PLAYER_Y_POSITION = 540
PLAYER_MIN_X_POSITION = 0
PLAYER_MAX_X_POSITION = 736
PLAYER_IMAGE = pygame.image.load('basket.png')

PRESENT_STARTING_Y = -64
PRESENT_SPEED = 0.3
PRESENT_IMAGE = pygame.image.load('present.png')

foods = ['Frozen pizza', 'Chorizo', 'Salami', 'Banitsa',
         'Eggs', 'Pasta sauce', 'Spaghetti', 'Mayo', 'Chocolate',
         'Ketchup', 'Barbeque sauce', 'Meat balls', 'Sliced cheese',
         'Banana', 'Orange', 'Waffle', 'Milk', 'Oats']


def draw_player(current_x):
    screen.blit(PLAYER_IMAGE, (current_x, PLAYER_Y_POSITION))


def draw_present(current_x, current_y):
    screen.blit(PRESENT_IMAGE, (current_x, current_y))


def handle_movement(event):
    speed = 0
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            speed = -PLAYER_SPEED
        if event.key == pygame.K_RIGHT:
            speed = PLAYER_SPEED

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            speed = 0

    return speed


screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load('background.png')
pygame.display.set_caption('Feed me!')
current_player_x = 370
current_speed = 0
player_bounds = pygame.Rect((current_player_x, PLAYER_Y_POSITION), (64, 64))

current_present_x = random.randint(0, 736)
current_present_y = PRESENT_STARTING_Y
present_bounds = pygame.Rect((current_present_x, current_present_y), (64, 64))
is_present_collected = False

food_in_present = foods[random.randint(0, (len(foods) - 1))]

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        current_speed = handle_movement(event)

    # calculate player borders
    current_player_x += current_speed
    if current_player_x <= PLAYER_MIN_X_POSITION:
        current_player_x = PLAYER_MIN_X_POSITION
    elif current_player_x >= PLAYER_MAX_X_POSITION:
        current_player_x = PLAYER_MAX_X_POSITION

    current_present_y += PRESENT_SPEED

    player_bounds.x = current_player_x
    present_bounds.y = current_present_y
    if player_bounds.colliderect(present_bounds):
        is_present_collected = True
        print('CONGRATULATIONS! You found: ' + food_in_present)

    if (current_present_y >= HEIGHT - 64) or is_present_collected:
        current_present_y = PRESENT_STARTING_Y
        current_present_x = random.randint(0, 736)
        present_bounds.x = current_present_x
        present_bounds.y = current_present_y
        is_present_collected = False
        food_in_present = foods[random.randint(0, len(foods) - 1)]

    draw_player(current_player_x)
    draw_present(current_present_x, current_present_y)
    pygame.display.update()
