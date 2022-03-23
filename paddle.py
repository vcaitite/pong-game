import pygame
import operator


HEIGHT = 500
WIDTH = 900

class Paddle:
    def __init__(self, surface, color, x_pos, y_pos, width, height):
        self.surface = surface
        self.color = color
        self.position = (x_pos, y_pos, width, height)
        self.start_position = self.position
        self.state_v = "stopped"
        self.state_h = "stopped"
        self.show()

    def show(self):
        pygame.draw.rect(self.surface, self.color, self.position)

    def move_v(self):
        if self.state_v == "up" and self.position[1] > 0:
            self.position = tuple(map(operator.add, self.position, (0, -15, 0, 0)))
        elif self.state_v == "down" and self.position[1] < HEIGHT - self.position[3] - 15:
            self.position = tuple(map(operator.add, self.position, (0, 15, 0, 0)))

    def move_h(self, paddle):
        if paddle == 1:
            if self.state_h == "forward" and self.position[0] < 350 - self.position[2]:
                self.position = tuple(map(operator.add, self.position, (20, 0, 0, 0)))
            elif self.state_h == "back" and self.position[0] > 10:
                self.position = tuple(map(operator.add, self.position, (-20, 0, 0, 0)))
        elif paddle == 2:
            if self.state_h == "forward" and self.position[0] > WIDTH - 350:
                self.position = tuple(map(operator.add, self.position, (-20, 0, 0, 0)))
            elif self.state_h == "back" and self.position[0] < WIDTH - 20 - 10:
                self.position = tuple(map(operator.add, self.position, (20, 0, 0, 0)))


    def restart(self):
        self.position = self.start_position
        self.state = 'stopped'
        self.show()
