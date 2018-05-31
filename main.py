import pygame
from players.player import Player
from enemies.enemy import Enemy
from inputs.input_manager import InputManager
from game_objects import *

BG_COLOR = (255, 153, 123)

# 1. Init pygame
pygame.init()

# 2. Game window & canvas
SIZE = (600, 800)
canvas = pygame.display.set_mode(SIZE)

# 3. Clock
clock = pygame.time.Clock()

input_manager = InputManager()
player = Player(10, 300, input_manager)
enemy = Enemy(200, 80)


add(player)
add(enemy)



# 3. Game loop
loop = True
right_pressed = False
left_pressed = False

# 1: Describe input
# 2: Give it player

while loop:
    # Game Loop 1: Events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            input_manager.update(event)

    print(input_manager)

    update()

    # Game Loop 2: Draw
    canvas.fill(BG_COLOR)
    pygame.display.set_caption("Micro war")

    render(canvas)

    # Game Loop 3: Delay and flip
    pygame.display.flip()
    clock.tick(60)
