import pygame
from bullets.bullet import Bullet
from game_objects import *
# Game
# Properties + Function mixed up => classified
# Combine class
# 3 classes: Cat(p + m), Rock(m + p), Raindrop(m + p), function, variables
class Player:
    # 1. Describe properties (Properies: image, x, y)
    def __init__(self, x, y, input_manager):
        self.image = pygame.image.load('images/player/player1.png')
        self.x = x
        self.y = y
        self.input_manager = input_manager

    def update(self):
        if self.input_manager.right_pressed:
            self.x += 3
        if self.input_manager.left_pressed:
            self.x -= 3
        if self.input_manager.up_pressed:
            self.y -= 3
        if self.input_manager.down_pressed:
            self.y += 3

        if self.input_manager.x_pressed:
            #1 Create bullet
            new_bullet = Bullet(self.x, self.y)

            #2 Add enemy created bullet into pool (game_objects)
            add(new_bullet)

    def render(self, canvas):
        canvas.blit(self.image, (self.x, self.y))
