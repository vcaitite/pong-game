import pygame
import operator


HEIGHT = 500

class Paddle:
    def __init__(self, surface, color, x_pos, y_pos, width, height):
        self.surface = surface
        self.color = color
        self.position = (x_pos, y_pos, width, height)
        self.state = "stopped"
        self.show()

    def show(self):
        pygame.draw.rect(self.surface, self.color, self.position)

    def move(self):
        if self.state == "up" and self.position[1] > 0:
            self.position = tuple(map(operator.add, self.position, (0, -15, 0, 0)))
        elif self.state == "down" and self.position[1] < HEIGHT - self.position[3]:
            self.position = tuple(map(operator.add, self.position, (0, 15, 0, 0)))

    def restart(self):
        self.position = (self.position[0], HEIGHT//2 - self.position[3]//2, self.position[2], self.position[3])
        self.state = 'stopped'
        self.show()
