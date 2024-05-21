import math
import random
import pygame


class Particle(pygame.sprite.Sprite):
    def __init__(self, ms, tether, center, radius, angle, *groups):
        super().__init__(*groups)
        self.angle = angle
        self.center = center
        self.radius = radius
        self.position = random.uniform(0.2, 0.4)
        self.ms = ms
        self.speed = 0
        self.anchor = 0
        self.tether = tether
        self.image = pygame.image.load('images/particle1.png').convert_alpha()
        self.rect = self.image.get_rect(center=center)

    def update(self):
        # If the particle is...
        if self.tether == 0:
            if self.anchor + 0.01 > self.position > self.anchor - 0.01:
                self.speed = 0
        # Under Anchor
        elif self.position < self.anchor - self.tether:
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
        self.rect.center = (self.center
                            + pygame.math.Vector2(1.05 - self.position, 0).rotate_rad(self.angle)
                            * self.radius)
        # print(f'Rad({self.angle}): pos({self.position}), anchor:({self.anchor})')

    def set_anchor(self, anchor):
        self.anchor = anchor
        self.speed = -self.ms if self.position > self.anchor else self.ms





