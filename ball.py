import pygame
import random #To define the start direction of the ball

WIDTH = 900
HEIGHT = 500


class Ball:
    def __init__(self, surface, color, x_pos, y_pos, radius):
        self.surface = surface
        self.color = color
        self.position = (x_pos, y_pos)
        self.radius = radius
        self.dx_dy = (0, 0)
        self.show()

    def show(self):
        pygame.draw.circle(self.surface, self.color, self.position, self.radius, width=20)

    def start_moving(self):
        direction = [-1, 1]
        self.dx_dy = (direction[random.randint(0, 1)] * 20, direction[random.randint(0, 1)] * random.randint(3, 20))

    def move(self):
        self.position = (self.position[0]+self.dx_dy[0], self.position[1]+self.dx_dy[1])

    def paddle_collision(self):
        self.dx_dy = (-self.dx_dy[0], self.dx_dy[1])

    def wall_collision(self):
        self.dx_dy = (self.dx_dy[0], -self.dx_dy[1])

    def restart_center(self):
        self.position = (WIDTH//2, HEIGHT//2)
        self.dx_dy = (0, 0)
        self.show()


