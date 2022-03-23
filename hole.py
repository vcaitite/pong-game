import pygame

WIDTH = 900
HEIGHT = 500


class Hole:

    def __init__(self, surface, hole_image, x_pos, y_pos):
        self.surface = surface
        self.start_position = (x_pos, y_pos)
        self.speed = 0
        self.hole_surf = hole_image
        self.hole_rect = hole_image.get_rect(center=(x_pos, y_pos))
        self.show()

    def show(self):
        self.surface.blit(self.hole_surf, self.hole_rect)

    def start_moving(self, speed):
        self.speed = speed

    def move(self, hole):
        if hole == 1:
            self.hole_rect.centerx -= self.speed
        elif hole == 2:
            self.hole_rect.centerx += self.speed

    def limit_collision(self):
        self.speed = -self.speed

    def restart(self):
        self.hole_rect.centerx = self.start_position[0]
        self.hole_rect.centery = self.start_position[1]
        self.speed = 0
        self.show()


