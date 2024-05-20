import math
import pygame


class Particle(pygame.sprite.Sprite):
    def __init__(self, center, radius, angle, *groups):
        super().__init__(*groups)
        self.angle = angle
        self.destination = center
        self.radius = radius
        self.origin = self.destination + pygame.math.Vector2(self.radius, 0).rotate_rad(angle)
        self.position = self.origin
        self.ms = 0.005
        self.speed = 0
        self.anchor = self.origin
        self.tether = 0.1
        self.image = pygame.image.load('images/particle.png').convert_alpha()
        self.rect = self.image.get_rect(center=center)

    def update(self):
        # If the particle exceeds max distance, it reverses direction
            # Past the center
        if self.position > 1:
            self.speed = -self.ms
            # Outside the outer edge or origin
        if self.position < 0:
            self.speed = self.ms
            # Under Anchor
        if self.position < self.anchor - self.tether:
            self.speed = self.ms
            # Over Anchor
        if self.position > self.angle + self.tether:
            self.speed = -self.ms

        # Update position relative to travel line
        self.position += self.speed

        # Update the sprite's rect position
        self.rect.center += pygame.math.Vector2(self.position, 0).rotate_rad(self.angle) * self.radius
        print(f'{self.angle}: pos({self.rect.center})')

    def set_anchor(self, anchor):
        self.anchor = anchor




