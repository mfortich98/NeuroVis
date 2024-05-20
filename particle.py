import math
import random

import pygame


class Particle(pygame.sprite.Sprite):
    def __init__(self, center, radius, angle, *groups):
        super().__init__(*groups)
        self.angle = angle
        self.center = center
        self.radius = radius
        self.position = random.uniform(0.2, 0.4)
        self.ms = 0.005
        self.speed = 0
        self.anchor = 0
        self.tether = 0.3
        self.image = pygame.image.load('images/particle.png').convert_alpha()
        self.rect = self.image.get_rect(center=center)

    def update(self):
        # If the particle is...
        # Under Anchor
        if self.position < self.anchor - self.tether:
            self.speed = self.ms
        # Over Anchor
        elif self.position > self.anchor + self.tether:
            self.speed = -self.ms
        #   Past the center
        if self.position > 1:
            self.speed = -self.ms
            # Outside the outer edge or origin
        elif self.position < 0:
            self.speed = self.ms

        # Update position relative to travel line
        self.position += self.speed

        # Update the sprite's rect position
        self.rect.center = self.center + pygame.math.Vector2(1.1 - self.position, 0).rotate_rad(self.angle) * self.radius
        # print(f'Rad({self.angle}): pos({self.position}), anchor:({self.anchor})')

    def set_anchor(self, anchor):
        self.anchor = anchor
        self.speed = -self.ms if self.position > self.anchor else self.ms





