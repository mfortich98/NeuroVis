import math
import pygame


class Particle(pygame.sprite.Sprite):
    def __init__(self, angle, radius, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('images/particle.png').convert_alpha()
        self.rect = self.image.get_rect(center=(0, 0))
        self.angle = angle
        self.radius = radius
        self.anchor = 0
        self.speed = 200
        self.tether = 50

    def update(self):
        # Update radius (distance from center)
        self.radius += self.speed

        # If the particle exceeds max distance, it reverses direction
        if self.radius > self.tether + self.anchor or self.radius < 0 or self.radius < self.tether - self.anchor:
            self.speed = -self.speed

        # Calculate the new position based on polar coordinates
        x = self.rect.center.x + self.radius * math.cos(self.angle)
        y = self.rect.center.y + self.radius * math.sin(self.angle)

        # Update the sprite's rect position
        self.rect.center = (x, y)

    def set_anchor(self, anchor):
        self.anchor = anchor



