import pygame

WIDTH = 900
HEIGHT = 500


class Portal:

    def __init__(self, surface, portal_image, x_pos, y_pos):
        self.surface = surface
        self.start_position = (x_pos, y_pos)
        self.speed = 0
        self.portal_surf = portal_image
        self.portal_rect = portal_image.get_rect(center=(x_pos, y_pos))
        self.activated = True
        self.show()

    def show(self):
        self.surface.blit(self.portal_surf, self.portal_rect)

    def start_moving(self, speed):
        self.speed = speed

    def move(self, portal):
        if portal == 1:
            self.portal_rect.centerx -= self.speed
        elif portal == 2:
            self.portal_rect.centerx += self.speed

    def limit_collision(self):
        self.speed = -self.speed

    def restart(self):
        self.portal_rect.centerx = self.start_position[0]
        self.portal_rect.centery = self.start_position[1]
        self.activated = True
        self.speed = 0
        self.show()


