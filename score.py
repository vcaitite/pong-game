import pygame

COLOR_WHITE = (0xFF, 0xFF, 0xFF)


class Score:
    def __init__(self, surface, goals, x_pos, y_pos):
        self.surface = surface
        self.goals = goals
        self.position = (x_pos, y_pos)
        self.text_font = pygame.font.SysFont('Helvetica', 60, italic=False, bold=True)
        self.label = self.text_font.render(self.goals, 0, COLOR_WHITE)

    def show(self):
        self.surface.blit(self.label, (self.position[0] - self.label.get_rect().width // 2, self.position[1]))

    def increase(self):
        goals = int(self.goals) + 1
        self.goals = str(goals)
        self.label = self.text_font.render(self.goals, 0, COLOR_WHITE)

    def restart(self):
        self.goals = '0'
        self.label = self.text_font.render(self.goals, 0, COLOR_WHITE)
