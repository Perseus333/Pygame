import pygame
import random

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
x_iterations = 0
y_iterations = 0
screen.fill((225, 225, 225))
pygame.init()
for x in range(WIDTH):
    x_iterations += 1
    for y in range(HEIGHT):
        y_iterations += 1
        color = random.randint(1, 254)
        pygame.draw.circle(screen, (color,color,color), (x, y), 1)
        pygame.display.update()
