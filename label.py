import pygame


class Label:
    def __init__(self, surface):
        self.text = ""
        self.text_color = (255, 255, 255)
        self.font = pygame.freetype.SysFont('Sans', 16)
        self.surface = surface

    def update(self, data):
        self.text = f"Synch value 1: {data[0]:.2f}\nSynch value 2: {data[1]:.2f}"

    def draw(self):
        lines = self.text.split("\n")
        line_loc = 14
        surface = pygame.image.load('images/label.png').convert_alpha()
        for line in lines:
            text_rect = self.font.get_rect(line)
            text_rect.left = 11
            text_rect.top = line_loc
            line_loc += self.font.size
            self.font.render_to(surface, text_rect.topleft, line, self.text_color)

        self.surface.blit(surface, (0, 0))
